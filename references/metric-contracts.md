# Metric contracts

## Periods

Use half-open intervals `[start, end)` after converting business dates to explicit UTC timestamps. Default business timezone is Asia/Shanghai. For partial weeks or months, compare the same elapsed portion of the prior period.

## Revenue and refunds

- Primary gross revenue: successful amount actually paid, converted under an explicitly dated exchange-rate rule.
- Show order count and unique payer count on the same transaction population.
- Analyze refunds separately by payment date and refund-recognition date when both are available.
- Bridge gross revenue to net revenue; do not mix refund behavior into payer motivation without explanation.
- Exclude test-mode data unless the intake explicitly includes it.

## New and existing payers

- New payer: the user's first historical successful payment occurs inside the target period.
- Existing payer: at least one successful payment exists before the target period.
- Registered-and-paid-same-day is a separate label and does not redefine new payer.
- State the user key used for history and its known collision or missingness risks.

## Plans

- Plan at behavior time explains historical behavior and must use an as-of entitlement or transaction history when available.
- Current plan supports operational targeting at query time.
- Keep both fields when possible. Never substitute current plan for historical plan without labeling the limitation.

## Order ordinals

Define first and repeat payments over successful historical transactions, not only the target-period slice. For order-type-specific questions, state whether ordinal is across all payments or only that order type.

## Points and token usage

- `billed_tokens` is the stored billing-bucket unit.
- Unified points equal `billed_tokens × 8` only when `usage_type = 'model-pro'`; all other usage types use `× 1` unless the business configuration is updated.
- The token-usage source is full-refresh and no longer relies on `dt`; filter Beijing business dates from `created_at`.
- Report model calls and unified points separately. Call share, raw-token share, and point share answer different questions.

## Payment-initiation client

Use the payment-initiation event identified by the current event mapping. Attribute the nearest valid OS/client observation at or before initiation, subject to an explicit identity key, time window, and tie-breaking rule. Report exact-match, fallback-match, and unmatched coverage. Do not use a post-payment OS event as the payment-origin client.

## Usage windows

When testing a usage-driven purchase hypothesis, cap behavior at each user's first target payment. Separate fixed historical baseline and recent pre-payment windows. Post-payment usage may describe outcomes but cannot explain the purchase trigger.
