# FactoryPulse Contracts

> Versioned, machine-validatable event contracts for the FactoryPulse reference platform.

[![Contract CI](https://github.com/david2526IA/factorypulse-contracts/actions/workflows/ci.yml/badge.svg)](https://github.com/david2526IA/factorypulse-contracts/actions/workflows/ci.yml)
[![JSON Schema](https://img.shields.io/badge/JSON%20Schema-Draft%202020--12-36A4E8)](https://json-schema.org/)
[![License](https://img.shields.io/badge/License-MIT-2563EB.svg)](LICENSE)

FactoryPulse is a future multi-repository industrial-operations platform. This repository is its shared language: it defines exactly what a telemetry producer, anomaly detector, vision service or data-quality pipeline can publish and what downstream systems may trust.

## Why contracts come first

Without a contract, independently deployed services eventually disagree on field names, units, timestamps and error handling. A schema registry makes those assumptions explicit, testable and versioned before integrations become expensive to repair.

## Available contracts

| Contract | Event type | Producer example | Consumer example |
| --- | --- | --- | --- |
| `telemetry.v1` | `factorypulse.telemetry` | Sensor gateway / simulator | Lakehouse, anomaly detector |
| `anomaly.v1` | `factorypulse.anomaly` | PredictivePlant adapter | Dashboard, alerting service |
| `inspection.v1` | `factorypulse.inspection` | VisionInspect adapter | Quality workflow, dashboard |
| `data-quality.v1` | `factorypulse.data_quality` | Lakehouse pipeline | Observability, dashboard |

## Quick start

```bash
git clone https://github.com/david2526IA/factorypulse-contracts.git
cd factorypulse-contracts
python -m venv .venv
```

Activate the environment, then:

```bash
pip install -e ".[dev]"
factorypulse-contracts list
factorypulse-contracts validate telemetry.v1 examples/telemetry.valid.json
pytest -q
```

The invalid example fails deliberately:

```bash
factorypulse-contracts validate telemetry.v1 examples/telemetry.invalid.json
```

## Python integration

```python
from factorypulse_contracts import validate_event

validate_event("telemetry.v1", event)
```

## Contract lifecycle

1. Propose the event purpose, producer and consumer.
2. Add/update the versioned JSON Schema.
3. Add valid and invalid fixtures.
4. Run CI before publishing a producer or consumer change.
5. Follow the [compatibility policy](docs/compatibility.md).

## Next integrations

- `factorypulse-ingestion` will publish `telemetry.v1` events.
- `factorypulse-intelligence` will consume telemetry and publish `anomaly.v1` / `inspection.v1`.
- `factorypulse-lakehouse` will validate events and publish `data-quality.v1` run results.

## License

MIT © 2026 David
