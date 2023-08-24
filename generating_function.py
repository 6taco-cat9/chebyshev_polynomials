# coefficients in Zp
def Z_p(n, co_eff_lst):
    co_eff_Zp = []
    for lst in co_eff_lst:
        co_eff_Zp.append([i % n for i in lst])
    return co_eff_Zp
    

# generating polynomial
# return Tn(x) mod m
def Tn_Zm(n, m, x):
    co_eff = co_eff_lst[n-1]
    sum = 0
    for i in co_eff:
        sum += i * x**n
        n = n-2
    return sum % m

# check whether or not Zm -> Zm
def generating_function(n, m):
    lst = []
    for x in range(m): # elements in Zm
        lst.append(Tn_Zm(n, m, x))

    if sorted(lst) == [i for i in range(m)]: return "G"
    else: return "N"