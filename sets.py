"""
# set = conjunto, 
# coleções nao ordenadas de valores unicos
# armazenam itens nao duplicados,
# suportam operações matematicas sobre conjuntos
# nao consegue modificar os itens mas consegue add elementos



# criando um set
planeta_anao = {'Plutão', 'ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)



# qtos elementos tem o set
planeta_anao = {'Plutão', 'ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(planeta_anao))



# verifica se o conjunto tem ou nao um valor especifico
planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print('Ceres' in planeta_anao)
print('Lua' not in planeta_anao) 



# coloca todos os elementos em mauisculo na mesma linha
planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}

for astro in planeta_anao:
    print(astro.upper(), end=' ')




# criando conjunto a partir de outras sequencias
# ter uma lista e transformar num set

astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print(f'lista {astros}')

astro_set = set(astros)
print(f'set {astro_set}')



# comparações set 
astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa Halley'}
print(astros1 == astros2)


# união de conjuntos com o pipe ' | ' ou .union
astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa Halley'}
print(astros1 | astros2)
# ou 
print(astros1.union(astros2))


# intersecção de conjuntos = todos elementos em comum
# & ou .intersection
astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa Halley'}
print(astros1 & astros2)
# ou 
print(astros1.intersection(astros2))


# verificar diferença simetrica de conjuntos
# ^ ou symmetric_difference
astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa Halley'}
print(astros1 ^ astros2)
# ou 
print(astros1.symmetric_difference(astros2))




# adicionar elementos no conjunto
astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa Halley'}

astros1.add('Urano')
astros1.add('Sol')
print(astros1)



# remover elementos no conjunto
astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa Halley'}

astros1.remove('Lua')
# ou 
astros1.discard('Io')
print(astros1)



# remover elemento arbitrário no conjunto aleatório
astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa Halley'}

astros1.pop()
print(astros1)

"""

# limpar todo o conjunto
astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa Halley'}

astros1.clear()
print(astros1)
