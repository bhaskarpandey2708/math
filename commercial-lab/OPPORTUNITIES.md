# Commercial opportunity shortlist — R&D hypotheses only

| Priority | Family | Potential product | Scope status | Critical obstacle |
|---|---|---|---|---|
| 1 | [124](../lean/docs/124.md) | Three-machine unit-job scheduling API and deadline assurance | Lean note covers polynomial-time minimum-makespan scheduler | The theorem is narrow; implement and benchmark vs OR-Tools |
| 2 | [113](../lean/docs/113.md) | Count feasible assignment configurations, support staffing resilience models | Lean note covers randomized approximation of perfect matching counts | Counting matchings is not the same as finding best assignment |
| 3 | [089](../lean/docs/089.md) | Graph metric embedding R&D for constrained network analytics | Lean note covers planar and bounded-treewidth embedding bounds | Existence theorem is not a fast executable service |
| 4 | [131](../lean/docs/131.md) | Degree-constrained synthetic network sampling | Lean scope covers switch-chain polynomial mixing | Exact uniform sampling claim is outside selected Lean result |
| 5 | [120](../CONTENTS.md) | High-volume staff/asset matching engine | No linked Lean scope for this family | Claimed almost-linear exact matching algorithm still needs verification and implementation |
| 6 | [104](../lean/docs/104.md) | Mean-payoff decision and strategy system | Selected randomized mean-payoff theorem formalized | Does not certify all related games; commercial mapping unproven |
| 7 | [139](../lean/docs/139.md) | Well-conditioned log-concave sampler research | Query-complexity result formalized | Arithmetic/bit costs are not bounded |
| 8 | [142](../CONTENTS.md) | Finite-field factoring computation | No linked Lean scope | Competitive advantage vs existing libraries is unknown |

### Selection criteria

Prefer a theorem with limited, stated assumptions; feasible proof-to-code translation; customer-visible measurable improvement; realistic deployment and limited validation risk. Legal permission is necessary but not sufficient. Verify by domain mathematician, security/legal counsel and representative benchmarks.

### Pilot path

1. Independently reproduce one Lean comparator and check the formal-versus-informal claim correspondence.
2. Build oracle with adversarial test cases, then derive an executable algorithm from the research paper.
3. Benchmark against established OR-Tools CP-SAT or appropriate incumbent, checking correctness, memory, p95 runtime and limits.
4. Find five qualified potential buyers and obtain one real anonymized sample dataset.
5. Charge only after demonstrating credible business value or a clearly contracted research engagement.

### Differentiation

A generic catalogue already has an external alternative in [ProofSearch](https://github.com/ProofSearch). OR-Tools already offers mature scheduling. The proposed moat is verifiable research engineering plus sector-specific constraints, benchmarking, explainability and integrations — not re-selling the same PDFs.

Revenue, sales demand, superior algorithm speed and mathematical correctness are not claimed as established.
