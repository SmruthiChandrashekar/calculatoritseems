import unittest
from report import generate_report


class TestReport(unittest.TestCase):
    def test_generate_report(self):
        res = generate_report([10, 20, 30])
        self.assertEqual(res["count"], 3)
        self.assertEqual(res["total"], 60)
        self.assertEqual(res["average"], 20.0)


if __name__ == "__main__":
    unittest.main()
