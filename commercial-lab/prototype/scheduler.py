"""Exact small-instance reference only; NOT the paper's polynomial algorithm."""
import json
import sys
from collections import deque
from itertools import combinations

def solve(data):
    if data.get("machines") != 3:
        raise ValueError("Exactly 3 identical machines required")
    jobs = data["jobs"]
    if not 1 <= len(jobs) <= 12:
        raise ValueError("Reference baseline is limited to 1..12 unit-length jobs")
    names = [x["id"] for x in jobs]
    if len(set(names)) != len(names):
        raise ValueError("Duplicate job IDs")
    idx = {name: i for i, name in enumerate(names)}
    deps = []
    for job in jobs:
        try:
            deps.append(sum(1 << idx[k] for k in set(job.get("after", []))))
        except KeyError as e:
            raise ValueError("Unknown predecessor") from e
    target = (1 << len(jobs)) - 1
    todo = deque([0])
    parents = {0: None}
    while todo:
        mask = todo.popleft()
        if mask == target:
            slots = []
            while parents[mask]:
                prev, selected = parents[mask]
                slots.append([names[i] for i in selected])
                mask = prev
            slots.reverse()
            result = {"method": "exact_exponential_reference",
                      "optimal_makespan": len(slots),
                      "schedule": [{"time_slot": i, "jobs": slot} for i, slot in enumerate(slots)]}
            if "deadline" in data:
                result["deadline_feasible"] = len(slots) <= data["deadline"]
            return result
        ready = [i for i in range(len(jobs))
                 if not mask & (1 << i) and deps[i] & mask == deps[i]]
        for k in range(1, min(3, len(ready)) + 1):
            for group in combinations(ready, k):
                nxt = mask | sum(1 << i for i in group)
                if nxt not in parents:
                    parents[nxt] = (mask, group)
                    todo.append(nxt)
    raise ValueError("Dependency graph has a cycle")

if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        print(json.dumps(solve(json.load(f)), indent=2))
