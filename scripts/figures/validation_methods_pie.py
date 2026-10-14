import os
from pathlib import Path
BASE_DIR = Path(os.environ.get('PRISMA_OUT_DIR', str(Path(__file__).resolve().parent.parent / 'figures')))
OUTPUT_PNG = BASE_DIR / 'validation_methods_pie.png'

import matplotlib.pyplot as plt
import numpy as np

PROFESSIONAL_NAVY = '#1F3A5F'
PROFESSIONAL_GOLD = '#B8860B'

labels = [
    'Simulation Only',
    'Simulation + Hardware',
]
counts = [13, 0]
notes = [
    'Simulation / numerical examples',
    'Physical experiments or HIL',
]
colors = [PROFESSIONAL_NAVY, PROFESSIONAL_GOLD]

fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

wedges, texts = ax.pie(
    counts,
    labels=None,
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.35, edgecolor='white', linewidth=3),
)

for i, (wedge, label, count, note) in enumerate(zip(wedges, labels, counts, notes)):
    angle = (wedge.theta2 + wedge.theta1) / 2
    mid_radius = 1 - 0.35 / 2
    x = mid_radius * np.cos(np.radians(angle))
    y = mid_radius * np.sin(np.radians(angle))
    if sum(counts) > 0:
        pct = count / sum(counts) * 100
    else:
        pct = 0
    ax.text(
        x, y,
        f'{label}\n{count} ({pct:.0f}%)\n{note}',
        ha='center', va='center',
        fontsize=13, fontweight='bold', color='black',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='none', alpha=0.9),
    )

centre_circle = plt.Circle((0, 0), 1 - 0.35, fc='white', ec='white', linewidth=2)
ax.add_artist(centre_circle)

plt.tight_layout()
plt.savefig(OUTPUT_PNG, dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print('Generated validation_methods_pie.png')
