# Maintenance protocol

Ordinary analysis does not update the skill. Enter maintenance mode only after an explicit request to update it.

## Layers

- Core method: `SKILL.md`, `core-framework.md`, `attribution-methods.md`
- Intake and defaults: `request-form.md`, `business-config.toml`
- Metric definitions: `metric-contracts.md`
- Execution and delivery: `data-modes.md`, `output-modes.md`
- Cases: `references/cases/`
- Validation and history: `scripts/validate_skill.py`, `CHANGELOG.md`

## Update workflow

1. Restate the requested change, reason, affected layer, and likely behavior impact.
2. Propose the smallest file-level change and wait for confirmation.
3. Preserve unrelated rules and cases.
4. Update the skill version:
   - patch: mapping, field, wording, or non-behavioral fix;
   - minor: new compatible branch, metric, or execution mode;
   - major: incompatible core contract or workflow change.
5. Add a concise `CHANGELOG.md` entry.
6. Run `python3 scripts/validate_skill.py` from the skill directory.
7. Replay relevant case invariants. Do not test exact prose.
8. Report what changed, what did not, and which historical outputs might differ.

## Case promotion rule

Do not convert a single historical hypothesis into a universal rule. Promote a case lesson into the core method only when it represents a stable business invariant or repeated failure mode. Otherwise keep it in the case and route to it conditionally.
