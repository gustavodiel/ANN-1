# coding=utf8
import math
from decimal import *
getcontext().prec = 28

# Função 11 --> Gustavo:
def f_gu(x,y):
    return Decimal.exp(-x) + Decimal.exp(y) -x*x -2*y*y*y
def fx_gu(x,y):
    return -Decimal.exp(-x) -2*x
def fy_gu(x,y):
    return -Decimal.exp(y) -6*y*y

def g_gu(x,y):
    return Decimal(math.cos(x+11*y)) +11*x -y -1
def gx_gu(x,y):
    return Decimal(-math.sin(x+11*y))+11
def gy_gu(x,y):
    return Decimal(-11*math.sin(x+11*y)) -1

# Função 27 --> Nicolas: #TODO
def f_ni(x,y):
    return Decimal.exp(-x) + Decimal.exp(y) -x*x -2*y*y*y
def fx_ni(x,y):
    return -Decimal.exp(-x) -2*x
def fy_ni(x,y):
    return -Decimal.exp(y) -6*y*y

def g_ni(x,y):
    return Decimal(math.cos(x+27*y)) +27*x -y -1
def gx_ni(x,y):
    return Decimal(-math.sin(x+27*y))+27
def gy_ni(x,y):
    return Decimal(-27*math.sin(x+27*y)) -1

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

def newton_naoLinear(estimX, estimY, f, fx, fy, g, gx, gy, erro=Decimal("0.001"), maxIteracoes=100):
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
        #print ("TESTE: " + str(jaco))

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
                print(xabs,x,y)
                t = 1
            elif yabs > xabs:
                print(yabs,x,y)
                t = 2
            else:#Erro é o mesmo p/ ambos, tanto faz
                print(xabx,y,s)
                t = 3

            # Verifica se condição de saída foi alcançada
            if t == 1:
                if xabs < erro:
                    return xabs, x, y
            elif t == 2:
                if yabs < erro:
                    return yabs, x, y
            else:#Erro é o mesmo p/ ambos, tanto faz
                return xabs, x, y

        # Atualiza iteracao e a nova aprox
        k += 1
        x = xn
        y = yn

    # Retorna o que deus quiser quando o erro mínimo não for alcançado
    return k,-1,-1

if __name__ == "__main__":
        print ("(erro, aproximX, aproximY)")
        #(n, x, y) = newton_naoLinear(1.5, 1.5, f_teste, fx_teste, fy_teste, g_teste, gx_teste, gy_teste)
        #(n, x, y) = newton_naoLinear(0.24, 1.29, f_gu, fx_gu, fy_gu, g_gu, gx_gu, gy_gu) # Problema gu converge em 5 para sol em (0.24..., 1.29...)
        #(n, x, y) = newton_naoLinear(0.6, 6.2, f_gu, fx_gu, fy_gu, g_gu, gx_gu, gy_gu) # Problema gu TESTE
        # Nicolas
        #(n, x, y) = newton_naoLinear(0.100, 1.338, f_ni, fx_ni, fy_ni, g_ni, gx_ni, gy_ni) # Problema ni converge em 5 para sol em (0.0959, 1.3246)
        (n, x, y) = newton_naoLinear(0.2, 7, f_ni, fx_ni, fy_ni, g_ni, gx_ni, gy_ni) # Problema ni converge em 5 para sol em (0.0959, 1.3246)
        print(n, x, y)
