# Case: Daily multi-branch drilldown regression

## Purpose

This synthetic case tests whether a daily revenue diagnosis continues through material child drivers and remains readable to a business audience. It generalizes a repeated failure mode; its amounts and segments are not universal daily assumptions.

## Intake snapshot

- Metric: gross successful-payment revenue, registrations, and first-payment conversion
- Target period: one complete Beijing business day
- Comparisons: previous day, another user-specified recent day, and a confirmed multi-day mean baseline
- Scope: all business, with product purpose, payment route, and registration cohort drilldowns
- Background: no confirmed product or routing change at intake
- Depth: complete business drilldown
- Execution: existing reconciled query results
- Deliverable: in-chat conclusion and Feishu-ready report

## Initial partial findings

- Paid-upgrade revenue is materially lower, but only the order-type total is known.
- Quota-pack revenue is materially lower, while behavior has been measured only among quota-pack buyers.
- A previously material channel-currency cell falls to zero near a visible time breakpoint.
- Registrations are not down proportionally, but registration-to-first-payment conversion is lower.

These are first-level observations. None is sufficient attribution by itself.

## Required branch behavior

### Paid upgrade decline

Continue from order purpose into plan transition, term, upgrader scale, frequency, price, and eligible-upgrader conversion. If missing annual or high-value orders explain the arithmetic but exposure or configuration is unverified, report `已下拆，原因待确认`, not `已归因`.

### Quota-pack decline

Continue into buyer scale, frequency, price mix, first or repeat behavior, and the eligible active-user buyer rate. Selected buyers cannot be the denominator for buyer-count change. Observational usage differences do not by themselves support `已归因`.

### Payment currency or routing shift

Continue into the channel-currency matrix, breakpoint, initiation-to-success funnel, and configuration or pipeline evidence. Treat routing observation and confirmed routing mechanism as different evidence states. Missing routing history should produce `需补充数据` with the exact log or configuration record named.

### Registration-payment funnel decline

Continue into the lost funnel stage and its hour, source, OS or version, geography, and payment-route contribution under an equal cohort maturation window.

## Expected report behavior

- Use the business sequence `结论摘要` → `核心指标对比` → `收入变化来源` → `重点变化项下钻`.
- Group the four triggered branches under `重点变化项下钻`; do not make internal progress tracking the report's main structure.
- Use result-oriented branch headings and place one of `已归因`, `已下拆，原因待确认`, `需补充数据`, or `尚不明确` beside the conclusion.
- Keep detailed contracts, data quality, cutoff, and artifact links in the appendix.
- Do not create generic management-facing chapters named after internal workflow or completion concepts.

## Regression invariants

- Render and explicitly confirm the complete intake, including every option, before execution.
- Apply materiality triggers recursively, while always honoring explicitly requested branches.
- Do not use selected buyers as the denominator for buyer-count change.
- Keep paid-upgrade transition, scale, frequency, and price effects distinct.
- Treat routing observation and confirmed routing mechanism as different evidence states.
- Equalize registration-cohort maturation before comparing first-payment conversion.
- Continue through every child driver that exceeds a trigger, or record a valid stop condition.
- Keep progress labels secondary to the business conclusion and name the exact next evidence when needed.
- Preserve all-model-first and non-causal behavior rules from the existing Lite quota-pack case.
