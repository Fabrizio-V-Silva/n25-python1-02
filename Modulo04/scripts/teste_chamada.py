"""
Programa de teste de chamadas com parametros no Python
Author: Richard Brosler
Version: 2025-04-03
"""
from click import clear 
# Definindo funções
def calculo_variaveis(a, b):
    ret = a + b 
    a = 15
    b = 20
    return ret
def uso_lista(lst):
    lst.append(5)
    lst.append(6)
    return len(lst)
# programa principal
d, e =5, 6
lista = [1,2]
# usando as funções
clear()
print(calculo_variaveis(d,e))
print(d,e)
print("Antes")
print(uso_lista(lista))
print("Depois",lista)
