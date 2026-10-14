import matplotlib.pyplot as plt

PROFESSIONAL_COLORS = [
    '#1F3A5F', '#2E8B8B', '#5A6B7C', '#8B2D3D', '#B8860B', '#2D6A4F'
]
TEXT_COLOR = '#1A2B3C'

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

domains = [
    'Serial\n(2-DoF)',
    'Single-Link\nRobots',
    'Space\nManipulators',
    'Dual\nManipulator',
    'Flexible-Joint\nRobot',
    'General/\nStandard',
]
counts = [7, 2, 1, 1, 1, 1]
colors_bar = [PROFESSIONAL_COLORS[i] for i in range(len(domains))]
bars = ax.bar(range(len(domains)), counts, color=colors_bar, edgecolor=TEXT_COLOR, linewidth=1.5, width=0.6)
ax.set_xticks(range(len(domains)))
ax.set_xticklabels(domains, fontsize=13)
ax.set_xlabel('Application Domain', color=TEXT_COLOR, fontsize=14)
ax.set_ylabel('Number of Papers', color=TEXT_COLOR, fontsize=14)
ax.tick_params(axis='x', rotation=0, colors=TEXT_COLOR, labelsize=13)
ax.tick_params(axis='y', colors=TEXT_COLOR, labelsize=12)
ax.set_ylim(0, max(counts) + 1)
for spine in ax.spines.values():
    spine.set_edgecolor(TEXT_COLOR)
for bar, count in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, str(count), ha='center', va='bottom', color=TEXT_COLOR, fontweight='bold', fontsize=13)
plt.tight_layout()
plt.savefig('application_domains_bar.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Done: application_domains_bar.png")
