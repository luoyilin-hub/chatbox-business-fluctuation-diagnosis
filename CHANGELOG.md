# Change log

## 1.1.0 — 2026-08-20

- Required the complete option-bearing intake to appear first, be re-rendered after changes, and receive explicit confirmation before execution.
- Added recursive materiality triggers for paid-upgrade decline, quota-pack decline, payment currency or routing shifts, and registration-payment funnel decline.
- Added denominator discipline and explicit stop conditions so a material branch cannot stop at a broad segment without continuing into its material child drivers.
- Reworked business-facing output around conclusion summary, core metric comparison, change sources, focused drilldowns, remaining data needs, and actions.
- Added the progress labels `已归因`, `已下拆，原因待确认`, `需补充数据`, and `尚不明确`; removed management-facing process jargon and aggregate completion scores.
- Added a synthetic multi-branch regression case and validation for recursive drilldown behavior, readable report structure, and version consistency.

## 1.0.0 — 2026-08-19

- Created the required intake for day, week, month, partial-period, and custom-range analysis.
- Added the stable business drilldown framework, revenue and lifecycle contracts, anomaly isolation, evidence grades, and conditional model investigation.
- Added JDBC, Spark SQL, dashboard, existing-file, Markdown, Feishu, SQL, and detail-output modes.
- Added maintenance, validation, and versioning rules.
- Added the aggregate Lite quota-pack and upgrade-intent case from 2026-08-18.
