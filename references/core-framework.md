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

Attribute the overall metric movement with an order-independent method when interactions matter. Do not start with country, OS, or model tables before establishing whether the primary change is scale, frequency, price, or data quality.

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

## 6. Continue every material drilldown

Use the thresholds in `business-config.toml` as recursive investigation triggers. A user-requested branch always runs regardless of size. For paid upgrades, quota packs, payment currency or routing, and the registration-payment funnel, follow `mandatory-drilldown-rules.md`.

After decomposing a material parent into one valid additive or explicitly decomposed axis, reapply the thresholds to its child drivers. Continue into every triggered child until one of the documented stop conditions is met. A segment moving in the same direction as the target is only a first-level observation; it is not a sufficient explanation.

Assign one business-readable progress label to each reported material finding:

- `已归因`: the contribution, affected population, and supported business mechanism are established;
- `已下拆，原因待确认`: the numerical driver or cohort is located, but the underlying reason still needs verification;
- `需补充数据`: the next required field, log, event, or denominator is unavailable or unreliable;
- `尚不明确`: available evidence is conflicting or does not identify a dominant explanation.

Do not add contributions from overlapping country, product, OS, payment, or lifecycle views. Thresholds control analytical depth; they must not become report chapter names or management-facing coverage scores.

## 7. Report evidence and decisions

For each material conclusion provide:

- target and comparison values;
- absolute and percentage difference;
- direct contribution to the target movement where additive;
- affected cohort and mechanism;
- evidence grade;
- limitation or alternative explanation;
- business action or next validation step.

Within one segmentation axis, cell contributions may sum to the target difference. Contributions from different overlapping axes must not be added together.
