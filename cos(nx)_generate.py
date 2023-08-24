# recursive formula
# cos(nx) = 2cos(x)cos((n-1)x) - cos((n-2)x)
def cos_nx(n):
    if n == 1: return [1]
    elif n == 2: return [2, -1]

    if n % 2 == 0:
        return [sum(i) for i in zip([i*2 for i in cos_nx(n-1)] + [0],[0] + [-1*i for i in cos_nx(n-2)])]
    else:
        return [sum(i) for i in zip([i*2 for i in cos_nx(n-1)],[0] + [-1*i for i in cos_nx(n-2)])]

# lst of coefficients up from T_1 to to T_n
def T_x(n):
    lst = [[1], [2, -1]]
    for i in range(2, n):
        a = [j * 2 for j in lst[i-1]]
        b = [0] + [j * (-1) for j in lst[i-2]]
        if len(a) < len(b): a = a + [0]
        lst.append([sum(j) for j in zip(a,b)])
    return lst