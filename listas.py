"""
# lista: representa uma sequencia de valores
# sintaxe: nome_lista = [valores]

incice 0,1,2,3,4, ...


notas = [5, 7, 8, 6, 9]
print(notas)



# juntando 2 lista e formando uma nova lista
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 4]
valores = n1 + n2
print(valores)



# acessando o 1° item da lista
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 4]
valores = n1 + n2
print(valores[0])



# acessando o ultimo item da lista
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 4]
valores = n1 + n2
print(valores[-1])


# acessando o penultimo item da lista
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
print(valores[-2])


# alterar a 1ª posicao da lista
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores[0] = 9
print(valores[0])


# valores sequenciais, imprimir valores a partir do 1° valor = 0: , 2 valores
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores[0] = 9
print(valores[0:2])


# mostra os 4 primeiros itens
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores[0] = 9
print(valores[:4])



# mostra o valor 8
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores[0] = 9
print(valores[3:4])


# mostra os 2 ultimos elementos
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores[0] = 9
print(valores[-2:])


# saber qtos elementos tem na lista
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores[0] = 9
print(len(valores))


# retorna versao ordenada da lista crescente
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores[0] = 9
print(sorted(valores))



# retorna versao ordenada da lista decrescente
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores[0] = 9
print(sorted(valores, reverse=True))

# somar todos os valores da lista
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores[0] = 9
print(sum(valores))



# valor minimo e valor maximo da lista
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores[0] = 9
print(min(valores))
print(max(valores))


# append = inserir um novo elemento no final da lista
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2
valores.append(13)
print(valores)




# pop = excluir um elemento no final da lista
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2

valores.append(13)
print(valores)
valores.pop()
print(valores)


# pop = excluir o elemento na posicao 3 da lista, no caso o 8 foi excluido
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2

valores.append(13)
print(valores)
valores.pop()
print(valores)
valores.pop(3)
print(valores)




# inserir elemento na posicao 3, com o valor 21 valores.insert(3, 21)
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2

valores.append(13)
print(valores)
valores.pop()
print(valores)
valores.pop(3)
print(valores)
valores.insert(3, 21)
print(valores)


# verifica se existe um valor dentro da lista  = print(12 in valores)
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6 ,3, 0, 12, 11]
valores = n1 + n2

valores.append(13)
print(valores)
valores.pop()
print(valores)
valores.pop(3)
print(valores)
valores.insert(3, 21)
print(valores)
print(12 in valores)



planetas = ['Mecurio', 'Venus', 'Marte', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta)


    
"""
 
bebidas = []

for i in range(5):
    print(f'Digite uma bebida favorita:')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f'\nBebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)

print('\nSaude!')


