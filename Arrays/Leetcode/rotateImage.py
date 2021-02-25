from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
        Do not return anything, modify matrix in-place instead.
        The asterisk in a zip() function converts the elements of the iterable into separate elements. 
        For example: if a = [a1, a2, a3] then zip(*a) equals to ((‘a’, ‘a’, ‘a’), (‘1’, ‘2’, ‘3’)).
        """
    matrix[:] = [a for a in zip(*matrix[::-1])]
    return matrix


if __name__ == '__main__':
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(rotate(m))
