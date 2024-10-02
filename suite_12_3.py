import unittest
import module_12_1
import module_12_2


runnST = unittest.TestSuite()
runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner= unittest.TextTestRunner(verbosity=2)
runner.run(runnST)