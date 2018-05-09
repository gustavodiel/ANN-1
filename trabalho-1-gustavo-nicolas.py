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
# ---- Considerações no algoritmo
# phi_gustavo  = phi0(x)
# phiD_gustavo = phi0(x)'

def phi_gustavo(x):
    return Decimal.exp(x).sqrt() / 4

def phiD_gustavo(x):
    return Decimal.exp(x).sqrt() / 8

# Funcao 27 --> Nicolas:
# f1(x)     = 1 - cos(x)*sqrt(x) tem raíz entre (5.165, 5.166) aparenta ser o 5.1655
# phi1(x)   = x + (1 - cos(x)sqrt(x))/sqrt(x)
# phi1(x)   = x + 1/sqrt(x) - cos(x)
# phi1(x)'  = sin(x) -1/(2*x^(2/3)) +1
# ---- Considerações no algoritmo
# phi_nicolas   = phi1(x)
# phiD_nicolas  = phi1(x)'

def phi_nicolas(x):
    return x + 1 / x.sqrt() - Decimal(math.cos(x))

def phiD_nicolas(x):
    return Decimal(math.sin(x)) - 1 / ( 2 * x ** (2/3) ) + 1

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
    (n, xn) = ponto_fixo(0.001, phi_nicolas, phiD_nicolas)
    print(n, xn)
