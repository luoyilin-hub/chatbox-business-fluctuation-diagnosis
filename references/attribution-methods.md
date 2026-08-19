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
