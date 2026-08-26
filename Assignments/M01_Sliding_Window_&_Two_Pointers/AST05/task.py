from typing import List

def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    # Product of elements on the left
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]

    # Product of elements on the right
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]

    return res


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(productExceptSelf(arr))