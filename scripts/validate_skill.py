#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/business-config.toml",
    "references/request-form.md",
    "references/core-framework.md",
    "references/metric-contracts.md",
    "references/attribution-methods.md",
    "references/data-modes.md",
    "references/output-modes.md",
    "references/maintenance.md",
    "references/cases/lite-quota-upgrade-intent.md",
    "CHANGELOG.md",
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
    "[maintenance]",
    "proposal_before_update = true",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter is missing")
    frontmatter = match.group(1)
    if "name: chatbox-business-fluctuation-diagnosis" not in frontmatter:
        fail("SKILL.md name is incorrect")
    if "description:" not in frontmatter or "TODO" in skill:
        fail("SKILL.md description is missing or unfinished")

    config = (ROOT / "references/business-config.toml").read_text(encoding="utf-8")
    for marker in REQUIRED_CONFIG_MARKERS:
        if marker not in config:
            fail(f"business-config.toml missing marker: {marker}")
    if not re.search(r'^version = "\d+\.\d+\.\d+"$', config, re.MULTILINE):
        fail("business-config.toml version must use semantic versioning")

    request_form = (ROOT / "references/request-form.md").read_text(encoding="utf-8")
    for number in range(1, 9):
        if f"## {number}." not in request_form:
            fail(f"request form missing required field {number}")
    if "Completion gate" not in request_form:
        fail("request form missing completion gate")

    case = (ROOT / "references/cases/lite-quota-upgrade-intent.md").read_text(encoding="utf-8")
    for invariant in ["all models", "post-payment", "non-causal", "$16", "$20"]:
        if invariant.lower() not in case.lower():
            fail(f"case regression invariant missing: {invariant}")

    print(f"OK: {ROOT.name} configuration and regression invariants are valid")


if __name__ == "__main__":
    main()
