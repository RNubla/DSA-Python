from typing import List
from collections import Counter


def singleNumber(nums: List[int]):
    # numDict = dict()

    # for x in range(len(nums)):
    #     numDict[nums[x]] = x
    # print(numDict)
    numDict = Counter(nums)
    for k, v in numDict.items():
        # return v
        if v == 1:
            return k
        # print(v)


if __name__ == '__main__':
    s = [2, 2, 1]
    # s = [4, 1, 2, 1, 2]
    print(singleNumber(s))
