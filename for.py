"""
lista = [2, 6, 9, 4, 0, 12, 3, 7]

for item in lista:
    print(item)


    

lista = [2, 6, 9, 4, 0, 12, 3, 7]
palavra = 'Bóson'

for letra in palavra:
    print(letra)

    
# gera valores de 1 a 10
for numero in range(1,11):
    print(numero)

    

# gera valores de 0 a 9
for numero in range(10):
    print(numero)


    
# gera numeros de 1 a 10, e 10 vezes a variavel nome
nome = input('Digite seu nome: ')
for x in range(10):
    print(f'{x+1} {nome}')





# range(valor_inicial, valor_final, incremento)
# numeros pares
for x in range(2,20,2):
    print(x)


    


# range(valor_inicial, valor_final, incremento)
# numeros pares decrescente
for x in range(20,1,-2):
    print(x)



"""
# Tupla
# continue = encerra a interação atual do laço, nao imprime o Quartzo
pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina' )

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)
