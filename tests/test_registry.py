import json
from pathlib import Path

import pytest
from jsonschema import ValidationError

from factorypulse_contracts.registry import available_contracts, validate_event


def test_all_expected_contracts_are_registered() -> None:
    assert available_contracts() == ["anomaly.v1", "data-quality.v1", "inspection.v1", "telemetry.v1"]


def test_valid_telemetry_example_passes() -> None:
    event = json.loads(Path("examples/telemetry.valid.json").read_text(encoding="utf-8"))
    validate_event("telemetry.v1", event)


def test_invalid_telemetry_example_fails() -> None:
    event = json.loads(Path("examples/telemetry.invalid.json").read_text(encoding="utf-8"))
    with pytest.raises(ValidationError):
        validate_event("telemetry.v1", event)


def test_unknown_contract_has_actionable_error() -> None:
    with pytest.raises(ValueError, match="Unknown contract"):
        validate_event("does-not-exist", {})
