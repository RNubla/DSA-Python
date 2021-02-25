from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # print(matrix[0])
    # if len(matrix) == 1:
    #     return matrix[0]
    # elif len(matrix) == 2 and len(matrix[0]) < 2 and len(matrix[1]) < 2:
    #     return matrix[0] + matrix[1]
    # elif len(matrix) == 2 and len(matrix[0]) > 1 and len(matrix[1]) > 1:
    #     first = matrix[0]
    #     last = matrix[1]
    #     return first + last[::-1]
    # elif len(matrix) > 1 and len(matrix[0]) < 2:
    #     tmp = []
    #     for x in range(len(matrix)):
    #         tmp += matrix[x]
    #     return tmp
    # first = matrix[0]
    # last = matrix[len(matrix)-1]
    # middle = matrix[len(matrix)//2]
    # print(first)
    # print(last[::-1])
    # print(middle[0:-1])

    # print(first + [middle[-1]] + last[::-1] + middle[0:-1])
    return matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1])


if __name__ == '__main__':
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # m = [[1]]
    # m = [[3], [2]]
    # m = [[1, 2], [3, 4]]
    # m = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    # print(*m.pop(0))
    # print([*zip(*m)][::-1])
    print(spiralOrder(m))

    """   
spiral_order([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

= [1, 2, 3] + spiral_order([[6, 9],
                            [5, 8],
                            [4, 7]])

= [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                     [5, 4]])

= [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                              [5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

= [1, 2, 3, 6, 9, 8, 7, 4, 5]

 """
