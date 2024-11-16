"""
# funções - bloco de código
# Modularização, reuso de código, legibilidade

# funções internas e funções definidas pelo usuario

def <nome_função> ([argumentos]):
    <instrucoes>

    
# função
def mensagem():
    print('Curso completo de Python.')

mensagem()



# função com argumento
def soma(a, b):
    print(a + b)

soma(12, 7)



# função com argumento multiplicação
def mult(x, y):
    return(x * y)

a = 5
b = 8
c = mult(a, b)
print(f'O produto de {a} X {b} é {c}')




# função com argumento divisao
def div(k, j):
    if j != 0:
        return k / j
    else:
        return 'Impossível dividir por zero!'

if __name__ == '__main__':
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))

    r = div(a, b)
    print(f'{a} dividido por {b} é igual a {r}')


"""

# calcular valores de numeros ao quadrado 
def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2, 5, 7 ,9, 12]
    resultados = quadrado(valores)
    for g in resultados:
        print(g) 


#PAREI 05:25:15