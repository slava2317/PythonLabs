from math import log, exp


def f(x):
    return x ** 2


def calculate_k(x,q):
    mult = abs(x * q)
    border = 10
    if mult > border:
        return log(abs(f(x)) + abs(q))
    elif mult < border:
        return exp(f(x) + q)
    elif mult == border:
        return f(x) + q


x,q = map(int,input("Enter the value of x and q: ").split())
print(calculate_k(x,q))