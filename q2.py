def sum(m, n):
    c = []
    for rowc in range(len(m)):
        temps=[0]*len(m[0])
        c.append(temps)
    for row in range(len(m)):
        for col in range(len(m[0])):
            c[row][col] = m[row][col] + n[row][col]
    return c

m=[[1, 2], [3, 4]]
n=[[1, 1], [1, 1]]
print(sum(m,n))
