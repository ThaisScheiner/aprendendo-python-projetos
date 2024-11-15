
"""
# importar modulos, pcts

ex: import math

# importar uma função especifica, uma constante, um metodo
from math import sqrt, sin = invés de =  import math = para não importar toda a biblioteca do math

# importar tudo
from math import *

# alias
import math as m

print(m.sqrt(81))


import math

print(math.sqrt(81))


# inicio
import mod_func as mf

# controla o fluxo de execução do codigo
# verifica se uma variavel especial interna do python 
# chamada name é igual a main
if __name__ == '__main__':  
    mf.mensagem()

    num = int(input('Digite um numero inteiro: '))

    print(f'\nCalcular fatorial do numero:')
    fat = mf.fatorial(num)
    print(f'O fatorial é {fat}')

    print(f'\nCalcular sequencia fibonacci:')
    fib = mf.fibo(num)
    print(f'O fibonacci é {fib}')
# fim

"""
import mod_func as mf
import numpy as np

if __name__ == '__main__':  
    L = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(L)