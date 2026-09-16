def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    ans = []
    m = len(a)
    n = len(a[0])
    for i in range(n):
        l = []
        for j in range(m):
            l.append(a[j][i])
        ans.append(l)
    return ans 