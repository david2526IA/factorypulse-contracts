from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import ValidationError

from .registry import available_contracts, validate_event


def main() -> None:
    parser = argparse.ArgumentParser(prog="factorypulse-contracts")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="list registered contracts")
    check = commands.add_parser("validate", help="validate an event JSON file")
    check.add_argument("contract", choices=available_contracts())
    check.add_argument("event", type=Path)
    args = parser.parse_args()
    if args.command == "list":
        print("\n".join(available_contracts()))
        return
    event = json.loads(args.event.read_text(encoding="utf-8"))
    try:
        validate_event(args.contract, event)
    except ValidationError as error:
        raise SystemExit(f"Invalid {args.contract} event: {error.message}") from error
    print(f"Valid {args.contract} event: {args.event}")


if __name__ == "__main__":
    main()
