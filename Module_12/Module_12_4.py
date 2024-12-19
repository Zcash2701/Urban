import logging
import unittest

class Runner:
    def __init__(self, name, speed=5):

        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')

        self.distance = 0

        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')



    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = True

    def test_walk(self):
        name = 'Илья'
        speed = -6

        try:
            walker = Runner(name, speed)
            for _ in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info('The runner successfully ran the distance')

        except TypeError as te:
            logging.error(f'Имя может быть только строкой, передано {type(name).__name__}', exc_info=te)
        except ValueError as ve:
            logging.error(f'Скорость не может быть отрицательной, сейчас {speed}', exc_info=ve)




    def test_run(self):
        name = 123
        speed = 10

        try:
            runner = Runner(name, speed)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('The runner successfully ran the distance')
        except TypeError as te:
            logging.error(f'Имя может быть только строкой, передано {type(name).__name__}', exc_info=te)
        except ValueError as ve:
            logging.error(f'Скорость не может быть отрицательной, сейчас {speed}', exc_info=ve)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walker = Runner('Walk')
        runner = Runner('Run')
        for _ in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)






logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format='%(asctime)s | %(levelname)s | %(message)s')

run_tour_TS = unittest.TestSuite()
run_tour_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tour_TS)