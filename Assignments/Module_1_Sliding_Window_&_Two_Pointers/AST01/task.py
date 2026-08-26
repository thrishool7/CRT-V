from typing import List

def The_Great_Run(N: int, k: int, arr: List[int]) -> int:
    window = sum(arr[:k])
    maximum = window

    for i in range(k, N):
        window += arr[i] - arr[i - k]
        maximum = max(maximum, window)

    return maximum


if __name__ == '__main__':
    N, k = map(int, input().split())
    path = list(map(int, input().split()))
    print(The_Great_Run(N, k, path))