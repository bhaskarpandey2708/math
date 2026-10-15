"""Tests for the independent exponential-time baseline."""
import unittest
import importlib.util
from pathlib import Path
_path = Path(__file__).resolve().parents[1] / "prototype" / "scheduler.py"
_spec = importlib.util.spec_from_file_location("math_scheduler", _path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
solve = _module.solve

class SchedulerTests(unittest.TestCase):
    def test_parallel(self):
        x = {"machines": 3, "jobs": [{"id": str(i)} for i in range(7)]}
        self.assertEqual(solve(x)["optimal_makespan"], 3)
    def test_precedence(self):
        x = {"machines": 3, "jobs": [{"id":"a"}, {"id":"b","after":["a"]}]}
        self.assertEqual(solve(x)["optimal_makespan"], 2)
    def test_cycle(self):
        x = {"machines": 3, "jobs": [{"id":"a","after":["b"]},
                                      {"id":"b","after":["a"]}]}
        with self.assertRaises(ValueError):
            solve(x)
    def test_deadline(self):
        x = {"machines": 3, "deadline": 0, "jobs":[{"id":"a"}]}
        self.assertFalse(solve(x)["deadline_feasible"])
    def test_wrong_machines(self):
        with self.assertRaises(ValueError):
            solve({"machines":2,"jobs":[{"id":"a"}]})

if __name__ == "__main__":
    unittest.main()
