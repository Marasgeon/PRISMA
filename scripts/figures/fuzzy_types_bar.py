import os
from pathlib import Path
BASE_DIR = Path(os.environ.get('PRISMA_OUT_DIR', str(Path(__file__).resolve().parent.parent / 'figures')))
OUTPUT_PNG = BASE_DIR / 'fuzzy_types_bar.png'

import matplotlib.pyplot as plt
import numpy as np

PROFESSIONAL_COLORS = ['#1F3A5F', '#2E8B8B', '#5A6B7C', '#8B2D3D']
TEXT_COLOR = '#1A2B3C'

fig, ax = plt.subplots(figsize=(9, 6))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

types = ['Takagi-Sugeno\n(T-S)', 'T-S +\nSMC']
counts = [13, 1]
colors_bar = [PROFESSIONAL_COLORS[i] for i in range(len(types))]
bars = ax.bar(range(len(types)), counts, color=colors_bar, edgecolor=TEXT_COLOR, linewidth=1.5, width=0.5)
ax.set_xticks(range(len(types)))
ax.set_xticklabels(types, fontsize=13)
ax.set_xlabel('Fuzzy Architecture', color=TEXT_COLOR, fontsize=14)
ax.set_ylabel('Number of Papers (non-exclusive)', color=TEXT_COLOR, fontsize=14)
ax.tick_params(axis='x', rotation=0, colors=TEXT_COLOR, labelsize=13)
ax.tick_params(axis='y', colors=TEXT_COLOR, labelsize=12)
ax.set_ylim(0, max(counts) + 2)
for spine in ax.spines.values():
    spine.set_edgecolor(TEXT_COLOR)
for bar, count in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15, str(count), ha='center', va='bottom', color=TEXT_COLOR, fontweight='bold', fontsize=13)
plt.tight_layout()
plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Done: fuzzy_types_bar.png")
