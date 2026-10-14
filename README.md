# PRISMA Methodology

This repository contains the scripts, data files, and protocol text used to produce the PRISMA ScR scoping review reported in the paper.

The paper maps the intersection of fuzzy logic control, descriptor systems, and robotic manipulators. The full text search used one Boolean query across six databases. The screening step applied a four concept keyword matcher to title and abstract fields. A second deduplication step consolidated cross database records. Full text assessment yielded the final set of thirteen studies. All included studies employ Takagi Sugeno fuzzy models. The fourteen studies that used only singular perturbation were excluded as false positives.

## Folder layout

```
docs                  Review protocol and method notes
flowchart             Mermaid source and matplotlib renderer
data                  Per stage counts, per database counts, included papers, quality dimensions
scripts/per_database  One workflow script per database (ACM, GoogleScholar, IEEEXplore, MDPI, ScienceDirect, Springer, Scopus)
scripts/sensitivity   Three NO concept sensitivity scripts (no_flc, no_manipulator, no_singular)
scripts/figures       Eight matplotlib scripts that produce the paper figures
flowchart             One renderer that turns the Mermaid source into the flowchart PNG
```

## Running the scripts

Each script reads CSVs from a data directory. By default the data directory is `data/<dbname>` relative to the repo root. Override with the environment variable `PRISMA_DATA_DIR` for the per database and sensitivity scripts, `PRISMA_OUT_DIR` for the figure scripts, and `PRISMA_FLOW_DIR` for the flowchart renderer.

```
pip install -r requirements.txt
export PRISMA_DATA_DIR=/path/to/per_db_csvs
export PRISMA_OUT_DIR=/path/to/figures
export PRISMA_FLOW_DIR=/path/to/flowchart_dir
python scripts/per_database/ieeexplore.py
python scripts/figures/fuzzy_types_bar.py
python flowchart/render_flowchart2.py
```

The per database scripts read `INPUT_CSV` from the data directory, apply the four concept keyword matcher, deduplicate by DOI and title similarity, write a screening log, and produce the per database flowchart. The sensitivity scripts (no_flc, no_manipulator, no_singular) repeat the same workflow with one concept removed from the matcher, demonstrating how much each concept group contributes to filtering. The figure scripts reproduce the eight figures used in the paper from the same per paper counts. The flowchart renderer reads the Mermaid source file and produces the PNG used in the paper.

## Method summary

Search query (single Boolean, used identically in all six databases):

```
("FLC" OR "fuzzy") AND ("control" OR "robotic") AND ("manipulator") AND ("singular" OR "descriptor")
```

Four concept keyword matcher applied to title and abstract after download. Concepts are fuzzy terms, control terms, robot or manipulator terms, and descriptor or singular terms. Broader fuzzy synonyms (Takagi Sugeno, Mamdani, neuro fuzzy) and additional descriptor synonyms (differential algebraic, implicit system, semi state) were applied only at the post export screening step to keep the search query compact and reproducible.

Per database deduplication by DOI immediately after export removes intra database duplicates. Cross database deduplication by DOI and title similarity runs after the year filter so that the same paper indexed under different publishers can be collapsed. The 2016 to 2026 year window is applied as a state of the art filter after screening to allow the three NO concept sensitivity queries to share a single baseline.

Quality assessment uses a six dimension rubric with a maximum of thirteen points. The dimensions are controller design clarity, stability analysis rigor, descriptor or singular formulation, experimental validation, performance metrics reporting, and reproducibility. The thirteen included studies yield a mean of 10.54 out of 13 with a median of 10 and a range of 10 to 12. The per study dimensional matrix used to derive these means is published in the paper and the rubric anchor definitions are given in the paper quality assessment section.

## Data files

The data folder contains the canonical per stage and per database counts from the paper.

- `data/prisma_summary.csv` records the PRISMA flow stage counts.
- `data/database_contributions.csv` records the per database found, after dedup, and included counts.
- `data/included_papers.csv` lists the thirteen included descriptor studies.
- `data/quality_dimensions.csv` records the per dimension mean quality scores.

The per database raw CSVs (the actual exports from each database) are not included in this repo to keep the size small. They are referenced by the per database scripts and are needed to reproduce the screening exactly. The env var `PRISMA_DATA_DIR` should point to a directory that contains the seven per database sub directories with the same names as the script sub directories.

## Files used in the paper

- `flowchart/flowchart1_mermaid.txt` is the Mermaid source for the identification and screening flowchart.
- `flowchart/flowchart2_mermaid.txt` is the Mermaid source for the eligibility and inclusion flowchart.
- `flowchart/render_flowchart2.py` is the matplotlib renderer that turns the Mermaid source into the PNG used in the paper.
- `docs/review_protocol.md` is the cleaned review protocol that informed the search and screening setup.
