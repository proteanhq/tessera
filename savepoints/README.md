# savepoints

Named base states, each a deterministic build recipe.

A savepoint is a build script run against the current domain code and the current Protean, keyed on (domain-code hash, Protean version). The recipe is the source of truth. A file copy of the resulting state is only a cache, invalidated whenever the domain code or the Protean version changes. So an upstream fix re-derives every downstream savepoint correctly the next time it is reached, and teleport stays a cheap file copy in the common case.

The catalogue is capped and governed (roughly eight to fifteen). A new savepoint needs justification; a scenario reuses an existing one where it can. Candidates:

- `empty`: fresh domain, nothing seeded.
- `one-account`: a single account with a short history.
- `running-system`: the engine up, subscriptions live, a steady trickle of activity.
- `week-of-activity`: a week of postings across many accounts.
- `aged-history`: an event store spanning event versions v1 to v4 across simulated time.
- `multi-context-external-bus`: Payments, Ledger, and Notifications wired with the external bus and a stub rail.
- `firehose`: a high-volume stream configured with retention.
- `postgres-stack` / `redis-stack`: full-adapter variants that pay the snapshot cost.

Recipes land here at milestone M3.
