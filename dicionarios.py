"""
# Dicionarios permitem armazenar sequencias  
de dados em pares em chave/valor
similares em arrays associativos
# não permite itens duplicados mas permite de qualquer tipo




# armazena informações de um elemento quimico
# acessa a chave nome e o valor lítio
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}
print(f'Elemento: {elemento['nome']}')



# mostra qtos elemetos possui

elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}
print(f'O dicionario possui {len(elemento)} elementos')




# alterar ou add novos itens ao dicionario
# alterando o grupo 'Metais Alcalinos' para 'Alcalinos'
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}
print(f'Original {elemento}')
elemento['grupo'] = 'Alcalinos'
print(f'Alrerado {elemento}')




# alterar ou add novos itens ao dicionario
# Adicionar a entrada 'período'
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

elemento['período'] = 1
print(elemento)




# alterar ou add novos itens ao dicionario
# exclusão de itens em dicionarios
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

elemento['período'] = 1
print(f'Elemento adiconado: {elemento}')

del elemento['período']
print(f'Elemento excluido: {elemento}')



# alterar ou add novos itens ao dicionario
# apagar todos os itens do dicionario = elemento.clear
# o dicionario ficara vazio
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(elemento)
elemento.clear()
print(elemento)



# alterar ou add novos itens ao dicionario
# apagar o dicionario da memoria  del elemento
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

del elemento
# ocorrerá erro, pois nao existe mais o dicionario 'elemento'
print(elemento) 


# retorna os itens do dicionario
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(elemento.items())




# retorna os itens do dicionario
# mostra as tuplas em cada linha com o laço for
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(elemento.items())
for i in elemento.items():
    print(i)




# retorna os itens do dicionario
# mostra somente as chaves do dicionario
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(elemento.keys())
for i in elemento.keys():
    print(i)



    
# retorna os itens do dicionario
# mostra somente os valores do dicionario
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(elemento.values())
for i in elemento.values():
    print(i)





# retorna os itens do dicionario chave e valor
# desempacotar as chaves e os valores simultaneamente
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

for i, j in elemento.items():
    print(f'{i}: {j}')





"""
# retorna os itens do dicionario chave e valor
# desempacotar as chaves e os valores simultaneamente
elemento = {
    'z': 3,  
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

for i, j in elemento.items():
    print(f'{i}: {j}')