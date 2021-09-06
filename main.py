import numpy as np
from src.distances import Distance


if __name__ == '__main__':
    points_1_int = np.arange(10)
    points_2_int = np.arange(10, 20)
    points_1_str = 'hamming'
    points_2_str = 'hammyng'  # with typo
    euclidean = Distance.euclidean_distance(points_1_int, points_2_int)
    manhattan = Distance.manhattan_distance(points_1_int, points_2_int)
    hamming = Distance.hamming_distance(points_1_str, points_2_str)
    hamming_percentage = Distance.hamming_distance_percentage(
        points_1_str, points_2_str)

    print(f'Euclidean Distance', euclidean)
    print(f'Manhattan Distance', manhattan)
    print(f'Hamming Distance', hamming)
    print(f'Hamming Distance %', hamming_percentage)
