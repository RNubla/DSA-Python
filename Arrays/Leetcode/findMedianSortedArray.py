from typing import List


def findMedianSortedArr(nums1: List[int], nums2: List[int]):

    # merge the two arr
    combined = nums1 + nums2
    combined.sort()
    middle = 0
    if len(combined) < 1:
        return float(middle)
    # middle2 = 0
    if len(combined) % 2 != 0:
        middle = len(combined) // 2
        return float(combined[middle])
    else:
        tmpMiddle = len(combined) // 2
        tmpMiddle2 = tmpMiddle - 1
        middle = float((combined[tmpMiddle] + combined[tmpMiddle2]) / 2)
        return middle

    # print(combined)


if __name__ == '__main__':
    s1 = []
    s2 = []
    # s = [4, 1, 2, 1, 2]
    print(findMedianSortedArr(s1, s2))
