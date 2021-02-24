from typing import List


def permute(nums: List[int]):
    ans = []
    helper(nums, [], ans)
    return ans


def helper(nums, temp, ans):
    if len(nums) == 0:
        ans.append(temp)
        return
    for i in range(len(nums)):
        helper(nums[:i]+nums[i+1:], temp+[nums[i]], ans)


if __name__ == '__main__':
    s1 = [2, 3, 5]

    print(permute(s1))
