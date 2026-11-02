# Compatibility policy

FactoryPulse contracts use `MAJOR.MINOR` schema versions.

- Additive optional fields increment **MINOR** and must preserve existing behaviour.
- Removing fields, changing a type, narrowing an enum, or changing semantics increments **MAJOR**.
- Producers must set `event_type` and `schema_version` on every event.
- Consumers must reject unknown major versions explicitly and record the failure.
- A contract change requires at least one valid example and one rejection test.

The v1 schemas intentionally set `additionalProperties: false`. This prevents accidental, undocumented fields from silently entering cross-service data. Add a field through the normal schema-change process instead.
