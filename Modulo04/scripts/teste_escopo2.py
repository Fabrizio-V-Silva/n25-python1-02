"""
Programa de teste de escopo de variáveis - 2
Author: Richard Brosler
Version: 2025-04-03
"""
from click import clear
def calculo():
    global c # independente de ter uma variável dentro do local, será usada a do global
    a = 5
    b = a + c 
    c = 30 # este "C" esta local (dentro da função)
    d = 50
    return b
# programa principal
c= 10 # este "C" esta global (fora da função)
print(calculo())
print("Valor de c=", c)