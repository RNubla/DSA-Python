from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
        res = []

        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return res

        if k == 2:
            return twoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for comb in kSum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + comb)
        return res

    def twoSum(nums: List[int], target: int) -> List[List[int]]:
        res = []
        lo, hi = 0, len(nums) - 1
        while (lo < hi):
            temp_sum = nums[lo] + nums[hi]
            if temp_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif temp_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1

        return res

    nums.sort()
    return kSum(nums, target, 4)


if __name__ == '__main__':
    a = [2, 1, 0, -1]
    print(fourSum(nums=a, target=2))
