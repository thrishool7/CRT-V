from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    result = []
    r, c = rStart, cStart

    result.append([r, c])

    steps = 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while len(result) < rows * cols:
        for i in range(4):
            dr, dc = directions[i]

            for _ in range(steps):
                r += dr
                c += dc

                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])

                    if len(result) == rows * cols:
                        return result

            # Increase steps after Right and Left
            if i == 1 or i == 3:
                steps += 1

    return result


if __name__ == '__main__':
    rows, cols, rStart, cStart = map(int, input().split())
    print(spiralMatrixIII(rows, cols, rStart, cStart))