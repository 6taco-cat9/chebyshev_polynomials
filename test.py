# recursive formula
# cos(nx) = 2cos(x)cos((n-1)x) - cos((n-2)x)
# cos(2x) = 2cos^2(x) - 1

def main(n):
    co_eff_lst = T_x(n) 
#    for i in co_eff_lst:
#        print(i)
    return co_eff_lst

'''
co_eff = []
def cos_nx(n):
    if n == 1:
        if [1] not in co_eff: co_eff.append([1])
        return [1]
    elif n == 2:
        if [2, -1] not in co_eff: co_eff.append([2, -1])
        return [2, -1]

    lst1 = [i * 2 for i in cos_nx(n - 1)]
    lst2 = [0] + [i * (-1) for i in cos_nx(n - 2)]

    if len(lst1) < len(lst2): lst1 = lst1 + [0]

    lst3 = [sum(i) for i in zip(lst1,lst2)]
    if lst3 not in co_eff: co_eff.append(lst3)

    return lst3
'''

def cos_nx(n):
    if n == 1: return [1]
    elif n == 2: return [2, -1]

    if n % 2 == 0:
        return [sum(i) for i in zip([i*2 for i in cos_nx(n-1)] + [0],[0] + [-1*i for i in cos_nx(n-2)])]
    else:
        return [sum(i) for i in zip([i*2 for i in cos_nx(n-1)],[0] + [-1*i for i in cos_nx(n-2)])]

def sin_nx(n):
    if n == 1: return [1]
    elif n == 2: return [2]

    if n % 2 == 1:
        return [sum(i) for i in zip([i*2 for i in sin_nx(n-1)] + [0],[0] + [-1*i for i in sin_nx(n-2)])]
    else:
        return [sum(i) for i in zip([i*2 for i in sin_nx(n-1)],[0] + [-1*i for i in sin_nx(n-2)])]

def T_x(n):
    lst = [[1], [2, -1]]
    for i in range(2, n):
        a = [j * 2 for j in lst[i-1]]
        b = [0] + [j * (-1) for j in lst[i-2]]
        if len(a) < len(b): a = a + [0]
        lst.append([sum(j) for j in zip(a,b)])
    return lst

def Z_p(n, co_eff_lst):
    co_eff_Zp = []
    for lst in co_eff_lst:
        co_eff_Zp.append([i % n for i in lst])
    return co_eff_Zp


def Tn_Zm(n, m, x):
    co_eff = main(102)[n-1]
    sum = 0
    for i in co_eff:
        sum += i * x**n
        n = n-2
    return sum % m

def generating_function(n, m):
    lst = []
    for x in range(m): # elements in Zm
        print(Tn_Zm(n, m, x))
        lst.append(Tn_Zm(n, m, x))

    if sorted(lst) == [i for i in range(m)]: return "G"
    else: return "N"



for i in [3,5,7,11,13]:
    print(i,i,generating_function(i,i))
    print("\n")



if __name__ == "__main__":
    main(20)
    print("\n")
    # for i in [3,5,7,11,13,17,19]:
    # for i in Z_p(3, main(50)): print(i)
    print("\n")
    # for i in Z_p(5, main(50)): print(i)
    


'''
for n in range(2, 101):
    for m in range(2, 101):
        if sorted([T_nx_Zm(n, m, i) for i in range(1, m)]) == [i for i in range(1, m)]:
            print("T"+ str(n)+ " Z" + str(m)+ " - G")
        else:
            print("T"+ str(n)+ " Z" + str(m)+ " - N")
'''

# to do - 
# period count in Zn
# Tn(x) in Zm # table

def nth_coeff(n, co_eff_lst, p):
    if n == 1: start = 1
    else: start = 2*n - 3

    nth_coeff_lst = [co_eff_lst[i][n-1] for i in range(start, 1000)]
    return [i % p for i in nth_coeff_lst]

def f(x, nth_coeff_lst):
    return nth_coeff_lst[x]

def findperiod(nth_coeff_lst, minlength=2, repetitions=3):
    while minlength <= 500:
        cur_lst = [f(i, nth_coeff_lst) for i in range(minlength)]
        for rep in range(1, repetitions):
            lst = [f(i, nth_coeff_lst) for i in range(minlength*rep, minlength*(rep+1))]
            if cur_lst != lst:
                minlength += 1
                break
        else: return minlength
'''
for n in range(1, 11):
    colst = nth_coeff(n, main(1000), 11)
    print(findperiod(colst))



print(Z_p(3, main(19)))
print(period_count(3, 1))
print(len(principal_period(period_count(3, 1))))

print([[6**i % 109 for i  in range(1, 109)].index(j) + 1 for j in range(1, 109)])
print([i**2%11 for i in range(11)])

str = ""
for i in [2,3,5,7,11,13,17,19,23,29,-2,-3,-5,-7,-11,-13,-17,-19,-23,-29]:
    if i % 113 in [j**2 % 113 for j in range(113)]:
        str += "+"
    else:
        str += "-"
print(str)
'''

def U_x(n):
    lst = [[2], [4, -1]]
    for i in range(2, n):
        a = [j * 2 for j in lst[i-1]]
        b = [0] + [j * (-1) for j in lst[i-2]]
        if len(a) < len(b): a = a + [0]
        lst.append([sum(j) for j in zip(a,b)])
    return lst
