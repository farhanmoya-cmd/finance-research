# Finance Research Toolkit

Seven reusable ChatGPT/Codex skills with selected supporting source files.

## Skills

| Skill | Purpose |
| --- | --- |
| equity-research | Single-stock research and earnings reviews |
| stock-valuation | Python DCF valuation and implied growth |
| value-at-risk | Databricks portfolio risk pipeline |
| systemic-risk | MATLAB systemic-risk analysis |
| finance-database | Instrument discovery and peer universes |
| automated-fundamental-analysis | Sector-relative stock screening |
| draw2d-diagrams | Editable JavaScript diagram applications |

## Uploading to a GitHub repository

Extract this ZIP and upload its contents, preserving the directory structure. Place `plugin.json` and `skills/` at the repository root. Uploading the ZIP file alone does not expose the skill files for discovery.

This archive has no Git history, credentials or installed dependency directories. It contains the same seven skill entrypoints as the private Finance Research Toolkit plugin, with this repository guide and third-party notices added.

## Runtime requirements

The skill instructions and source do not provision Python, MATLAB, Databricks, Node.js, market data or an MCP connection. Follow the individual SKILL.md files. Historical dependency pins and example data require compatibility and freshness checks. Full FinanceDatabase data snapshots and MATLAB sample datasets are omitted.

## Source and licensing

This is a collection of third-party projects, not a single uniformly licensed codebase. Original license files are retained. Read THIRD_PARTY_NOTICES.md before publishing or redistributing the source. Do not add an umbrella MIT license that purports to relicense all bundled code.