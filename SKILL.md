---
name: chatbox-business-fluctuation-diagnosis
description: Diagnose Chatbox revenue, payment, order, conversion, usage, point-consumption, and cost fluctuations over a day, week, month, or custom period. Use when a user wants a structured business drilldown, attribution plan, direct data analysis, Spark SQL, dashboard metric design, or a report. Require the analysis intake before execution; model-specific investigations such as DeepSeek or V4 are conditional branches, not the default path.
---

# Chatbox Business Fluctuation Diagnosis

Use one stable reasoning framework across plan-only, JDBC analysis, Spark SQL, dashboard, and report tasks. Treat tools and deliverables as replaceable adapters rather than the analysis method.

## Required intake

Before querying data, writing executable SQL, designing a dashboard, or producing a final attribution report, read [references/request-form.md](references/request-form.md). Extract answers already present in the user's request, display the completed fields, and ask only for missing required fields. Do not execute until the required fields are complete.

Use defaults from [references/business-config.toml](references/business-config.toml). A completed form authorizes only the execution and deliverables selected in that form.

## Core workflow

After intake is complete, read [references/core-framework.md](references/core-framework.md) and follow the relevant branches:

1. Verify that the fluctuation is real and not caused by data freshness, schema, timezone, currency, refund, test-data, or status issues.
2. Decompose the target metric arithmetically before opening behavioral hypotheses.
3. Separate anomalies and concentrated events from routine business movement. Report both the complete result and the routine result with material anomalies isolated.
4. Drill through lifecycle, order purpose, product, geography, payment, client, and acquisition context as supported by the target metric.
5. Enter usage, model, Agent Mode, survey, or profile branches only when the basic decomposition identifies a relevant cohort or the intake states a relevant hypothesis.
6. Distinguish direct facts, arithmetic attribution, behavioral association, business hypothesis, and experimental evidence.

Use [references/metric-contracts.md](references/metric-contracts.md) whenever computing revenue, payers, first payment, plans, points, refunds, or payment-client attribution. Use [references/attribution-methods.md](references/attribution-methods.md) for contribution, concentration, behavioral windows, and causal-language rules.

## Execution modes

Read [references/data-modes.md](references/data-modes.md) only for the selected mode:

- Plan only: return hypotheses, metrics, drilldown order, required fields, and expected evidence without querying.
- JDBC/direct query: inspect current schemas, write read-only queries, reconcile totals, and preserve reusable SQL and aggregate outputs.
- Spark SQL: express the same contracts as layered CTEs or maintained marts suitable for scheduled execution.
- Dashboard: define grain, dimensions, measures, refresh logic, drill paths, quality checks, and metric ownership before building.
- Existing files: analyze supplied outputs under the same contracts and state coverage limitations.

Read [references/output-modes.md](references/output-modes.md) only for selected deliverables. Do not treat Feishu, Markdown, SQL files, or a dashboard as mandatory unless requested.

## Conditional model investigations

Default to all-model call and unified-point distributions when model usage is relevant. Open a DeepSeek, V4, or other named-model branch only when:

- the intake explicitly asks about that model;
- a price, entitlement, rollout, or routing change creates a model-specific hypothesis; or
- the general model distribution shows a material model-specific shift.

Never promote a model-specific historical case into the default daily path. Pre-purchase behavior may support association; it does not establish causality.

## Cases

Cases illustrate decisions and reusable paths; they are not universal rules. For a quota-pack-to-upgrade question with an explicit V4 hypothesis, read [references/cases/lite-quota-upgrade-intent.md](references/cases/lite-quota-upgrade-intent.md).

## Maintenance mode

When the user explicitly asks to update this skill, read [references/maintenance.md](references/maintenance.md). Propose the affected layer and impact first, wait for confirmation, then make the narrowest change, run `scripts/validate_skill.py`, replay relevant qualitative regression checks, update the version and `CHANGELOG.md`, and summarize behavior changes. Ordinary analysis must not silently modify the skill.
