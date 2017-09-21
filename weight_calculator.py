"""This module contains a Lifter class. Based on their 1 Rep Max weight, class will calculate its
suggested weight for a 4x6 workout routine"""

class Lifter:
    """Lifter class contains 1RM for lifts, and calculating their recommended working set weight"""
    def __init__(self, name, benchMax, squatMax, deadliftMax):
        self.__name = name
        self.__bench = benchMax
        self.__squat = squatMax
        self.__deadlift = deadliftMax

    def get_name(self):
        """Returns name"""
        return self.__name

    def get_bench(self):
        """Returns bench 1RM weight"""
        return self.__bench

    def get_squat(self):
        """Returns squat 1RM weight"""
        return self.__squat

    def get_deadlift(self):
        """Returns deadlift 1RM weight"""
        return self.__deadlift

    def set_name(self, name):
        """Sets new name"""
        self.__name = name

    def set_bench(self, bench):
        """Sets new bench"""
        self.__bench = bench

    def set_squat(self, squat):
        """Sets new squat"""
        self.__squat = squat

    def set_deadlift(self, deadlift):
        """Sets new deadlift"""
        self.__deadlift = deadlift

    def working_set_weight(self, one_rep_max):
        """Calculates 4x6 working set based on one_rep_max"""
        rounded_max = self.__round_nearest_fifth(one_rep_max)
        return rounded_max * 0.75


#PRIVATE METHODS

    def __round_nearest_fifth(self, num):
        return int(5 * round(float(num)/5))

if __name__ == '__main__':
    L1 = Lifter("Boy", 200, 300, 400)
    B = L1.get_bench()
    S = L1.get_squat()
    D = L1.get_deadlift()

    BENCH = L1.working_set_weight(B)
    SQUAT = L1.working_set_weight(S)
    DEADLIFT = L1.working_set_weight(D)
    print("Working set for bench: {}, squat: {}, deadlift: {}".format(BENCH, SQUAT, DEADLIFT))
