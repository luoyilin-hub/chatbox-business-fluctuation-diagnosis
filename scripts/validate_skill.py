#!/usr/bin/env python3
from __future__ import annotations

import ast
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/business-config.toml",
    "references/request-form.md",
    "references/core-framework.md",
    "references/mandatory-drilldown-rules.md",
    "references/metric-contracts.md",
    "references/attribution-methods.md",
    "references/data-modes.md",
    "references/output-modes.md",
    "references/maintenance.md",
    "references/cases/lite-quota-upgrade-intent.md",
    "references/cases/daily-multi-branch-drilldown.md",
    "CHANGELOG.md",
]

LEGACY_FILES = [
    "references/diagnostic-closure-gates.md",
    "references/cases/daily-multi-branch-closure.md",
]

REQUIRED_CONFIG_MARKERS = [
    "[skill]",
    'version = "',
    "[defaults]",
    'timezone = "Asia/Shanghai"',
    'stable_baseline_statistic = "mean"',
    "[payer_lifecycle]",
    "new_payer = ",
    "[plan_contract]",
    "historical_attribution = ",
    "[point_contract]",
    "pro_multiplier = 8",
    "[model_branch]",
    'default = "all_models"',
    "[mandatory_drilldown]",
    "material_absolute_revenue_usd = 300",
    "recursive = true",
    "explicit_user_branch_always = true",
    "[maintenance]",
    "proposal_before_update = true",
]

PROGRESS_LABELS = {
    "已归因",
    "已下拆，原因待确认",
    "需补充数据",
    "尚不明确",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def section(markdown: str, number: int) -> str:
    match = re.search(
        rf"^## {number}\. .*?(?=^## \d+\.|^## Completion gate|\Z)",
        markdown,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        fail(f"request form missing field {number}")
    return match.group(0)


def config_section(config: str, name: str) -> str:
    match = re.search(
        rf"^\[{re.escape(name)}\]\s*$\n(.*?)(?=^\[|\Z)",
        config,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        fail(f"business-config.toml missing section: {name}")
    return match.group(1)


def config_value(config: str, section_name: str, key: str):
    body = config_section(config, section_name)
    match = re.search(rf"^{re.escape(key)}\s*=\s*(.+?)\s*$", body, re.MULTILINE)
    if not match:
        fail(f"business-config.toml missing value: {section_name}.{key}")
    raw = match.group(1)
    if raw == "true":
        return True
    if raw == "false":
        return False
    try:
        return ast.literal_eval(raw)
    except (SyntaxError, ValueError):
        fail(f"business-config.toml has unsupported value: {section_name}.{key}={raw!r}")


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))
    legacy = [path for path in LEGACY_FILES if (ROOT / path).exists()]
    if legacy:
        fail("legacy drilldown files still present: " + ", ".join(legacy))

    skill = read("SKILL.md")
    match = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter is missing")
    frontmatter = match.group(1)
    if "name: chatbox-business-fluctuation-diagnosis" not in frontmatter:
        fail("SKILL.md name is incorrect")
    if "description:" not in frontmatter or "TODO" in skill:
        fail("SKILL.md description is missing or unfinished")
    for routed_reference in [
        "references/request-form.md",
        "references/mandatory-drilldown-rules.md",
        "references/cases/daily-multi-branch-drilldown.md",
    ]:
        if routed_reference not in skill:
            fail(f"SKILL.md does not route to {routed_reference}")

    config = read("references/business-config.toml")
    for marker in REQUIRED_CONFIG_MARKERS:
        if marker not in config:
            fail(f"business-config.toml missing marker: {marker}")
    version = config_value(config, "skill", "version")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail("business-config.toml version must use semantic versioning")
    changelog = read("CHANGELOG.md")
    if not re.search(rf"^## {re.escape(version)}\s+—\s+\d{{4}}-\d{{2}}-\d{{2}}$", changelog, re.MULTILINE):
        fail("CHANGELOG.md does not contain the configured version and date")

    numeric_contracts = {
        "material_absolute_revenue_usd": (0, None),
        "material_net_change_share": (0, 1),
        "volume_change_rate": (0, 1),
        "funnel_rate_change_pp": (0, 100),
        "routing_share_change_pp": (0, 100),
    }
    for key, (lower, upper) in numeric_contracts.items():
        value = config_value(config, "mandatory_drilldown", key)
        if not isinstance(value, (int, float)) or value <= lower or (upper is not None and value > upper):
            fail(f"invalid mandatory_drilldown value: {key}={value!r}")
    if config_value(config, "mandatory_drilldown", "recursive") is not True:
        fail("mandatory drilldown must be recursive")
    if config_value(config, "mandatory_drilldown", "explicit_user_branch_always") is not True:
        fail("explicitly requested branches must always run")
    if set(config_value(config, "mandatory_drilldown", "statuses")) != PROGRESS_LABELS:
        fail("mandatory_drilldown progress labels are incomplete")
    if "minimum_closed_absolute_movement_share" in config:
        fail("legacy aggregate completion threshold is still configured")

    request_form = read("references/request-form.md")
    for number in range(1, 10):
        field = section(request_form, number)
        if number <= 8 and len(re.findall(r"^- [A-Z]\. ", field, re.MULTILINE)) < 2:
            fail(f"request form field {number} does not preserve its lettered options")
    for contract in ["Rendering contract", "Current answer", "Answer source", "Field status", "Execution status"]:
        if contract not in request_form:
            fail(f"request form missing full-render contract: {contract}")
    if "explicitly confirmed before execution" not in request_form:
        fail("request form does not enforce explicit confirmation")

    drilldown_rules = read("references/mandatory-drilldown-rules.md")
    for branch in [
        "Trigger rules",
        "Recursive drilldown protocol",
        "Paid upgrade decline",
        "Quota-pack decline",
        "Payment currency or routing shift",
        "Registration-payment funnel decline",
        "Stop conditions",
    ]:
        if f"## {branch}" not in drilldown_rules:
            fail(f"mandatory drilldown rules missing branch: {branch}")
    for label in PROGRESS_LABELS:
        if f"`{label}`" not in drilldown_rules:
            fail(f"mandatory drilldown rules missing progress label: {label}")
    for behavior in ["Reapply the triggers", "remaining child drivers are below threshold", "explicitly requested branch always runs"]:
        if behavior.lower() not in drilldown_rules.lower():
            fail(f"mandatory drilldown behavior missing: {behavior}")

    output_modes = read("references/output-modes.md")
    for heading in [
        "结论摘要",
        "核心指标对比",
        "收入变化来源",
        "重点变化项下钻",
        "其他关键结构检查",
        "待确认原因与数据需求",
        "业务建议",
        "附录：统计口径、数据质量、截止时间与产物",
    ]:
        if f"`{heading}`" not in output_modes:
            fail(f"output modes missing business report section: {heading}")
    for label in PROGRESS_LABELS:
        if f"`{label}`" not in output_modes:
            fail(f"output modes missing progress label: {label}")
    for forbidden_heading in ["结论关闭状态", "部分关闭", "partially_closed"]:
        if forbidden_heading in output_modes:
            fail(f"output modes still expose workflow jargon: {forbidden_heading}")
    if "do not create a separate status section" not in output_modes.lower():
        fail("output modes do not keep progress tracking secondary")

    core = read("references/core-framework.md")
    attribution = read("references/attribution-methods.md")
    if "reapply the thresholds" not in core.lower() or "apply the triggers again" not in attribution.lower():
        fail("recursive materiality is not enforced across the core method")

    case = read("references/cases/lite-quota-upgrade-intent.md")
    for invariant in ["all models", "post-payment", "non-causal", "$16", "$20"]:
        if invariant.lower() not in case.lower():
            fail(f"case regression invariant missing: {invariant}")

    multi_branch_case = read("references/cases/daily-multi-branch-drilldown.md")
    for branch in [
        "Paid upgrade decline",
        "Quota-pack decline",
        "Payment currency or routing shift",
        "Registration-payment funnel decline",
    ]:
        if f"### {branch}" not in multi_branch_case:
            fail(f"multi-branch regression case missing: {branch}")
    for invariant in [
        "complete intake",
        "recursively",
        "selected buyers",
        "routing observation",
        "cohort maturation",
        "valid stop condition",
        "business conclusion",
    ]:
        if invariant.lower() not in multi_branch_case.lower():
            fail(f"multi-branch regression invariant missing: {invariant}")

    print(f"OK: {ROOT.name} v{version} recursive drilldown and reporting invariants are valid")


if __name__ == "__main__":
    main()
