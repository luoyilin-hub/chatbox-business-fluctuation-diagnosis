# Core diagnosis framework

## 1. Validate the signal

Before interpreting business behavior, verify:

- data completeness and freshness for target and comparison periods;
- timezone conversion and complete-period boundaries;
- transaction status, test data, duplicated rows, and joins;
- currency conversion, exchange-rate date, and amount units;
- refunds and whether they occurred or were recognized in the target period;
- schema, partition, event, and scheduled-job changes.

If a data issue materially explains the movement, stop business attribution at that point and state the impact.

## 2. Start with an arithmetic identity

For revenue, begin with:

`revenue = paying users × orders per payer × revenue per order`

Also bridge registration, new payer, existing payer, order count, gross revenue, refunds, and net revenue when relevant. For non-revenue targets, define the corresponding numerator, denominator, and population before segmenting.

Attribute the top-level movement with an order-independent method when interactions matter. Do not start with country, OS, or model tables before establishing whether the primary change is scale, frequency, price, or data quality.

## 3. Separate anomalies from routine movement

Check top-user and top-order shares, repeated amounts, short-time clusters, IP/device concentration when authorized, refund concentration, plan/country/currency contradictions, and newly registered high-value purchasers.

Present:

- the complete result;
- material anomaly cohorts and their direct contribution;
- the routine result with those cohorts isolated rather than silently deleted.

An anomaly may be legitimate business. Label it by observed pattern until risk is verified.

## 4. Drill the routine component

Use branches supported by the target metric, generally in this order.

### Lifecycle

- new versus existing payer;
- registration-day payment as an independent label;
- first order versus later order ordinal;
- first purchase, repeat purchase, renewal, upgrade, and reactivation;
- historical purchase frequency and time since previous payment.

### Product and purchase purpose

- plan and product;
- new purchase, renewal, upgrade, quota pack, or other order type;
- monthly, annual, or one-time term;
- single-order price and per-user accumulated payment;
- plan at behavior time and current plan as distinct fields.

### Geography

- mainland versus non-mainland;
- country and business region;
- payer count, order count, revenue, average order value, and contribution to change.

### Payment

- currency, payment method, channel, success rate, and refund rate;
- price tier and exchange-rate effects.

### Client and acquisition context

- payment-initiation client, OS, app version, language, page, or entry source;
- matching coverage and fallback coverage;
- acquisition or registration channel when available.

## 5. Investigate behavioral mechanisms after cohorts are known

For usage-driven purchases, examine pre-payment total usage, unified points, depletion speed, all-model call and point distributions, recent-versus-baseline acceleration, and Agent Mode. Use named-model branches only under the triggers in `SKILL.md`.

Profile and paid-survey data explain the identified cohort. Always show coverage and missingness, and avoid making uncovered users resemble the covered sample.

## 6. Report evidence and decisions

For each material conclusion provide:

- target and comparison values;
- absolute and percentage difference;
- direct contribution to the target movement where additive;
- affected cohort and mechanism;
- evidence grade;
- limitation or alternative explanation;
- business action or next validation step.

Within one segmentation axis, cell contributions may sum to the target difference. Contributions from different overlapping axes must not be added together.
