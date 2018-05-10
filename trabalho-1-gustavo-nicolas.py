# coding=utf8
import math
from decimal import *
# Para que serve isso?
getcontext().prec = 28

# Funcao 11 --> Gustavo:
# f0(x)    = 4x - sqrt(e^x) tem raíz entre (-0.0001, 0.0001) aparenta ser o 0
# x        = sqrt(e^x)/4
# phi0(x)  = sqrt(e^x)/4
# phi0(x)' = sqrt(e^x) / 8

def f_gustavo(x):
    return 4*x - Decimal.exp(x).sqrt()

def phi_gustavo(x):
    return Decimal.exp(x).sqrt() / 4

# Funcao 27 --> Nicolas:
# f1(x)     = 1 - cos(x)*sqrt(x) tem raíz entre (5.165, 5.166) aparenta ser o 5.1655
# phi1(x)   = x + (1 - cos(x)sqrt(x))/sqrt(x)
# phi1(x)   = x + 1/sqrt(x) - cos(x)
# phi1(x)'  = sin(x) -1/(2*x^(2/3)) +1

def f_nicolas(x):
    return x + 1 / x.sqrt() - Decimal(math.cos(x))

def phi_nicolas(x):
    return Decimal(math.sin(x)) - 1 / ( 2 * x ** Decimal(1.5) ) + 1


def f_teste(x):
    return 2 * x ** 3 - Decimal(11.7) * x ** 2 + Decimal(17.7) * x - 5

def phi_teste(x):
    return - Decimal(0.112) * x ** 3 + Decimal(0.66) * x ** 2 + Decimal(0.28)


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
    (n, xn) = ponto_fixo(5.1, f_teste, phi_teste)
    print(n, xn)
