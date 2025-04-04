"""
Código para demonstrar escopo de variáveis no python
Author: Richard Brosler
Version: 2025-04-03
"""
from click import clear
# Definindo uma função
def calculo():
    a = 5
    b = a + c  
   # c = 30 # Se descomentado dá erro porque a variável "C" passa a ser local e não global
    return b
# Programa principal
c = 10
clear()
print(calculo())