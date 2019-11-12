m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = []
i = 0
while i < m:
    j = 0
    matrix.append([])
    while j < n:
        v = int(input("matrix[" + str(i) + "," + str(j) + "]="))
        matrix[i].append(v)
        j = j + 1
    i = i + 1


def transpose(matrix):
    transposed = []
    for row in range(n):
        temp = [0] * m
        transposed.append(temp)

    for a in range(m):
        for b in range(n):
            transposed[b][a] = matrix[a][b]

    return transposed


print(transpose(matrix))
