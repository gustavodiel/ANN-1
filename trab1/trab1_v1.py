import math
from decimal import *

getcontext().prec = 28

def g(x):
    return x - x * x * x - Decimal(4)*(x * x) + Decimal(10)

def f(x):
    return x * x * x + Decimal(4)*(x * x) - Decimal(10)


def ponto_fixo(pA, erro=Decimal("0.001"), max_iteracoes=100):
    k = 0
    xn = Decimal(pA)
    while k < max_iteracoes:
        p = f(xn)
        menos = (p - xn)
        print(menos)
        if abs(menos) < erro or menos/(abs(p)) < erro or abs(f(p)) < erro:
            return (k, p)

        k += 1
        xn = p

    return (k, -1)



if __name__ == "__main__":

    (n, xn) = ponto_fixo(1.5, Decimal("0.1"))
    print(n, xn)