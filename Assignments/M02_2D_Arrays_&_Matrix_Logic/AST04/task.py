def diagonalSort(mat):
    rows = len(mat)
    cols = len(mat[0])

    # Start from every column in the first row
    for c in range(cols):
        diagonal = []
        i, j = 0, c

        while i < rows and j < cols:
            diagonal.append(mat[i][j])
            i += 1
            j += 1

        diagonal.sort()

        i, j = 0, c
        k = 0

        while i < rows and j < cols:
            mat[i][j] = diagonal[k]
            i += 1
            j += 1
            k += 1

    # Start from every row in the first column
    for r in range(1, rows):
        diagonal = []
        i, j = r, 0

        while i < rows and j < cols:
            diagonal.append(mat[i][j])
            i += 1
            j += 1

        diagonal.sort()

        i, j = r, 0
        k = 0

        while i < rows and j < cols:
            mat[i][j] = diagonal[k]
            i += 1
            j += 1
            k += 1

    return mat


if __name__ == '__main__':
    m, n = map(int, input().split())
    mat = []

    for i in range(m):
        mat.append(list(map(int, input().split())))

    print(diagonalSort(mat))