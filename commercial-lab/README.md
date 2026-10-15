# Mathematics-to-Market Lab — independent R&D

This is an independent commercial feasibility study using publicly released OpenAI mathematical manuscripts. It is not an OpenAI product or an endorsement of every theorem.

## Inventory

- [372 family index](data/family-index.csv) — subject, summary, Lean-scope-link status.
- [718 manuscript PDF references](data/manuscript-index.csv) — unique links recognized by our extractor, NOT an exhaustive proof review.
- [Index metadata](data/index-metadata.json) — upstream reports 719 manuscripts; a one-link discrepancy remains.
- [Opportunity shortlist](OPPORTUNITIES.md)
- [Validation protocol](VALIDATION.md)
- [Prototype baseline](prototype/scheduler.py) / [sample jobs](examples/sample_jobs.json) / [tests](tests/test_scheduler.py)

## First experiment — three-machine precedence scheduler

Upstream family [124](../lean/docs/124.md) reports a formalized polynomial-time algorithm for minimizing makespan among unit-length jobs with arbitrary acyclic precedence constraints on exactly three identical machines.

Our prototype is a SEPARATELY IMPLEMENTED exponential-time exact reference solver, capped at 12 jobs, and is **not** an implementation of OpenAI's novel algorithm or evidence of commercial performance. It serves as a correctness oracle for a later implementation.

Run from repository root:

    python3 commercial-lab/prototype/scheduler.py commercial-lab/examples/sample_jobs.json
    python3 -m unittest discover -s commercial-lab/tests -v

The example deliberately has an infeasible deadline: optimal completion in 5 slots versus a requested 4.

### Business hypothesis

Sell B2B scheduling evaluations or an API for precisely scoped three-workstation unit-job workloads, subject to real customer validation. Time-varying durations, nonidentical equipment and changeovers lie outside the theorem. Compare against production competitors such as [OR-Tools CP-SAT](https://github.com/google/or-tools); nobody has demonstrated a competitive advantage here yet.

### Licensing and truthfulness

Root fork license is Apache-2.0: respect license, required attribution and modified-file notices for derived distributions. The license does not authorize OpenAI trademark claims or access to the unreleased frontier model. A Lean link is not a substitute for locally reproducing the formalization and auditing assumptions. Consult [upstream history](../history.md) for withdrawals and revisions.

No confidential pricing, customer data or unverified revenue claims are placed in this public fork.
