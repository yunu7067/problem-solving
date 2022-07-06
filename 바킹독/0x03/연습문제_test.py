import unittest
from 문제 import Solution

class BaakingDog(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            Solution().연습문제2([1, 52, 48], 3),
            1,
        )

    def test2(self):
        self.assertEqual(
            Solution().연습문제2([50, 42], 2),
            0,
        )

    def test3(self):
        self.assertEqual(
            Solution().연습문제2([4, 13, 63, 87], 4),
            1,
        )


if __name__ == "__main__":
    unittest.main()
