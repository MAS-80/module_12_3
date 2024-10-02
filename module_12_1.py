import unittest
import runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        n1 = runner.Runner('Vasia')
        for i in range(10):
            n1.walk()
        self.assertEqual(n1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        n1 = runner.Runner('Vasia')
        for i in range(10):
            n1.run()
        self.assertEqual(n1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        n1 = runner.Runner('Vasia')
        n2 = runner.Runner('Petia')
        for i in range(10):
            n1.walk()
            n2.run()
        self.assertNotEqual(n1.distance, n2.distance)


if __name__ == '__main__':
    unittest.main()