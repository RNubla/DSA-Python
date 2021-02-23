from typing import List


def twoSums(nums: List[int], target: int) -> List[int]:
    if len(nums) < 2 or not nums:
        return []
    seen = {}

    for i in range(len(nums)):
        neededNums = target - nums[i]
        if neededNums in seen:
            return[i, seen[neededNums]]
        else:
            seen[nums[i]] = i


def twoSumSorted(nums: List[int], target: int) -> List[int]:
    if len(nums) < 2 or not nums:
        return []

    nums.sort()

    pointerL = 0
    pointerR = len(nums)-1

    while pointerL < pointerR:
        tempSum = nums[pointerL] + nums[pointerR]
        if tempSum == target:
            return [pointerL, pointerR]
        elif tempSum < target:
            pointerL += 1
        else:
            pointerR -= 1


if __name__ == '__main__':
    a = [3, 2, 4]
    # a = [2, 7, 11, 15]
    target = 6
    print(twoSumSorted(nums=a, target=target))
    print(twoSums(nums=a, target=target))
