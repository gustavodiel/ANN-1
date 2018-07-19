# coding=utf8
import math
from decimal import *
getcontext().prec = 5

# Função 11 --> Gustavo:
def f_gu(x,y):
    return Decimal.exp(-x) + Decimal.exp(y) -x*x -2*y*y*y
def fx_gu(x,y):
    return -Decimal.exp(-x) -2*x
def fy_gu(x,y):
    return Decimal.exp(y) -6*y*y

def g_gu(x,y):
    return Decimal(math.cos(x+11*y)) +11*x -y -1
def gx_gu(x,y):
    return -Decimal(math.sin(x+11*y))+11
def gy_gu(x,y):
    return -11*Decimal(math.sin(x+11*y)) -1

# Função 27 --> Nicolas:
def f_ni(x,y):
    return Decimal.exp(-x) + Decimal.exp(y) -x*x -2*y*y*y
def fx_ni(x,y):
    return -Decimal.exp(-x) -2*x
def fy_ni(x,y):
    return Decimal.exp(y) -6*y*y

def g_ni(x,y):
    return Decimal(math.cos(x+27*y)) +27*x -y -1
def gx_ni(x,y):
    return -Decimal(math.sin(x+27*y))+27
def gy_ni(x,y):
    return -27*Decimal(math.sin(x+27*y)) -1

# 1o exemplo da foto que mandei ao Diel (funcionando vide resolucao manual -- verificado)
def f_teste(x,y):
    return x ** 2 + y ** 2 - 4
def fx_teste(x,y):
    return 2*x
def fy_teste(x,y):
    return 2*y

def g_teste(x,y):
    return x ** 2 - y ** 2 - 1
def gx_teste(x,y):
    return 2*x
def gy_teste(x,y):
    return -2*y

def newton_naoLinear(estimX, estimY, f, fx, fy, g, gx, gy, erro=Decimal("0.00001"), maxIteracoes=1000):
    k = 0
    # Flag
    t = 0

    # Estimativa inicial
    x = Decimal(estimX)
    y = Decimal(estimY)

    while k < maxIteracoes:
        # Obtem valores para as derivadas parciais com aprox aplicadas
        rfx = fx(x,y)
        #print("TESTE fx: " + str(rfx))
        rfy = fy(x,y)
        #print("TESTE fy: " + str(rfy))
        rgx = gx(x,y)
        #print("TESTE gx: " + str(rgx))
        rgy = gy(x,y)
        #print("TESTE gy: " + str(rgy))

        # Calcula o jacobiano do sistema
        jaco = rfx*rgy - rgx*rfy
        # print ("TESTE: " + str(jaco))
        got_error = 0

        if jaco == 0:
            break;
        elif jaco != 0:
            # Calcula valores para as funções de ponto fixo nao lineares com aprox aplicadas
            rf = f(x,y)
            rg = g(x,y)

            # Calcula valores para (x=xn,y=yn) na iteracao presente
            xn = x - (rf*rgy - rg*rfy)/jaco
            yn = y - (rg*rfx - rf*rgx)/jaco

            # Calcula erro abs infinito
            xabs = abs(xn - x)
            yabs = abs(yn - y)
            if xabs > yabs:
            #    print(x,y)
                t = 1
            elif yabs > xabs:
            #    print(x,y)
                t = 2
            else:#Erro é o mesmo p/ ambos, tanto faz
            #    print(y,s)
                t = 3

            # Verifica se condição de saída foi alcançada
            if t == 1:
                got_error = xabs
                if xabs < erro:
                    return k, x, y
            elif t == 2:
                got_error = yabs
                if yabs < erro:
                    return k, x, y
            else: # Erro é o mesmo p/ ambos, tanto faz
                if yabs < erro and xabs < erro:
                    return k, x, y

        # Atualiza iteracao e a nova aprox
        k += 1
        x = xn
        y = yn

        print(k, x, y, got_error)

    # Retorna o que deus quiser quando o erro mínimo não for alcançado
    return "Esgotou limite de iteracoes",x,y

if __name__ == "__main__":
        print("    Resultados")
        print("(iterações, x, y)")
        # (n, x, y) = newton_naoLinear(1.5, 1.5, f_teste, fx_teste, fy_teste, g_teste, gx_teste, gy_teste)
        # Gustavo
        # (n, x, y) = newton_naoLinear(-1.6, 1.29, f_gu, fx_gu, fy_gu, g_gu, gx_gu, gy_gu) # Sol 1 do problema gu, sol em 5 p/ (0.2449, 1.2998)
        # (n, x, y) = newton_naoLinear(0.5, 7.0, f_gu, fx_gu, fy_gu, g_gu, gx_gu, gy_gu) # Sol 2 do problema gu, sol em 5 p/ (0.60200, 6.13457)
        (n, x, y) = newton_naoLinear(-50, -50, f_gu, fx_gu, fy_gu, g_gu, gx_gu, gy_gu) # Sol 2 do problema gu, sol em 5 p/ (0.60200, 6.13457)
        #
        # Nicolas
        # (n, x, y) = newton_naoLinear(2.19, 1.32, f_ni, fx_ni, fy_ni, g_ni, gx_ni, gy_ni) # Sol 1 do problema ni, sol em 5 p/ (0.0921, 1.3287)
        # (n, x, y) = newton_naoLinear(9.19, 6.2, f_ni, fx_ni, fy_ni, g_ni, gx_ni, gy_ni) # Sol 2 do problema ni, sol em 5 p/ (0.2944, 6.1325)
        # (n, x, y) = newton_naoLinear(-50, -50, f_ni, fx_ni, fy_ni, g_ni, gx_ni, gy_ni) # Sol 2 do problema gu, sol em 5 p/ (0.60200, 6.13457)
        # print(n, x, y)
