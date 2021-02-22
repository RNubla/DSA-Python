from typing import List


def threeSum(nums: List[int]):
    # def threeSum(nums: List[int]) -> List[List[int]]:
    result = set()
    # split nums into three list: negative numbers, positive numbers and zeros
    pos, neg, zeros = [], [], []
    for num in nums:
        if num > 0:
            pos.append(num)
        elif num < 0:
            neg.append(num)
        else:
            zeros.append(num)

    # create a seeparete set for negatives and positive for O(1) look-up times
    PosSet, NegSet = set(pos), set(neg)

    # if there is at least 1 zero in the list, add all cases where -numm exist in NegSet and num exist in PosSet
    if zeros:
        for num in PosSet:
            if -1*num in NegSet:
                result.add((-1*num, 0, num))

    # if there are at least 3 zeroes in the list, then also include(0,0,0) = 0
    if len(zeros) >= 3:
        result.add((0, 0, 0))

    # for all pairs of negative numbers i.e (-3,-1) chech to see if their complement (4) exist in the positive
    # number set
    for x in range(len(neg)):
        for y in range(x+1, len(neg)):
            complement = -1*(neg[x] + neg[y])
            if complement in PosSet:
                result.add(tuple(sorted([neg[x], neg[y], complement])))

    # for all pairs of positive numbers i.e (1,1) check to see if their complement (-2) exisit
    # int the negative number set
    for x in range(len(pos)):
        for y in range(x+1, len(pos)):
            complement = -1*(pos[x] + pos[y])
            if complement in NegSet:
                result.add(tuple(sorted([pos[x], pos[y], complement])))

    return result


if __name__ == '__main__':
    # a = [-1, 0, 1, 2, -1, -4]
    a = [1, 1, -2]
    print(threeSum(a))
