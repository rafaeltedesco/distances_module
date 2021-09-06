from typing import List


class Distance:

    def __init__(self, pt1: List[int], pt2: List[int]):
        self.pt1 = pt1
        self.pt2 = pt2

    def euclidean_distance(self):
        distance = sum([((self.pt1[i] - self.pt2[i]) ** 2)
                       for i in range(len(self.pt1))])
        return distance ** 0.5

    def manhattan_distance(self):
        distance = sum([abs((self.pt1[i] - self.pt2[i]))
                       for i in range(len(self.pt1))])
        return distance

    def hamming_distance(self):
        distance = sum([1 if (self.pt1[i] != self.pt2[i])
                       else 0 for i in range(len(self.pt1))])
        return distance
