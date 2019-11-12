def multiply(m, n):
    c = []
    for rowc in range(len(m)):
        temps = [0] * len(n[0])
        c.append(temps)
    for l in c:
        print(l)
    for row in range(len(m)):
        for col in range(len(n[0])):
            for k in range(len(n)):
                c[row][col] += m[row][k] * n[k][col]
    return c


m = [[1, 2, 3], [4, 5, 6]]
n = [[1, 2], [3, 4], [5, 6]]

print(multiply(m, n))
