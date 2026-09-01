# Tessera

A navigable library of runnable scenarios over a purpose-built finance (ledger) domain, built to walk every esoteric and non-DDD surface of [Protean](https://github.com/proteanhq/protean): the async runtime, event sourcing, the diagnostics compiler, observability, persistence, and upgrades.

Each scenario puts the domain in a known state, induces a condition (a fault, a normal operation, or a misconfiguration), runs the relevant Protean surface (`check`, the diagnostic cluster, the OTel trace tree, the DLQ, `upgrade-check`, the health endpoints), and records what it revealed. The scenarios form a story tree: a trunk narrative (a neobank's life, start to maturity) with feature parts and chapters down to individual runnable scenarios. A command-line tool, `cx`, jumps to any point, lands in that state, and lets you roam.

Tessera is the singular of *tesserae*, the small tiles of a mosaic: each scenario stands alone and also forms part of one picture. A jump to any scenario lands in the exact state a full walk would have built, the way a tile fits its slot.

## Status

Early construction. The domain design is complete; the build to a green, running domain (milestone M2) is in progress. Nothing is runnable yet.

## The domain

A neobank ledger core across eight bounded contexts:

| Context | Role |
| --- | --- |
| Ledger | The event-sourced double-entry core. The source of truth the rest consume. |
| Accounts | Customer accounts, holds, status. |
| Payments | Transfers and settlement, orchestrated as sagas. |
| Cards | Authorizations, clearing, disputes. |
| Fraud | Monitoring and freezes. |
| Compliance | Onboarding, KYC, sanctions, calling an external provider. |
| Reporting | Read models: balances, statements, dashboards, point-in-time queries. |
| Notifications | Outbound events to external systems over the bus. |

A small second Protean domain, **Insights**, subscribes to the external-bus events and builds a cross-domain read model. It exercises the multi-domain surface without bloating the kernel.

## Layout

- `src/`: the finance domain, one package per bounded context, plus `shared` and `insights`.
- `cx/`: the scenario tool (`cx list`, `cx goto`, `cx play`, `cx walk`, `cx maraud`, ...).
- `scenarios/`: the story tree as data, one manifest per scenario.
- `savepoints/`: named base states, each a deterministic build recipe.
- `goldens/`: captured Protean output per scenario, reviewed as diffs.
- `tests/`: the walk-equals-jump self-test and unit coverage.

## Getting started

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run cx --help
```

Tessera runs against the current Protean line, pulled from `main`.

## License

Apache-2.0. See [LICENSE](LICENSE).
