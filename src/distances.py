from typing import Union, List, TypeVar

TNum = TypeVar('TNum', int, float)
TList = TypeVar('TList', int, float, str)


class Distance:

    @staticmethod
    def euclidean_distance(pt1: List[TNum], pt2: List[TNum]):
        distance = sum([((pt1[i] - pt2[i]) ** 2)
                       for i in range(len(pt1))])
        return distance ** 0.5

    @staticmethod
    def manhattan_distance(pt1: List[TNum], pt2: List[TNum]):
        distance = sum([abs((pt1[i] - pt2[i]))
                       for i in range(len(pt1))])
        return distance

    @staticmethod
    def hamming_distance(pt1: List[TList], pt2: List[TList]):
        distance = sum([1 if (pt1[i] != pt2[i])
                       else 0 for i in range(len(pt1))])
        return distance
