# Analysis intake

Complete and confirm this form before execution. Infer and prefill fields from the user's request. Natural-language answers are valid; option letters are shortcuts.

## Rendering contract

Place this complete form before any plan, analysis, conclusion, SQL, or deliverable. Every rendering must include:

- questions 1–9 in order, including optional question 9;
- every lettered option under every question, even when an answer is already known;
- `Current answer`, `Answer source` (`user`, `proposed default`, or `missing`), and `Field status` under each question;
- the confirmation block and execution status at the end.

Do not replace the form with a summary of completed fields. Infer and prefill what the user already supplied, but ask only for missing required answers. Re-render the entire form after any material answer changes. A proposed default is not confirmed merely because it was displayed.

## 1. Metric or phenomenon — required

- A. Revenue
- B. Paying users
- C. Orders
- D. Registration or conversion
- E. Activity or product usage
- F. Points or cost
- G. Custom metric

Record the observed direction, size, and business question when known.

## 2. Target period — required

- A. Single day
- B. Complete calendar week
- C. Complete calendar month
- D. Week or month to date
- E. Custom date range

Use Beijing time unless overridden. Store explicit start and exclusive end timestamps once execution begins.

## 3. Comparison — required

- A. User-specified period
- B. Previous comparable period
- C. Same period last year
- D. Custom comparison

Then confirm stable baseline:

- E. Do not add one
- F. Add one using the default statistic: mean
- G. Add one with a custom range or statistic

If the user did not specify a comparison, propose the configured previous comparable period. Do not invent an additional historical benchmark. Ask whether a stable baseline is wanted; when it is wanted and no statistic is specified, use the mean.

## 4. Scope — required; multiple selections allowed

- A. All business
- B. Mainland versus non-mainland
- C. Country or region
- D. Plan or product
- E. Order type
- F. Client or OS
- G. Payment method or currency
- H. Specified cohort
- I. Custom scope

Record explicit exclusions, test-mode handling, and whether the target is an event-time cohort or a current operational cohort.

## 5. Known context or hypothesis — required

- A. None
- B. Product or plan change
- C. Price change
- D. Model change
- E. Promotion or campaign
- F. Acquisition-channel change
- G. Data-pipeline change
- H. Custom background

Background determines optional branches; it is not a conclusion.

## 6. Analysis depth — required

- A. Basic metric decomposition
- B. Complete business drilldown
- C. Anomaly or concentrated-order investigation
- D. Usage-behavior investigation
- E. Profile or survey investigation
- F. Custom depth

Complete drilldown includes anomaly isolation and routine movement. Profile and survey work follows cohort identification rather than preceding it.

## 7. Execution mode — required; multiple selections allowed

- A. Analysis plan only
- B. Read-only JDBC/direct query
- C. Spark SQL
- D. Dashboard metric design
- E. Analyze existing files or query results

Selected execution does not authorize unrelated writes or external publication.

## 8. Deliverable — required; multiple selections allowed

- A. In-chat conclusion
- B. Markdown report
- C. Feishu document
- D. SQL files
- E. Dashboard specification
- F. Detail table or spreadsheet

## 9. Constraints — optional

Capture deadline, privacy rules, unavailable data, cost or performance limits, required masking, and other restrictions.

## Completion gate

End every rendered form with this confirmation block:

- Required fields 1–8: `complete` or list the missing fields.
- Proposed defaults awaiting acceptance: list them or write `none`.
- Explicit exclusions and constraints: summarize them or write `none`.
- Execution status: `waiting for confirmation` or `confirmed`.

Fields 1–8 must be filled, and the displayed complete form must be explicitly confirmed before execution. A default is valid only after the user accepts it. Any material change to a confirmed answer resets execution status to `waiting for confirmation`. After confirmation, proceed within the selected scope without asking for another redundant confirmation. Pause only when newly discovered ambiguity would materially change the result.
