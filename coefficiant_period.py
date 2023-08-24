# periods of nth coefficient of Chebyshev polynomials in Zp

# return all nth coefficients in Zp in first 5000 polynomials
def nth_coeff(n, co_eff_lst, p):
    if n == 1: start = 1
    else: start = 2*n - 3

    nth_coeff_lst = [co_eff_lst[i][n-1] for i in range(start, 1000)]
    return [i % p for i in nth_coeff_lst]

# select the xth value in the nth coefficient list
def f(x, nth_coeff_lst):
    return nth_coeff_lst[x]

# period length function (improve repetition for more reliable dara)
def findperiod(nth_coeff_lst, minlength=2, repetitions=3):
    while minlength <= 1500:
        cur_lst = [f(i, nth_coeff_lst) for i in range(minlength)]
        for rep in range(1, repetitions):
            lst = [f(i,nth_coeff_lst) for i in range(minlength*rep,minlength*(rep+1))]
            if cur_lst != lst:
                minlength += 1
                break
        else: return minlength