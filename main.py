import numpy as np
from src.distances import Distance


if __name__ == '__main__':
    points_1 = np.arange(10)
    points_2 = np.arange(10, 20)
    distance = Distance(points_1, points_2)
    euclidean = distance.euclidean_distance()
    manhattan = distance.manhattan_distance()
    hamming = distance.hamming_distance()

    print(f'Euclidean Distance', euclidean)
    print(f'Manhattan Distance', manhattan)
    print(f'Hamming Distance', hamming)
