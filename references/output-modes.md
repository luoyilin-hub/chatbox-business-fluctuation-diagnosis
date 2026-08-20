# Output modes

## In-chat conclusion

The complete confirmed intake appears before execution as required by `request-form.md`. After analysis, lead with the business answer, target-versus-comparison magnitude, main change sources, and next action. Use a compact table only when several material findings need to be summarized:

`变化项 | 影响金额或幅度 | 已确认结论 | 分析进度 | 待确认`

Use only these progress labels:

- `已归因`
- `已下拆，原因待确认`
- `需补充数据`
- `尚不明确`

Progress is supporting context, not the main conclusion. Do not create a separate process-status chapter or expose internal analysis workflow terminology.

## Markdown or Feishu report

Use a business narrative rather than an analysis checklist. Unless the user requests another structure, use:

1. `结论摘要`
2. `核心指标对比`
3. `收入变化来源`, or the equivalent source section for a non-revenue target
4. `重点变化项下钻`
5. `其他关键结构检查`
6. `待确认原因与数据需求`
7. `业务建议`
8. `附录：统计口径、数据质量、截止时间与产物`

The report does not repeat the full intake by default; the full intake remains in the pre-execution chat. Include only a concise scope sentence in the report body, and keep detailed metric contracts and quality notes in the appendix.

### Section guidance

- `结论摘要`: state whether the target is above or below each comparison, the main additive change sources, and the decision-relevant interpretation. Integrate the compact progress table here when useful; do not create a separate status section.
- `核心指标对比`: name the metric and comparisons explicitly. Show revenue, orders, payers, frequency, average order value, registrations, or conversion as relevant. Avoid generic method-only headings that do not name the metric or comparison.
- `收入变化来源`: first show one valid arithmetic identity, then a mutually exclusive business-source axis such as new purchase, renewal, upgrade, quota pack, or other purpose. Clearly label overlapping descriptive views.
- `重点变化项下钻`: include only user-requested branches and branches triggered by `mandatory-drilldown-rules.md`. Group them under this parent section instead of placing unrelated branches at the same report level.
- `其他关键结构检查`: summarize geography, payment, client, and anomaly checks. Expand only the material dimensions; otherwise state that no material structural change was found.
- `待确认原因与数据需求`: list only unresolved mechanisms, the exact missing evidence, and the next query or owner. Omit the section when nothing remains.
- `业务建议`: tie each action to a finding and distinguish immediate action from proposed validation.
- `附录`: place detailed metric contracts, data quality, evidence grades, data cutoff, SQL, and artifact links here.

### Required shape for each focused drilldown

Use a result-oriented heading that states the observed answer, for example `付费升级减少：主要集中在 Pro→Pro+` rather than a heading made from a metric name and progress label.

Within the branch, use this sequence:

1. Impact on the target metric and share of the relevant change.
2. First-level decomposition on one valid axis, such as scale, frequency, and price.
3. Further drilldown of every child that still exceeds a trigger.
4. Current business conclusion, with observations separated from supported mechanism.
5. One progress label and, when needed, the exact data or validation still required.

Do not add contribution percentages from overlapping axes. When both an arithmetic view and a product, geography, or client view are useful, show them as separate lenses.

Creating or editing Feishu is a selected deliverable, not a required analysis step. Reuse the same evidence and contracts across local and Feishu versions.

## SQL deliverable

Provide executable SQL plus a short contract header: grain, period, comparison, filters, amount units, timezone, status handling, and expected output columns. Separate production mart SQL from one-off exploratory queries.

## Dashboard specification

Provide page structure, filters, metric dictionary, dimensions, drill interactions, refresh/cutoff, data quality alerts, and reconciliation queries. Identify which views are additive and which are overlapping descriptive lenses.

## Detail outputs

Default to aggregate or hashed identifiers. Include matching coverage and unknown buckets. Keep sensitive raw event values out of broadly shared reports unless the user explicitly requests them and the delivery location is appropriate.
