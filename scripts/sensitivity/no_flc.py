import os
from pathlib import Path
BASE_DIR = Path(os.environ.get('PRISMA_DATA_DIR', str(Path(__file__).resolve().parent.parent / 'data' / 'sensitivity')))
INPUT_RIS = BASE_DIR / 'NO_FLC.ris'

import rispy
import csv
from collections import defaultdict

def normalize_title(title):
    
    if not title:
        return ''
    t = title.lower()
    import re
    t = re.sub(r'[^\w\s]', '', t)
    t = re.sub(r'\s+', ' ', t)
    return t.strip()

def find_duplicates(entries):
    
    duplicates = []
    
    doi_map = defaultdict(list)
    for idx, entry in enumerate(entries):
        doi = entry.get('doi', '').strip() if entry.get('doi') else ''
        if doi:
            doi_map[doi].append(idx)
    
    for doi, indices in doi_map.items():
        if len(indices) > 1:
            duplicates.append({
                'method': 'DOI match',
                'doi': doi,
                'entries': [entries[i].get('authors', ['Unknown'])[0] if entries[i].get('authors') else 'Unknown' for i in indices],
                'titles': [entries[i].get('title', '') for i in indices],
                'years': [entries[i].get('year', '') for i in indices]
            })
    
    title_map = defaultdict(list)
    for idx, entry in enumerate(entries):
        title = entry.get('title', '')
        if title:
            norm_title = normalize_title(title)
            if len(norm_title) > 10:
                title_map[norm_title].append(idx)
    
    for title, indices in title_map.items():
        if len(indices) > 1:
            existing_dois = [entries[i].get('doi', '') for i in indices if entries[i].get('doi')]
            if not existing_dois or len(set(existing_dois)) > 1:
                duplicates.append({
                    'method': 'Title match',
                    'title': entries[indices[0]].get('title', ''),
                    'entries': [entries[i].get('authors', ['Unknown'])[0] if entries[i].get('authors') else 'Unknown' for i in indices],
                    'titles': [entries[i].get('title', '') for i in indices],
                    'years': [entries[i].get('year', '') for i in indices]
                })
    
    return duplicates

def screen_entry(entry):
    
    
    title = (entry.get('title', '') or '').lower()
    abstract = (entry.get('abstract', '') or '').lower()
    year = entry.get('year', '')
    
    combined_text = f"{title} {abstract}"
    
    if year:
        try:
            if int(year) < 1970:
                return 'EXCLUDE', f"Pre-1970 publication (year: {year})"
        except:
            pass
    
    fuzzy_indicators = [
        'fuzzy', 'mamdani', 'sugeno', 'takagi', 'ts fuzzy', 
        'neuro-fuzzy', 'adaptive fuzzy', 'fuzzy pid', 'flc'
    ]
    has_fuzzy = any(indicator in combined_text for indicator in fuzzy_indicators)
    
    robotic_indicators = [
        'robot', 'manipulator', 'arm', 'gripper', 'end-effector',
        'degrees of freedom', 'dof', 'joint', 'robotic'
    ]
    has_robot = any(indicator in combined_text for indicator in robotic_indicators)
    
    has_descriptor = 'descriptor' in combined_text
    has_singular_system = ('singular system' in combined_text or 'singular systems' in combined_text) and 'singularly perturbed' not in combined_text
    
    
    
    if not has_robot:
        return 'EXCLUDE', "No robotic manipulator mentioned"
    
    if not (has_descriptor or has_singular_system):
        return 'EXCLUDE', "No descriptor/singular dynamics mentioned"
    
    if not has_fuzzy:
        return 'EXCLUDE', "No fuzzy logic controller (consistent with NO_FLC query)"
    
    return 'INCLUDE', "Meets all inclusion criteria (NOTE: fuzzy found - unusual for NO_FLC)"

def main():
    print("=" * 60)
    print("PRISMA Review - NO_FLC Database")
    print("=" * 60)
    print("Query: (\"control system\" OR \"robotic control\") AND (\"manipulator\") AND (\"singular\" OR \"descriptor\")")
    print("This database contains papers WITHOUT fuzzy logic control")
    print("=" * 60)
    
    print("\n[1] Parsing RIS file...")
    with open(INPUT_RIS, 'r', encoding='utf-8') as f:
        entries = rispy.load(f)
    
    print(f"    Total entries found: {len(entries)}")
    
    print("\n[2] Performing deduplication...")
    duplicates = find_duplicates(entries)
    
    if duplicates:
        print(f"    Found {len(duplicates)} duplicate groups:")
        for dup in duplicates:
            print(f"      - Method: {dup.get('method', 'N/A')}")
            print(f"        Entries: {', '.join(dup.get('entries', []))}")
    else:
        print("    No duplicates found")
    
    with open('NO_FLC_deduplication_report.txt', 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("DEDUPLICATION REPORT - NO_FLC Database\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total records in database: {len(entries)}\n")
        f.write(f"Duplicate groups found: {len(duplicates)}\n\n")
        
        if duplicates:
            for i, dup in enumerate(duplicates, 1):
                f.write(f"--- Duplicate Group {i} ---\n")
                f.write(f"Method: {dup.get('method', 'N/A')}\n")
                if 'doi' in dup:
                    f.write(f"DOI: {dup['doi']}\n")
                if 'title' in dup:
                    f.write(f"Title: {dup['title']}\n")
                f.write(f"Authors: {', '.join(dup.get('entries', []))}\n")
                f.write(f"Years: {', '.join(dup.get('years', []))}\n")
                f.write("Titles:\n")
                for t in dup.get('titles', []):
                    f.write(f"  - {t}\n")
                f.write("\n")
        else:
            f.write("No duplicates found.\n")
        
        f.write("\n" + "=" * 60 + "\n")
        f.write("DEDUPLICATION COMPLETE\n")
        f.write("=" * 60 + "\n")
    
    print(f"    Deduplication report saved to: NO_FLC_deduplication_report.txt")
    
    print("\n[3] Performing Title & Abstract Screening...")
    
    screening_results = []
    include_count = 0
    exclude_count = 0
    uncertain_count = 0
    
    for entry in entries:
        decision, reason = screen_entry(entry)
        
        authors = entry.get('authors', [])
        if authors:
            if len(authors) > 3:
                authors_str = ', '.join(authors[:3]) + ' et al.'
            else:
                authors_str = ', '.join(authors)
        else:
            authors_str = 'Unknown'
        
        if len(authors_str) > 100:
            authors_str = authors_str[:100] + '...'
        
        abstract = entry.get('abstract', '')
        if len(abstract) > 200:
            abstract = abstract[:200] + '...'
        
        screening_results.append({
            'authors': authors_str,
            'title': entry.get('title', ''),
            'year': entry.get('year', ''),
            'journal': entry.get('journal_name', entry.get('journal', '')),
            'doi': entry.get('doi', ''),
            'decision': decision,
            'reason': reason,
            'abstract': abstract
        })
        
        if decision == 'INCLUDE':
            include_count += 1
        elif decision == 'EXCLUDE':
            exclude_count += 1
        else:
            uncertain_count += 1
    
    print(f"    Screening complete!")
    print(f"    - INCLUDE: {include_count}")
    print(f"    - EXCLUDE: {exclude_count}")
    print(f"    - UNCERTAIN: {uncertain_count}")
    
    csv_file = 'NO_FLC_screening_results.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['authors', 'title', 'year', 'journal', 'doi', 'decision', 'reason', 'abstract']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(screening_results)
    
    print(f"    Screening results saved to: {csv_file}")
    
    print("\n[4] Generating included papers list...")
    included_papers = [r for r in screening_results if r['decision'] == 'INCLUDE']
    
    with open('NO_FLC_included_papers.txt', 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("INCLUDED PAPERS - After Title & Abstract Screening\n")
        f.write("NO_FLC Database\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total included: {len(included_papers)}\n\n")
        
        for i, paper in enumerate(included_papers, 1):
            f.write(f"{i}. {paper['title']}\n")
            f.write(f"   Authors: {paper['authors']}\n")
            f.write(f"   Year: {paper['year']}\n")
            f.write(f"   Journal: {paper['journal']}\n")
            f.write(f"   DOI: {paper['doi']}\n")
            f.write(f"   Reason: {paper['reason']}\n")
            f.write("\n")
    
    print(f"    Included papers list saved to: NO_FLC_included_papers.txt")
    
    print("\n[5] Exclusion reasons summary:")
    reason_counts = {}
    for r in screening_results:
        if r['decision'] == 'EXCLUDE':
            reason = r['reason']
            reason_counts[reason] = reason_counts.get(reason, 0) + 1
    
    for reason, count in sorted(reason_counts.items(), key=lambda x: -x[1]):
        print(f"    - {reason}: {count}")
    
    print("\n" + "=" * 60)
    print("PRISMA FLOW DIAGRAM - NO_FLC Database")
    print("=" * 60)
    print(f)
    
    print("\n[COMPLETE]")
    print("=" * 60)
    
    return {
        'total_records': len(entries),
        'duplicates_found': len(duplicates),
        'included': include_count,
        'excluded': exclude_count,
        'uncertain': uncertain_count
    }

if __name__ == '__main__':
    main()
