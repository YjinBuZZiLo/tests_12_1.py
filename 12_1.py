import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk1 = runner.Runner('First')
        for i in range(10):
            walk1.walk()
        self.assertEqual(walk1.distance, 50)

    def test_run(self):
        walk2 = runner.Runner('Second')
        for j in range(10):
            walk2.run()
        self.assertEqual(walk2.distance, 100)

    def test_challenge(self):
        walk3 = runner.Runner('Third')
        walk4 = runner.Runner('Fourth')
        for k in range(10):
            walk3.run()
            walk4.walk()
        self.assertNotEqual(walk3.distance, walk4.distance)


if __name__ == '__main__':
    unittest.main()