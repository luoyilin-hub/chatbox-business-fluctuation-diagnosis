# Data and implementation modes

## Plan only

Return the metric tree, required tables and fields, comparison logic, drill order, expected outputs, quality checks, and decision criteria. Do not imply that data was queried.

## Read-only JDBC or direct query

1. Reuse the configured read-only connection and inspect current schemas before relying on remembered fields.
2. Keep credentials outside SQL and generated artifacts.
3. Write modular SQL for reconciliation, top-level decomposition, dimensions, anomalies, and optional branches.
4. Hash personal identifiers in ordinary outputs; expose raw values only when explicitly requested and authorized.
5. Reconcile segmented totals to the top-line population and amount.
6. Preserve SQL, aggregate outputs, analysis code, and an explicit cutoff time.

Do not assume a past schema still exists. In particular, current token-usage date filtering uses Beijing-converted `created_at`, not a removed `dt` partition.

## Spark SQL

Translate the confirmed metric contracts rather than copying one-off JDBC syntax. Prefer layers:

- normalized source layer;
- transaction or event fact at a documented grain;
- historical/as-of lifecycle and entitlement layer;
- target-versus-comparison aggregate layer;
- anomaly and optional behavior branches;
- dashboard-ready output.

Document partitioning, late-arriving data, backfill behavior, timezone, currency, idempotence, and cost controls. Avoid embedding one historical model hypothesis in a general mart.

## Dashboard design

Define metric owner, refresh cadence, data cutoff, default comparison, filters, drill hierarchy, unknown buckets, privacy, and reconciliation checks. Separate summary cards, exact contribution tables, anomaly panels, and optional investigation tabs. A dashboard should make the method inspectable rather than presenting unrelated dimension charts as additive attribution.

## Existing files

Validate row grain, date range, units, filters, and completeness before analysis. State which contracts cannot be verified from the supplied file.
