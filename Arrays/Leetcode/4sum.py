from typing import List

# def fourSum(nums: List[int], target: int):
#     result = set()

#     pos, neg, zeros = [], [], []

#     for num in nums:
#         if num > 0:
#             pos.append(num)
#         elif num < 0:
#             neg.append(num)
#         else:
#             zeros.append(num)

#     PosSet, NegSet, = set(pos), set(neg)

#     if zeros:
#         for num in PosSet:
#             if -1*num in NegSet:
#                 result.add((-1*num, 0, 0, num))

#     if len(zeros) >= 4 and target == 0:
#         result.add((0, 0, 0, 0))
#     elif len(zeros) >= 4 and target != 0:
#         result

#     for x in range(len(neg)):
#         for y in range(x+1, len(neg)):
#             complement = -1*(neg[x] + neg[y])
#             if complement in PosSet:
#                 result.add(
#                     tuple(sorted([neg[x], neg[y], complement, -1*complement])))

#     for x in range(len(pos)):
#         for y in range(x+1, len(pos)):
#             complement = -1*(pos[x] + pos[y])
#             if complement in NegSet:
#                 result.add(
#                     tuple(sorted([pos[x], pos[y], complement, -1*complement])))

#     for x in range(len(pos)):
#         for y in range(len(neg)):
#             complement = -1*(pos[x] + pos[y])
#             if complement in NegSet:
#                 result.add(
#                     tuple(sorted([pos[x], pos[y], complement, -1*complement])))

#     return result


def threeSum(nums, target):
    res = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j, k = i+1, len(nums)-1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == target:
                res.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1
                k -= 1
            elif total < target:
                j += 1
            else:
                k -= 1
    return res


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        rest = threeSum(nums[i+1:], target-nums[i])
        res += [[nums[i]]+r for r in rest]
    return res


if __name__ == '__main__':
    # a = [1, 0, -1, 0, -2, 2]
    # a = [0, 0, 0, 0]
    a = [2, 1, 0, -1]
    print(fourSum(a, 2))
