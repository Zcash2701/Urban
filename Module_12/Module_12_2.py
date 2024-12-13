import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}
        #return cls.all_result

    @classmethod
    def tearDownClass(cls):
        for keys, value in cls.all_result.items():
            print(value)


    def setUp(self):
        self.runner_Yuen = Runner('Yuen', 10)
        self.runner_Andru = Runner('Andru', 9)
        self.runner_Nick = Runner('Nick', 3)


    def test_Yuen_vs_Nick(self):
        race = Tournament(90, self.runner_Yuen, self.runner_Nick)
        result = race.start()
        self.all_result['1'] = {key: value.name for key,value in result.items()}
        self.assertTrue(result[max(result.keys())] == 'Nick')

    def test_Andru_vs_Nick(self):
        race = Tournament(90, self.runner_Nick, self.runner_Andru)
        result = race.start()
        self.all_result['2'] = {key: value.name for key,value in result.items()}
        self.assertTrue(result[max(result.keys())] == 'Nick')

    def test_all_runner(self):
        race = Tournament(90, self.runner_Yuen, self.runner_Andru, self.runner_Nick)
        result = race.start()
        self.all_result['3'] = {key: value.name for key,value in result.items()}
        print(self.assertTrue(result[max(result.keys())] == 'Nick'))




if __name__ == '__main__':
    unittest.main()