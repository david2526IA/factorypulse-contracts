"""Schema registry and strict validation API."""

from __future__ import annotations

import json
from importlib.resources import files

from jsonschema import Draft202012Validator, FormatChecker


def available_contracts() -> list[str]:
    return sorted(path.name.removesuffix(".json") for path in files("factorypulse_contracts.schemas").iterdir() if path.suffix == ".json")


def load_contract(name: str) -> dict[str, object]:
    path = files("factorypulse_contracts.schemas").joinpath(f"{name}.json")
    if not path.is_file():
        raise ValueError(f"Unknown contract '{name}'. Available: {', '.join(available_contracts())}")
    return json.loads(path.read_text(encoding="utf-8"))


def validate_event(name: str, event: dict[str, object]) -> None:
    """Raise a JSON Schema validation error if an event violates the contract."""
    Draft202012Validator(load_contract(name), format_checker=FormatChecker()).validate(event)
