# scenarios

The story tree as data. One manifest per scenario.

A scenario manifest declares:

- its narrative parent (its slot in the story tree, from trunk to part to chapter),
- one required savepoint (its base state, a name from `savepoints/`),
- the steps that induce a condition (a fault, a normal operation, or a misconfiguration),
- the Protean surfaces to capture (`check`, the diagnostic cluster, the OTel trace, the DLQ, `upgrade-check`, the health endpoints),
- the story (the human-facing narration),
- the tags: which Protean surfaces and domain elements it exercises, for scoped re-runs.

A scenario has six beats: setup, inducement, the reveal, the verdict, the remedy, the confirmation. Adding a scenario is adding a manifest node; because a node declares one required savepoint and is otherwise self-contained, it touches no sibling and forces no downstream rebuild.

Manifests land here as the first parts are built (milestone M5, after the domain freezes at M4).
