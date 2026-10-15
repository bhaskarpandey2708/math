# Proof-to-product evidence and release gates

Date: 2026-10-15. The fork must be compared against future upstream corrections.

## Levels of evidence

0. Indexed in original catalogue only.
1. Catalogue links to a Lean scope note for a particular result.
2. Formalization independently reproduced with pinned Lean and comparator dependencies; logs retained.
3. Informal proof correspondence and caveats reviewed by outside mathematics expert.
4. Algorithm independently implemented and checked against an exact oracle, test fixtures and adversarial cases.
5. Benchmarked on representative customer workloads, licensed, security-reviewed and customer-valued.

Our automatically indexed results are **at most level 1**. Do not promote a result simply because a Lean link exists.

## Risk register

- Upstream October 7 history withdrew three Hodge-related papers and revised fourteen manuscripts. Dependent results need checking.
- Upstream reports 719 manuscripts, but this index extracted 718 distinct preprint PDF paths; gap remains unresolved.
- Family 104 has selected randomized mean-payoff formalization, not a blanket proof of all titles in that family.
- Family 131 formalizes switch-chain bounds, not the exact uniform sampler.
- Family 139 bounds value/gradient *queries*, not bit/arithmetic runtime.
- Family 124 applies to unit-length jobs on exactly three identical machines; real factory workloads may not fit.
- A formally stated existence or complexity theorem is not production software.

## Family 124 validation

1. Read [Lean 124 scope](../lean/docs/124.md) and [comparator instructions](../lean/ComparatorChallenges/README.md).
2. Pin upstream commit SHA, toolchain and dependency versions; run the ThreeMachine comparator locally and retain logs.
3. Review comparator statement and underlying axioms, hypotheses and proof dependencies.
4. Implement the novel algorithm from the manuscript separately from the exponential reference solver.
5. Benchmark both against Google OR-Tools CP-SAT on realistic precedence DAGs: quality, correctness, elapsed time, memory.
6. Interview buyers; validate their machine/task assumptions and quantify savings relative to current scheduling.

Avoid claiming official OpenAI affiliation or that its unreleased model is included. Apache-2.0 root license imposes notices and conditions; vet third-party components separately.
