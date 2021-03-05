
def fact(n):   # compute for the factorial
    r = 1
    while n > 0:
        r = r * n
        n -= 1
    return r


print(fact(5))

def f_to_kelvin(degrees_f):
    return 273.15 + (degrees_f - 32) * 5 / 9


abs_temp = f_to_kelvin
print(abs_temp(32))
