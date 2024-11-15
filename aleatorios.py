"""
# numeros aleatorios
import random

valor = random.randint(1, 20)
print(valor)




import random

print('Gerar 5 números aleatórios entre 1 e 50: \n')
for i in range(5):
    n = random.randint(1,50)
    print(f'Número gerado: {n}')




# random numero flutuante
import random

valor = random.random()
print(valor)


# random numero flutuante entre 0 e 10
import random

valor = random.random()
print(f'Número gerado: {valor * 10}')




# random numero flutuante entre 0 e 10   round = arredondar com até 2 casas decimais
import random

valor = random.random()
print(f'Número gerado: {round(valor * 10, 2)}')



# random numero flutuante entre 1 e 100  
import random

valor = random.uniform(1, 100)
print(f'Número: {valor}')





# random numero flutuante entre 1 e 100  arredondar com 4 casas decimais
import random

valor = random.uniform(1, 100)
print(f'Número: {round(valor, 4)}')




# sortear 1 numero aleatorio em uma lista  
import random

L = [2, 4, 6, 9, 10, 13, 14, 16, 18, 20, 21, 27, 33]
n = random.choice(L)
print(f'Numero escolhido: {n}')


# sortear 3 numeros aleatorios em uma lista  
import random

L = [2, 4, 6, 9, 10, 13, 14, 16, 18, 20, 21, 27, 33]
n = random.sample(L, 3)
print(f'Numeros escolhidos: {n}')




"""
# embaralhar numeros da lista
import random

L = [2, 4, 6, 9, 10, 13, 14, 16, 18, 20, 21, 27, 33]
print(f'Exibir a lista original: {L}\n')
print(f'Embaralhar a lista e exibi-la: ')
n = random.shuffle(L)
print(L)


