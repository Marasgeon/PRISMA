import matplotlib.pyplot as plt
import numpy as np

PROFESSIONAL_COLORS = ['#1F3A5F', '#2E8B8B', '#5A6B7C', '#8B2D3D', '#B8860B']
TEXT_COLOR = '#1A2B3C'

fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

combos = [
    'T-S Descriptor\n+ PDC',
    'T-S +\nObserver',
    'T-S + Non-PDC\n/ NQLF',
    'T-S +\nSMC',
    'T-S + EET /\nImpulsive'
]
counts = [6, 3, 2, 1, 1]
colors_bar = [PROFESSIONAL_COLORS[i] for i in range(len(combos))]
bars = ax.bar(range(len(combos)), counts, color=colors_bar, edgecolor=TEXT_COLOR, linewidth=1.5, width=0.6)
ax.set_xticks(range(len(combos)))
ax.set_xticklabels(combos, fontsize=12)
ax.set_xlabel('Controller Architecture Combination', color=TEXT_COLOR, fontsize=14)
ax.set_ylabel('Number of Papers', color=TEXT_COLOR, fontsize=14)
ax.tick_params(axis='x', rotation=0, colors=TEXT_COLOR, labelsize=12)
ax.tick_params(axis='y', colors=TEXT_COLOR, labelsize=12)
ax.set_ylim(0, max(counts) + 1)
for spine in ax.spines.values():
    spine.set_edgecolor(TEXT_COLOR)
for bar, count in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, str(count), ha='center', va='bottom', color=TEXT_COLOR, fontweight='bold', fontsize=13)
plt.tight_layout()
plt.savefig('controller_combinations_bar.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Done: controller_combinations_bar.png")
