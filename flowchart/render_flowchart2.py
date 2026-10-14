

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(os.environ.get('PRISMA_FLOW_DIR', str(Path(__file__).resolve().parent)))
INPUT_TXT = BASE_DIR / 'flowchart2_mermaid.txt'
OUTPUT_PNG = BASE_DIR / 'flowchart2.png'

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

PROF_COLORS = {
    'start_fill':    '#D6E0EC',
    'start_stroke':  '#1F3A5F',
    'assess_fill':   '#EFE4C7',
    'assess_stroke': '#B8860B',
    'incl_fill':     '#CFE0D0',
    'incl_stroke':   '#2D6A4F',
    'excl_fill':     '#E6D0D4',
    'excl_stroke':   '#8B2D3D',
    'total_fill':    '#D4B8BC',
    'total_stroke':  '#8B2D3D',
    'text':          '#1A2B3C',
    'link_main':     '#1F3A5F',
    'link_excl':     '#8B2D3D',
    'link_incl':     '#2D6A4F',
}

def parse_mermaid_subgraph(text):
    
    nodes = {}
    edges = []
    subgraphs = []

    for m in re.finditer(r'subgraph\s+(\w+)\s*\[([^\]]+)\]', text):
        subgraphs.append({'id': m.group(1), 'title': m.group(2).strip('"')})

    for m in re.finditer(r'(\w+)\["((?:[^"\[\]]|\\"|"<br/>")*?)"\]', text, re.DOTALL):
        node_id = m.group(1)
        node_text = m.group(2)
        nodes[node_id] = node_text

    for m in re.finditer(r'(\w+)\s*(-->|~~~)\s*(\w+)', text):
        edges.append((m.group(1), m.group(3), m.group(2)))

    return nodes, edges, subgraphs

def parse_node_text(raw_text):
    
    text = raw_text.replace('<br/>', '\n')
    n_match = re.search(r'<b>\(n\s*=\s*(\d+)\)</b>', text)
    n_value = n_match.group(1) if n_match else None
    clean = re.sub(r'<[^>]+>', '', text)
    return clean.strip(), n_value

def classify_node(node_id, subgraphs):
    
    mapping = {
        'A': 'start', 'START': 'start_box',
        'B': 'assess', 'ASSESS': 'assess_box',
        'C': 'included', 'INCLUDED': 'included_box',
        'D1': 'excluded', 'D2': 'excluded', 'D3': 'excluded',
        'E': 'total_excluded',
    }
    return mapping.get(node_id, 'default')

def draw_box(ax, x, y, w, h, text, fill, stroke, stroke_width=2, fontsize=11, bold_title=None):
    
    box = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle='round,pad=0.02,rounding_size=0.08',
        linewidth=stroke_width,
        edgecolor=stroke,
        facecolor=fill,
    )
    ax.add_patch(box)
    if bold_title:
        ax.text(x, y + h * 0.15, bold_title, ha='center', va='center',
                fontsize=fontsize + 1, fontweight='bold', color=PROF_COLORS['text'])
        ax.text(x, y - h * 0.15, text, ha='center', va='center',
                fontsize=fontsize, color=PROF_COLORS['text'])
    else:
        ax.text(x, y, text, ha='center', va='center',
                fontsize=fontsize, color=PROF_COLORS['text'],
                wrap=True)

def draw_arrow(ax, x1, y1, x2, y2, color, width=2, style='-'):
    
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='->,head_length=0.4,head_width=0.3',
        linewidth=width,
        color=color,
        linestyle=style,
        mutation_scale=15,
    )
    ax.add_patch(arrow)

def draw_invisible_link(ax, x1, y1, x2, y2):
    
    ax.plot([x1, x2], [y1, y2], 'none')

def main():
    input_path = INPUT_TXT
    output_path = OUTPUT_PNG

    text = input_path.read_text(encoding='utf-8')
    nodes, edges, subgraphs = parse_mermaid_subgraph(text)

    node_info = {}
    for nid, ntext in nodes.items():
        clean, n_val = parse_node_text(ntext)
        node_info[nid] = {'text': clean, 'n': n_val}

    fig, ax = plt.subplots(figsize=(16, 13))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 13)
    ax.set_aspect('equal')
    ax.axis('off')

    positions = {
        'A': (7, 11),
        'B': (7, 9.2),
        'D1': (2.5, 6.8),
        'D2': (7, 6.8),
        'D3': (11.5, 6.8),# Right excluded
        'E': (7, 4.2),
        'C': (7, 1.5),
    }

    sub_regions = {
        'START':    {'pos': (7, 11),   'w': 7,   'h': 1.8, 'fill': PROF_COLORS['start_fill'], 'stroke': PROF_COLORS['start_stroke']},
        'ASSESS':   {'pos': (7, 9.2), 'w': 13,  'h': 1.6, 'fill': PROF_COLORS['assess_fill'], 'stroke': PROF_COLORS['assess_stroke']},
        'INCLUDED': {'pos': (7, 1.5), 'w': 13,  'h': 2.0, 'fill': PROF_COLORS['incl_fill'], 'stroke': PROF_COLORS['incl_stroke']},
    }

    for sg_id, sg in sub_regions.items():
        x, y = sg['pos']
        w, h = sg['w'], sg['h']
        box = FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle='round,pad=0.02,rounding_size=0.1',
            linewidth=3,
            edgecolor=sg['stroke'],
            facecolor=sg['fill'],
            zorder=0,
        )
        ax.add_patch(box)
        title_y = y + h / 2 - 0.15
        if sg_id == 'START':
            title = 'FULL TEXT ASSESMENT'
        elif sg_id == 'ASSESS':
            title = 'ELIGIBILITY ASSESSMENT'
        else:
            title = 'INCLUDED'
        ax.text(x, title_y, title, ha='center', va='center',
                fontsize=12, fontweight='bold', color=PROF_COLORS['text'])

    box_dims = {
        'A': (4, 1.0),
        'B': (4.5, 0.8),
        'D1': (3.4, 1.0),
        'D2': (3.4, 1.0),
        'D3': (3.4, 1.0),
        'E': (3.0, 0.8),
        'C': (3.8, 1.0),
    }

    for nid, (x, y) in positions.items():
        w, h = box_dims.get(nid, (3, 0.8))
        cls = classify_node(nid, subgraphs)
        if cls == 'start' or cls == 'start_box':
            fill, stroke = PROF_COLORS['start_fill'], PROF_COLORS['start_stroke']
        elif cls == 'assess' or cls == 'assess_box':
            fill, stroke = PROF_COLORS['assess_fill'], PROF_COLORS['assess_stroke']
        elif cls == 'included' or cls == 'included_box':
            fill, stroke = PROF_COLORS['incl_fill'], PROF_COLORS['incl_stroke']
        elif cls == 'excluded':
            fill, stroke = PROF_COLORS['excl_fill'], PROF_COLORS['excl_stroke']
        elif cls == 'total_excluded':
            fill, stroke = PROF_COLORS['total_fill'], PROF_COLORS['total_stroke']
        else:
            fill, stroke = '#FFFFFF', PROF_COLORS['text']

        sw = 3 if cls in ('included', 'included_box', 'total_excluded') else 2
        info = node_info.get(nid, {'text': nid, 'n': None})
        text = info['text']
        ax.text(x, y, text, ha='center', va='center',
                fontsize=11 if cls in ('start', 'assess', 'included') else 10,
                fontweight='bold' if cls in ('start', 'assess', 'included', 'total_excluded') else 'normal',
                color=PROF_COLORS['text'],
                zorder=2)
        box = FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle='round,pad=0.02,rounding_size=0.08',
            linewidth=sw,
            edgecolor=stroke,
            facecolor=fill,
            zorder=1,
        )
        ax.add_patch(box)

    draw_arrow(ax, positions['A'][0], positions['A'][1] - 0.5,
               positions['B'][0], positions['B'][1] + 0.4,
               PROF_COLORS['link_main'], width=2.5)

    for d in ['D1', 'D2', 'D3']:
        draw_arrow(ax, positions['B'][0], positions['B'][1] - 0.4,
                   positions[d][0], positions[d][1] + 0.5,
                   PROF_COLORS['link_excl'], width=2)

    for d in ['D1', 'D2', 'D3']:
        draw_arrow(ax, positions[d][0], positions[d][1] - 0.5,
                   positions['E'][0] + (positions[d][0] - positions['E'][0]) * 0.3,
                   positions['E'][1] + 0.4,
                   PROF_COLORS['link_excl'], width=2)

    b_x, b_y = positions['B']
    c_x, c_y = positions['C']
    arrow = FancyArrowPatch(
        (b_x - 1.5, b_y - 0.4),
        (c_x - 1.5, c_y + 0.5),
        connectionstyle='angle3,angleA=180,angleB=90',
        arrowstyle='->,head_length=8,head_width=5',
        linewidth=2.5,
        color=PROF_COLORS['link_incl'],
        zorder=3,
    )
    ax.add_patch(arrow)

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'Generated {output_path}')

BASE_DIR = Path(os.environ.get('PRISMA_FLOW_DIR', str(Path(__file__).resolve().parent)))
INPUT_TXT = BASE_DIR / 'flowchart2_mermaid.txt'
OUTPUT_PNG = BASE_DIR / 'flowchart2.png'

if __name__ == '__main__':
    main()
