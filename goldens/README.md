# goldens

Captured Protean output, one golden per scenario.

Each scenario captures the Protean surface it runs as a golden file. When Protean changes, re-running the affected scenarios produces diffs: a diff is accepted as the new golden (the fix improved the surface) or rejected as a regression.

Goldens capture normalized, semantic output: the diagnostic code, its location, and the named fix, with timestamps stripped and collections sorted. The golden asserts meaning, so incidental formatting churn does not produce a diff. Each scenario tags the surfaces it exercises, so a fix to one surface re-runs only the scenarios that touch it.

Goldens land here as scenarios are walked and captured (milestone M5 onward).
