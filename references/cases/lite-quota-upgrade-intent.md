# Case: Lite quota-pack purchases and upgrade intent

## Purpose

This frozen, aggregate case demonstrates how to analyze willingness to upgrade when a lower-tier cohort buys flexible quota packs. It also demonstrates a named-model investigation that was triggered by an explicit business hypothesis. It must not make V4 or DeepSeek a default branch.

## Intake snapshot

- Metric: quota-pack orders, buyers, and payment amount
- Target period: 2026-08-18 Beijing time
- Supporting history: 2026-08-01 through 2026-08-18
- Scope: quota-pack orders bound to Licenses classified as current Lite for the operational cohort
- Background: Lite-to-Pro costs $16 more and adds 10 million points; quota packs start at $5 for 2.5 million points and add 0.5 million points per additional dollar
- Explicit hypothesis: increased V4 consumption may be causing quota-pack purchases
- Execution: read-only JDBC plus local aggregate analysis
- Deliverable: complete business conclusion

## Analysis path

1. Reconcile buyer, order, and revenue totals.
2. Normalize product list-price tiers separately from actual currency-converted revenue so FX tails do not turn a nominal $20 purchase into $19.99 for decision thresholds.
3. Show single-order price distribution.
4. Aggregate per buyer for the target day, then for the month-to-date history.
5. Separate first or one-off $5 trials from repeat quota-pack behavior.
6. Compare two business thresholds:
   - $16: incremental Lite-to-Pro price;
   - $20: quota-pack cost of the same 10 million points.
7. Segment immediate, accumulated, and weak upgrade signals.
8. Because the intake explicitly named V4, inspect all-model usage first, then V4 calls and unified points.
9. Cap the recent usage window at each buyer's first target payment and compare with a fixed earlier baseline.
10. Distinguish a small acute high-spend cohort from broad month-to-date high consumption.

## Frozen aggregate result

- 311 buyers, 342 orders, and $2,082.88 actual revenue
- 81.87% of orders were at the $5 tier
- Per-buyer target-day median was $5; 12 buyers reached at least $20
- 116 buyers reached at least $20 in month-to-date quota-pack spend
- 57.23% had an earlier August quota-pack purchase
- 36.33% were a target-day $5 purchase with no earlier August quota purchase
- Pre-purchase V4 penetration was 64.63%; V4 represented 51.39% of calls and 52.49% of unified points
- The 12 target-day high-spend buyers had higher V4 penetration and usage intensity, but month-to-date high spend was more consistent with broad all-model consumption than with V4 alone

## Decision logic

The upgrade provides 625,000 points per incremental dollar versus 500,000 points per quota-pack dollar. The same 10 million points cost $20 in packs, so a $16 upgrade is 25% more point-efficient. This supports targeted upgrade messaging for accumulated high-spend users, not a claim that all quota-pack buyers will upgrade.

## Evidence limits

- Flexible one-off spend is not the same commitment as a subscription upgrade.
- The cohort lacks all non-buying Lite users as a full-population control.
- Current plan and plan at purchase time answer different questions.
- V4 association does not prove that V4 caused the purchase.
- Product placement still requires cost, margin, cannibalization, and experiment evidence.

## Regression invariants

- Complete intake before data execution.
- Preserve both single-order and per-user accumulated views.
- Use behavior-time and current plans for their respective purposes.
- Treat $16 and $20 as separate business thresholds even if observed tiers make their target-day counts equal.
- Investigate all models before interpreting the named model.
- Exclude post-payment usage from purchase-trigger evidence.
- Keep observational conclusions non-causal.
