import matplotlib.pyplot as plt
import numpy as np

PROFESSIONAL_COLORS = [
    '#1F3A5F',
    '#2E8B8B',
    '#5A6B7C',
    '#8B2D3D',
    '#B8860B',
    '#2D6A4F',
]
TEXT_COLOR = '#1A2B3C'

def darken_color(hex_color, factor=0.75):
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return '#{:02x}{:02x}{:02x}'.format(
        int(rgb[0] * factor), int(rgb[1] * factor), int(rgb[2] * factor)
    )

def lighten_color(hex_color, factor=0.35):
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return '#{:02x}{:02x}{:02x}'.format(
        int(255 - (255 - rgb[0]) * factor),
        int(255 - (255 - rgb[1]) * factor),
        int(255 - (255 - rgb[2]) * factor),
    )

databases = ['Scopus', 'ScienceDirect', 'IEEE Xplore', 'Springer', 'Google Scholar', 'ACM']
found = [9401, 4153, 340, 1000, 772, 145]
after_dedup = [9395, 4153, 340, 1000, 723, 145]
included = [2, 2, 7, 1, 1, 0]
total_found = 15811

dark_colors = [darken_color(c) for c in PROFESSIONAL_COLORS]
light_colors = [lighten_color(c) for c in PROFESSIONAL_COLORS]

fig, ax = plt.subplots(figsize=(12, 8))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

pcts = [f / total_found * 100 for f in found]
size_outer = 0.2
inner_circle_radius = 0.4
labels_outer = [f'{databases[i]}\n{pcts[i]:.1f}%' for i in range(len(databases))]

wedges1, texts1, _ = ax.pie(
    found,
    radius=1,
    colors=dark_colors,
    autopct=lambda p: '',
    pctdistance=0.85,
    startangle=90,
    wedgeprops=dict(width=size_outer, edgecolor='white', linewidth=2),
    textprops={'color': TEXT_COLOR, 'fontsize': 9, 'fontweight': 'bold'},
)

wedges2, texts2 = ax.pie(
    after_dedup,
    radius=1 - size_outer,
    colors=[darken_color(c, 0.85) for c in PROFESSIONAL_COLORS],
    startangle=90,
    wedgeprops=dict(width=size_outer, edgecolor='white', linewidth=2),
)

wedges3, texts3 = ax.pie(
    included,
    radius=1 - 2 * size_outer,
    colors=PROFESSIONAL_COLORS,
    startangle=90,
    wedgeprops=dict(width=size_outer, edgecolor='white', linewidth=2),
    textprops={'color': TEXT_COLOR, 'fontweight': 'bold'},
)

for i, wedge in enumerate(wedges3):
    if included[i] > 0:
        angle = (wedge.theta2 + wedge.theta1) / 2
        mid_radius = 1 - 2.5 * size_outer
        x = mid_radius * np.cos(np.radians(angle))
        y = mid_radius * np.sin(np.radians(angle))
        ax.text(
            x, y, str(included[i]),
            ha='center', va='center', fontsize=10, fontweight='bold', color='black',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.8),
        )

for i, text in enumerate(texts1):
    angle = (wedges1[i].theta2 + wedges1[i].theta1) / 2
    mid_radius = 1 - size_outer / 2
    x = mid_radius * np.cos(np.radians(angle))
    y = mid_radius * np.sin(np.radians(angle))
    text.set_text(labels_outer[i])
    text.set_position((x, y))
    text.set_fontsize(7)
    text.set_fontweight('bold')
    text.set_color(TEXT_COLOR)
    text.set_bbox(dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.8))

centre_circle = plt.Circle((0, 0), inner_circle_radius, fc='#C46B4E', ec='white', linewidth=2)
ax.add_artist(centre_circle)
ax.text(0, 0.03, '13', ha='center', va='center', fontsize=18, fontweight='bold', color='white')
ax.text(0, -0.08, 'Papers', ha='center', va='center', fontsize=8, fontweight='bold', color='white')

legend_databases = ['ACM Digital Library', 'Google Scholar', 'Springer', 'IEEE Xplore', 'ScienceDirect', 'Scopus']
legend_found = [145, 772, 1000, 340, 4153, 9401]
legend_pcts = [f / sum(legend_found) * 100 for f in legend_found]

legend_labels = [
    r'$\mathbf{Records\ Found:}$ 15,811',
    r'$\mathbf{After\ Dedup:}$ 15,756',
    r'$\mathbf{Included:}$ 13',
    '',
]
legend_labels += [
    f'{legend_databases[i]}: {legend_found[i]:,} ({legend_pcts[i]:.1f}%)'
    for i in range(len(legend_databases))
]

empty_handles = [plt.Rectangle((0, 0), 1, 1, facecolor='none', edgecolor='none') for _ in range(4)]
colored_handles = [plt.Rectangle((0, 0), 1, 1, facecolor=c, edgecolor='none') for c in dark_colors[::-1]]
all_handles = empty_handles + colored_handles

fig.legend(
    all_handles, legend_labels,
    loc='lower center', bbox_to_anchor=(0.5, 0.08), ncol=2, fontsize=8,
    frameon=True, title='Total papers per database',
)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.savefig('database_contributions_pie.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('Generated database_contributions_pie.png')
