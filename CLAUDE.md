# Tessera development guide

Tessera is a scenario library over a purpose-built finance domain, built to walk every esoteric and non-DDD surface of [Protean](https://github.com/proteanhq/protean). This file is the guide for building *in* this repository. The README is the outward-facing description.

This repository is the execution surface. The strategy, the design of record, and the initiative tracking are maintained separately and privately.

## The shape of the thing

Three layers, kept deliberately separate:

- **The finance domain** (`src/`). A wholesome, durable neobank ledger core designed backward from feature coverage: every esoteric Protean surface has a natural home in the model. The kernel is designed once, built to green, then frozen. After the freeze, kernel changes are versioned and logged; additive growth (new scenarios, new read models, branch-only elements) stays free.
- **The scenarios** (`scenarios/`, `savepoints/`, `goldens/`). Each scenario is a data manifest: a narrative parent, one required savepoint for its state, the steps that induce a condition, the Protean surfaces to capture, and the story. Scenarios break the domain on branches to walk faults; the kernel on the trunk stays clean.
- **The tool** (`cx`). A thin command tool over the domain and the scenarios that orchestrates git, data, the Protean CLI, and the capture layer.

## The domain: contexts

One Protean domain, eight bounded contexts, plus a second small domain.

| Context | Role | Persistence |
| --- | --- | --- |
| `ledger` | Event-sourced double-entry core; the source of truth | Event-sourced |
| `accounts` | Customer accounts, holds, status | Relational |
| `payments` | Transfers and settlement as sagas; idempotency, outbox | Relational |
| `cards` | Authorizations, clearing, disputes | Relational |
| `fraud` | Monitoring and priority-lane freezes | Relational |
| `compliance` | Onboarding, KYC, sanctions; circuit breaker, ACL subscriber | Relational |
| `reporting` | Balances, statements, dashboards; projections, temporal queries | Relational read models |
| `notifications` | ACL subscriber publishing CloudEvents to the external bus | No aggregate |
| `insights` | A separate Protean domain; cross-domain read model over the bus | Relational |
| `shared` | Shared kernel: value objects (Money) and cross-context helpers | n/a |

Ledger is the event-sourced core the rest consume. `JournalEntry` guards debit-equals-credit; each `LedgerAccount` keeps its own event stream. One high-volume event, `AccountPosted`, carries a v1-to-v4 upcaster chain so the aged-history state is real. `CustomerAccountOpened` carries a deprecation subject.

Each context becomes a Protean domain at build time (its own `domain.py` and `domain.toml`), following the sibling reference app [shopstream](https://github.com/proteanhq/shopstream). At the current scaffold stage the context packages are placeholders; the kernel is implemented at milestone M2.

## Milestones

The domain is built and frozen before scenarios pile on it, so it does not move under the library.

- **M0**: the feature-to-requirement matrix (the coverage spec). Complete.
- **M1**: the context map and kernel model. Complete.
- **M2**: kernel implemented; `protean check` and `protean verify` run clean across all contexts; the happy-path trunk runs. The domain exists and is green. **In progress.**
- **M3**: the savepoint catalogue built as recipes; the `cx` skeleton (`goto`, `where`, `reset`) works; the walk-equals-jump self-test passes on a sample.
- **M4**: the domain frozen and versioned; the changelog opens. The gate before any scenario part is built.

## Conventions

- **Events are versioned from day one.** Every event is v1 at birth. Two subjects are designed to evolve (`AccountPosted`, `CustomerAccountOpened`) so the upcaster and deprecation scenarios have real history.
- **Savepoints are recipes, their file copies are caches.** A savepoint is a deterministic build script run against the current domain code and the current Protean, keyed on (domain-code hash, Protean version). A file copy is only a cache, invalidated when either changes. An upstream fix re-derives every downstream savepoint correctly on next reach.
- **Goldens assert meaning.** Capture normalized, semantic output: the diagnostic code, its location, the named fix, with timestamps stripped and collections sorted, so incidental formatting churn does not produce a diff.
- **Walk equals jump.** Jumping directly to scenario N must produce the exact state that walking to N from the top would. This is the correctness contract; a self-test asserts it on a sample.
- **Kernel changes are logged after the freeze.** Before M4 the kernel moves freely. After M4, a kernel change is a versioned, logged event scoped to a re-run of the affected scenarios.

## Dev setup

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/). SQLite is the default provider, so the base savepoints are file copies with no Docker. Scenarios that exercise Postgres, message-db, or Redis declare that need and pay the snapshot cost.

```bash
uv sync                 # install, pulling protean from main
uv run cx --help        # the scenario tool (skeleton until E2)
uv run protean check    # once the domain is implemented (M2)
uv run pytest           # tests
```

## The cx tool verbs

Planned surface (built in initiative epic E2, after the domain reaches M2):

- `cx list` / `cx map`: the library, grouped by feature and part, each scenario's savepoint and story, with a mark for what has been seen.
- `cx goto <scenario>`: rebuild to that scenario's state, land, print the "what is interesting here" card.
- `cx play <scenario>`: run the full beat sequence narrated, pausing for the verdict.
- `cx walk --from <scenario>`: the guided tour onward from a point.
- `cx maraud [<scenario>]`: goto, then drop into a live session with the interesting surfaces one keystroke away.
- `cx snapshot` / `cx restore`: freeze and thaw the live state so roaming never costs a rebuild.
- `cx where` / `cx reset`.
