import unittest
import Module_12_2, Module_12_1

run_tour_TS = unittest.TestSuite()
run_tour_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.TournamentTest))
run_tour_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_1.RunnerTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tour_TS)
