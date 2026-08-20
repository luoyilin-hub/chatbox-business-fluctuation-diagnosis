# Attribution methods

## Top-level decomposition

For multiplicative identities such as payer count × frequency × price, use a symmetric or Shapley-style decomposition when contribution percentages are required. Record the formula. A sequential decomposition is acceptable only when labeled and when order effects are immaterial.

## Segmented contribution

Within a dimension, calculate each cell's target-minus-comparison difference and its share of the overall change. Keep new cells, disappearing cells, and unknown values visible. Do not add country contribution, plan contribution, and OS contribution together because those populations overlap.

## Scale versus mix

When useful, separate:

- scale effect: total population or volume changes with comparison-period mix held constant;
- mix effect: composition changes at target-period scale;
- within-cell rate or price effect.

State the chosen standardization or decomposition method.

## Population and denominator discipline

Define the eligible population before interpreting a rate. A selected outcome cohort, such as quota-pack buyers or successful payers, can describe behavior within that cohort but cannot explain why the number of buyers or payers changed. To explain outcome volume, compare an eligible full-population denominator and its outcome rate, or label the explanation as incomplete and name the missing denominator.

Keep numerator and denominator on consistent event-time, eligibility, geography, plan, and identity contracts. Show unmatched and unknown populations rather than silently dropping them.

## Materiality and recursive drilldown

Use the configured thresholds as investigation triggers, not as proof of importance. Explicit user questions always trigger their branch. Zero-to-material and material-to-zero payment-routing cells are material even when percentage changes are undefined.

Apply the triggers again after every valid decomposition. A material parent should not stop at a broad segment such as order type, country, or client when one or more of its child drivers also exceed a trigger. Continue until the mechanism is supported, the remaining children are below threshold, the required evidence is unavailable, or the available evidence remains genuinely inconclusive.

When the overall net change is zero or near zero because positive and negative movements offset, judge materiality from absolute movement within one valid axis. Do not combine overlapping country, product, OS, payment, or lifecycle contributions to imply completeness.

## Concentration and anomaly checks

Use top-1/top-5/top-10 user and order shares, repeated-amount clusters, time density, device or IP concentration when permitted, and contradictions across country, currency, language, payment, and client. Hash identifiers in outputs unless raw details are explicitly required and authorized.

Do not label shared IP or device as fraud by itself. Separate observed concentration from risk interpretation.

## Behavioral association

Compare behavior before the outcome. Prefer cohort-standardized rates or matched/stratified comparisons when plan, point balance, activity, or tenure confounds the relationship. Report absolute rates and relative lift. Small high-value cohorts require counts alongside percentages.

## Evidence grades

- Direct fact: source transaction or event count, amount, or timestamp.
- Arithmetic attribution: additive or explicitly decomposed contribution.
- Behavioral association: temporally ordered overlap or statistical association.
- Business hypothesis: plausible mechanism requiring more evidence.
- Experimental evidence: randomized or credible quasi-experimental result.

Use causal verbs only for experimental or otherwise causally identified evidence. Prefer “associated with,” “consistent with,” or “may have contributed” for observational results.
