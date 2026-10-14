import os
from pathlib import Path
BASE_DIR = Path(os.environ.get('PRISMA_OUT_DIR', str(Path(__file__).resolve().parent.parent / 'figures')))
OUTPUT_PNG = BASE_DIR / 'performance_metrics_bar.png'

import matplotlib.pyplot as plt
import numpy as np

PROFESSIONAL_COLORS = ['#1F3A5F', '#2E8B8B', '#5A6B7C', '#8B2D3D', '#B8860B', '#2D6A4F']
TEXT_COLOR = '#1A2B3C'

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

metrics = ['Tracking Error\n(MSE, RMSE)', 'Robustness\n(Disturbance)', 'Vibration\nSuppression', 'Steady-State\nError', 'Rise/Settling\nTime', 'Energy\nConsumption']
counts = [7, 10, 0, 0, 0, 0]
colors_bar = [PROFESSIONAL_COLORS[i] for i in range(len(metrics))]
bars = ax.bar(range(len(metrics)), counts, color=colors_bar, edgecolor=TEXT_COLOR, linewidth=1.5, width=0.6)
ax.set_xticks(range(len(metrics)))
ax.set_xticklabels(metrics, fontsize=13)
ax.set_xlabel('Performance Metric', color=TEXT_COLOR, fontsize=14)
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
print("Done: performance_metrics_bar.png")
