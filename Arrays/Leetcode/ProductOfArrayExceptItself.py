def productExceptSelf(nums):
    p = 1
    n = len(nums)
    output = []

    for i in range(0, n):
        output.append(p)
        p *= nums[i]
    p = 1
    for i in range(n-1, -1, -1):
        output[i] *= p
        p = p * nums[i]

    return output


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    print(productExceptSelf(a))
