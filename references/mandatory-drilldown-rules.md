# Mandatory drilldown rules

Use this reference when a listed branch exceeds a configured trigger or the user explicitly requests it. Thresholds decide how far the analysis must continue; they do not determine report chapters or prove a business cause.

## Trigger rules

An explicitly requested branch always runs. Otherwise, start or continue the applicable drilldown when any trigger is met:

- revenue contribution absolute value reaches `material_absolute_revenue_usd`, or its absolute share of the overall metric change reaches `material_net_change_share`;
- payer, buyer, order, registration, attempt, or other relevant volume changes by at least `volume_change_rate`;
- a funnel conversion rate changes by at least `funnel_rate_change_pp` percentage points;
- a payment channel-currency share changes by at least `routing_share_change_pp` percentage points;
- a previously material routing cell becomes zero, or a new cell becomes material.

When positive and negative movements offset and the net change is zero or near zero, judge the trigger from absolute movement within one valid axis.

## Recursive drilldown protocol

For each triggered branch:

1. Reconcile its population and amount to the relevant parent total.
2. Decompose the parent on one valid additive or explicitly decomposed axis.
3. Identify the affected eligible population and denominator when explaining a count or rate.
4. Reapply the triggers to every child driver; continue into each child that still triggers.
5. Keep arithmetic, lifecycle, product, geography, payment, and client lenses separate when they overlap.
6. Separate direct observations, arithmetic attribution, behavioral association, business hypothesis, and confirmed configuration or pipeline facts.
7. Assign one progress label to the reported finding:
   - `已归因`: contribution, affected population, and supported business mechanism are established;
   - `已下拆，原因待确认`: the numerical driver or cohort is located, but its underlying business reason is not yet supported;
   - `需补充数据`: the next required field, event, log, configuration record, or denominator is unavailable or unreliable;
   - `尚不明确`: available evidence is conflicting or does not identify a dominant explanation.

Finding a broad segment is not a stopping condition when one of its children still exceeds a trigger.

## Paid upgrade decline

Treat an upgrade as a transition from the entitlement or plan immediately before payment to the purchased plan at payment time. Do not infer the historical transition from current plan alone.

Required drilldown:

- reconcile upgrade revenue, successful orders, and unique upgraders;
- decompose revenue into upgrader count, orders per upgrader, and revenue per order;
- split transition paths such as Lite-to-Pro and Pro-to-Pro+, including unknown origin or destination;
- continue into monthly, annual, and other terms, nominal price tiers, actual paid amount, currency, discounts, and refunds when triggered;
- distinguish first upgrade, repeated upgrade-like payment, renewal mislabeled as upgrade, and reactivation where the order model permits;
- when explaining upgrader count, use an eligible pre-upgrade population and report upgrade initiation and success rates when available;
- inspect geography, payment route, OS or version, and acquisition context only after the main transition and arithmetic contributors are known.

Use `已归因` only when the business mechanism behind the material transition, scale, frequency, price, or funnel change is supported. If the analysis only shows that annual or high-value orders disappeared, use `已下拆，原因待确认` until exposure, configuration, campaign, or comparable causal evidence is checked.

## Quota-pack decline

Required drilldown:

- reconcile quota-pack revenue, orders, and unique buyers;
- decompose revenue into buyer count, orders per buyer, and revenue per order;
- preserve both single-order price-tier and per-user accumulated-spend views;
- separate first-time, one-off, and repeat buyers, purchase interval, prior quota-pack history, and month-to-date accumulation;
- define the eligible plan or active-user denominator and calculate quota-pack buyer rate; buyer-only behavior cannot explain buyer-count change;
- continue into plan, price tier, repeat status, or other child drivers when they trigger;
- for a usage mechanism, compare pre-payment point balance, all-model calls, unified points, and depletion speed against a fixed historical window, capped at first target payment;
- run a named-model branch only under the triggers in `SKILL.md`;
- separate product economics or upgrade substitution from observational usage association.

Buyer scale, frequency, and price mix may establish a complete numerical decomposition without establishing the business reason. Use `已下拆，原因待确认` when usage, product exposure, or substitution remains observational.

## Payment currency or routing shift

Required drilldown:

- reconcile a payment-channel by currency matrix for target, direct comparisons, and any confirmed stable baseline;
- keep new, disappearing, zero, and unknown cells visible and identify the change breakpoint at the finest reliable time grain;
- bridge payment initiation, attempt, authorization when available, successful payment, and refund counts and rates;
- continue into payment method, gateway, currency, SKU, nominal and actual price, tax or fee, country, OS, and app version when triggered;
- test data freshness, event mapping, gateway-field changes, and scheduled-job changes before attributing the shift to user behavior;
- distinguish a routing observation from a confirmed configuration change. A currency cell falling to zero is not by itself proof of intentional switching.

Use `已归因` only with direct configuration or pipeline evidence, or a reconciled funnel that identifies where volume moved or failed. If routing logs or configuration history are required but absent, use `需补充数据` and name them.

## Registration-payment funnel decline

Define the registration cohort in business time and preserve cohort maturation. Do not compare an incomplete target cohort with a fully matured comparison cohort without equalizing the observation window.

Required drilldown:

- bridge registrations, payment initiators, payment attempts, first successful payers, and first-payment revenue;
- report registration-to-initiation, initiation-to-attempt, attempt-to-success, and registration-to-first-payment rates when the events exist;
- decompose the change into registration volume, stage conversion, time-to-pay, and first-payment value;
- continue into the first material loss by hour, acquisition source or entry, OS, app version, country or region, payment method, and currency;
- keep event matching coverage, identity loss, unknown source, and late-arriving payment outcomes visible;
- reconcile event-time registration cohorts with transaction-time revenue before using the funnel to explain daily revenue.

Use `已归因` only when the loss is localized to a funnel stage, its material cohort contribution is quantified, and the supported mechanism is clear. If a required stage or acquisition field is unavailable, use `需补充数据` and name the missing field rather than treating the end-to-end rate as a cause.

## Stop conditions

A triggered path may stop only when at least one condition is documented:

- the material contribution, affected population, and business mechanism support `已归因`;
- the numerical driver is complete, all remaining child drivers are below threshold, and any unverified mechanism is labeled `已下拆，原因待确认`;
- a specific missing or unreliable input prevents further work and is labeled `需补充数据`;
- the available evidence is genuinely conflicting or diffuse and is labeled `尚不明确`.

Do not turn thresholds, progress labels, or internal quality checks into standalone management-report chapters. Put the business conclusion first and the progress label beside it.
