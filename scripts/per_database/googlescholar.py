

import csv
import re
from pathlib import Path

BASE_DIR = Path(os.environ.get("PRISMA_DATA_DIR", str(Path(__file__).resolve().parent.parent / "data" / "googlescholar")))
INPUT_CSV = BASE_DIR / (["acm_all_with_abstracts.csv", "google_scholar_all_with_abstracts.csv", "ieeexplore_papers.csv", "mdpi_all_with_abstracts.csv", "sciencedirect_all_with_abstracts.csv", "SearchResults_with_abstracts.csv", "scopus_all_with_abstracts.csv"][["acm","googlescholar","ieeexplore","mdpi","sciencedirect","springer","scopus"].index("googlescholar")])
SCREENING_LOG = BASE_DIR / "prisma_screening_log.csv"
INCLUDED_CSV = BASE_DIR / "googlescholar_included_papers.csv"
INCLUDED_RIS = BASE_DIR / "googlescholar_included_papers.ris"
FLOWCHART_TXT = BASE_DIR / "prisma_flowchart.txt"

KEYWORDS = {
    'fuzzy': ['fuzzy', 'flc', 'mamdani', 'sugeno', 'takagi-sugeno', 'neuro-fuzzy', 'neurofuzzy', 'tsk'],
    'control': ['control', 'controller'],
    'manipulator': ['manipulator', 'robot arm', 'robot', 'arm'],
    'singular_descriptor': ['singular', 'descriptor', 'dae', 'algebraic constraint', 'index reduction']
}

def check_keywords(text, keywords):
    
    if not text:
        return False
    text_lower = text.lower()
    return any(kw in text_lower for kw in keywords)

def screen_record(title, abstract, has_abstract):
    
    search_text = f"{title} {abstract}" if has_abstract else title

    has_fuzzy = check_keywords(search_text, KEYWORDS['fuzzy'])
    has_control = check_keywords(search_text, KEYWORDS['control'])
    has_manipulator = check_keywords(search_text, KEYWORDS['manipulator'])
    has_singular = check_keywords(search_text, KEYWORDS['singular_descriptor'])

    missing = []
    if not has_fuzzy:
        missing.append("No fuzzy controller")
    if not has_control:
        missing.append("No control term")
    if not has_manipulator:
        missing.append("No robotic manipulator")
    if not has_singular:
        missing.append("No singular/descriptor dynamics")

    if missing:
        return False, "; ".join(missing)

    return True, "Included"

def main():
    records = []
    included_records = []

    with open(INPUT_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)

    n_identified = len(records)
    print(f"Step 1 - Identification: {n_identified} records found")

    seen_dois = set()
    unique_records = []
    n_duplicates = 0

    for record in records:
        doi = (record.get('doi') or '').strip().lower()
        if doi and doi in seen_dois:
            n_duplicates += 1
        else:
            seen_dois.add(doi)
            unique_records.append(record)

    n_after_dedup = len(unique_records)
    print(f"Step 2 - Deduplication: {n_duplicates} duplicates removed, {n_after_dedup} unique records")

    n_included = 0
    n_excluded_no_fuzzy = 0
    n_excluded_no_manipulator = 0
    n_excluded_no_singular = 0

    screening_results = []

    for record in unique_records:
        title = record.get('title', '') or ''
        abstract = record.get('abstract', '') or ''
        has_abstract = bool(abstract.strip()) and abstract.strip() != "Abstract not available in search results"

        include, reason = screen_record(title, abstract, has_abstract)

        screening_results.append({
            'title': title,
            'authors': record.get('authors', ''),
            'year': record.get('year', ''),
            'doi': record.get('doi', ''),
            'journal': record.get('journal', ''),
            'abstract': abstract[:300] + '...' if len(abstract) > 300 else abstract,
            'include': include,
            'reason': reason
        })

        if include:
            n_included += 1
            included_records.append(record)
        else:
            if "No fuzzy" in reason:
                n_excluded_no_fuzzy += 1
            if "No robotic manipulator" in reason:
                n_excluded_no_manipulator += 1
            if "No singular" in reason:
                n_excluded_no_singular += 1

    print(f"Step 3 - Screening: {n_included} included, {len(unique_records) - n_included} excluded")

    with open(SCREENING_LOG, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'authors', 'year', 'doi', 'journal', 'abstract', 'include', 'reason'])
        writer.writeheader()
        writer.writerows(screening_results)
    print(f"  - Saved: {SCREENING_LOG}")

    if included_records:
        with open(INCLUDED_CSV, 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['title', 'authors', 'year', 'journal', 'doi', 'abstract']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for rec in included_records:
                writer.writerow({k: rec.get(k, '') for k in fieldnames})
        print(f"  - Saved: {INCLUDED_CSV}")

        with open(INCLUDED_RIS, 'w', encoding='utf-8') as f:
            for rec in included_records:
                f.write("TY  - GEN\n")
                f.write(f"TI  - {rec.get('title', '')}\n")
                authors = rec.get('authors', '').split(';')
                for au in authors:
                    if au.strip():
                        f.write(f"AU  - {au.strip()}\n")
                f.write(f"PY  - {rec.get('year', '')}\n")
                f.write(f"DO  - {rec.get('doi', '')}\n")
                f.write(f"AB  - {rec.get('abstract', '')}\n")
                f.write("ER  -\n\n")
        print(f"  - Saved: {INCLUDED_RIS}")

    n_excluded_total = len(unique_records) - n_included

    flowchart_content = f

    if included_records:
        flowchart_content += "================================================================================\n"
        flowchart_content += "                    FINAL INCLUDED PAPERS ({})\n".format(n_included)
        flowchart_content += "================================================================================\n\n"
        for i, rec in enumerate(included_records, 1):
            title = rec.get('title', '')[:80]
            authors = rec.get('authors', 'Unknown')
            year = rec.get('year', 'Unknown')
            doi = rec.get('doi', '')
            flowchart_content += f"{i}. {title}\n"
            flowchart_content += f"   Authors: {authors}\n"
            flowchart_content += f"   Year: {year} | DOI: {doi}\n\n"
    else:
        flowchart_content += "================================================================================\n"
        flowchart_content += "                    NO PAPERS MET INCLUSION CRITERIA\n"
        flowchart_content += "================================================================================\n"

    flowchart_content += f

    with open(FLOWCHART_TXT, 'w', encoding='utf-8') as f:
        f.write(flowchart_content)
    print(f"  - Saved: {FLOWCHART_TXT}")

    print(f"\n{'='*60}")
    print("PRISMA Workflow Complete for Google Scholar")
    print(f"{'='*60}")
    print(f"Identified: {n_identified}")
    print(f"After deduplication: {n_after_dedup}")
    print(f"Included: {n_included}")
    print(f"Excluded: {n_excluded_total}")

if __name__ == "__main__":
    main()