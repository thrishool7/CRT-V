def pairInSortedRotated(arr, target):
    n = len(arr)

    # Find the smallest element
    pivot = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            pivot = i
            break

    left = pivot
    right = (pivot - 1 + n) % n

    while left != right:
        total = arr[left] + arr[right]

        if total == target:
            return True
        elif total < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n

    return False


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))