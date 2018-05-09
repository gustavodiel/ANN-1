import math
from decimal import *

getcontext().prec = 28

#phi(x) = x + A(X) * f(x)

#Funcao Gustavo: 4x - sqrt(e^x) = 0
#4x - sqrt(e^x) + x = x
#5x - sqrt(e^x) = x
#derivada: 5 - sqrt(e^x) / 2

#Funcao Nicolas: 1 - cost(x) * sqrt(x)

def g_gustavo(x):
    return x - f_gustavo(x) / fl_gustavo(x)

def fl_gustavo(x):
    return (Decimal(5) - (Decimal.exp(x)).sqrt() / Decimal(2))


def f_gustavo(x):
    return Decimal(4) * x - Decimal.exp(x).sqrt()


def ponto_fixo(pA, f, g, erro=Decimal("0.001"), max_iteracoes=100):
    k = 0
    xn = Decimal(pA)
    while k < max_iteracoes:
        p = g(xn)
        menos = p - xn
        print(menos, p)
        if abs(menos) < erro:
            print("UMM")
            return k, p

        if abs(f(p)) < erro:
            print("TRE")
            return k, p

        k += 1
        xn = p

    return k, -1


if __name__ == "__main__":

    (n, xn) = ponto_fixo(2, f_gustavo, g_gustavo, Decimal("0.0000001"), max_iteracoes=5000)
    print(n, xn)
