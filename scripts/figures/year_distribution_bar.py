import os
from pathlib import Path
BASE_DIR = Path(os.environ.get('PRISMA_OUT_DIR', str(Path(__file__).resolve().parent.parent / 'figures')))
OUTPUT_PNG = BASE_DIR / 'year_distribution_bar.png'

import matplotlib.pyplot as plt
import numpy as np

PROFESSIONAL_COLORS = ['#1F3A5F', '#2E8B8B', '#5A6B7C', '#8B2D3D', '#B8860B', '#2D6A4F', '#C46B4E', '#6B4E8C', '#C8A875', '#4A6B8A']
TEXT_COLOR = '#1A2B3C'

fig, ax = plt.subplots(figsize=(9, 6))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

years = [2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
counts = [0, 4, 1, 1, 2, 1, 2, 1, 1, 0]
colors_bar = [PROFESSIONAL_COLORS[i] for i in range(len(years))]
bars = ax.bar(range(len(years)), counts, color=colors_bar, edgecolor=TEXT_COLOR, linewidth=1.5, width=0.7)
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years, fontsize=13)
ax.set_xlabel('Year', color=TEXT_COLOR, fontsize=14)
ax.set_ylabel('Number of Papers', color=TEXT_COLOR, fontsize=14)
ax.tick_params(colors=TEXT_COLOR, labelsize=12)
for spine in ax.spines.values():
    spine.set_edgecolor(TEXT_COLOR)
for bar, count in zip(bars, counts):
    if count > 0:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, str(count), ha='center', va='bottom', color=TEXT_COLOR, fontweight='bold', fontsize=13)
plt.tight_layout()
plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Done: year_distribution_bar.png")
