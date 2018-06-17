# coding=utf8
import math
from decimal import *
getcontext().prec = 28

# Função 11 --> Gustavo:
# f0(x)    = 4x - sqrt(e^x) tem raíz entre (0.02, 0.3) aparenta ser o 0.28882
# x        = sqrt(e^x)/4
# phi0(x)  = sqrt(e^x)/4
# phi0(x)' = sqrt(e^x) / 8

def f_gustavo(x):
    return 4*x - Decimal.exp(x).sqrt()

def phi_gustavo(x):
    return Decimal.exp(x).sqrt() / 4

# Função 27 --> Nicolas:
# f1(x)     = 1 - cos(x)*sqrt(x) tem raíz entre (5.161, 5.17) aparenta ser o 5.16785
# phi1(x)   = x + (1 - cos(x)sqrt(x))/sqrt(x)
# phi1(x)   = x + 1/sqrt(x) - cos(x)
# phi1(x)'  = sin(x) -1/(2*x^(2/3)) +1

def f_nicolas(x):
    return 1 - Decimal(math.cos(x)) * x.sqrt()

def phi_nicolas(x):
    return x + 1 / x.sqrt() - Decimal(math.cos(x))

# Função teste = exercício 1 da lista 1 usada para estudar a P1
# 2x^3 - 11.7x^2 + 17.7x - 5 tem raíz entre (3, 4) aparenta ser o 3.5267
# phi(x)  = -0.11x^3 +0.66x^2 + 0.28
# phi(x)' = -0.336x^2 + 1.32x

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
            return k, p

        if abs(f(p)) < erro:
            return k, p

        k += 1
        xn = p

    return k, -1

if __name__ == "__main__":
        print ("(erro, aprox.)")
        (n, xn) = ponto_fixo(0.21, f_gustavo, phi_gustavo)
        #(n, xn) = ponto_fixo(5.161, f_nicolas, phi_nicolas)
        #(n, xn) = ponto_fixo(3.21, f_teste, phi_teste)
        print(n, xn)
