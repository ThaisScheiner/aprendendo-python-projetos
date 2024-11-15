"""
# São imutáveis, mais rapidas que as listas

tupla = (2, 4, 6, 7, 9)
print(tupla)


# qtos elementos tem na tupla
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
print(len(halogenios))

# visualizar o elemento 3 
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
print(halogenios[3])

# visualizar ultimo elemento 
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
print(halogenios[-1])

# qtas vezes aparece o nº 5
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5, 2, 6, 8, 4, 4, 5, 6, 4, 0, 12, 22, 3, 4, 5)
print(t1.count(5))

# imprimir de 0 ate 2 elementos
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres

print(halogenios[0:2])


# imprimir do 1º ate o 3º elemento
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres

print(halogenios[:3])


# imprimir os 2 ultimos elementos
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres

print(halogenios[-2:])


# verifica se o elemento esta presente na tupla, no caso o Cl
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres

print('Cl' in halogenios)


# somar todos os valores da tupla t1
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5, 2, 6, 8, 4, 4, 5, 6, 4, 0, 12, 22, 3, 4, 5)
print(sum(t1))


# valor minimo e valor maximo da tupla t1
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5, 2, 6, 8, 4, 4, 5, 6, 4, 0, 12, 22, 3, 4, 5)
print(min(t1))
print(max(t1))

# o que nao pode fazer com a tupla que pode fazer na lista
# operações nao disponiveis em tuplas: .sort(), .append(), .reverse(), .pop()
# todos os metodos que alteram a tupla sao indisponiveis



# tupla no laço for
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5, 2, 6, 8, 4, 4, 5, 6, 4, 0, 12, 22, 3, 4, 5)
print(min(t1))
print(max(t1))

for elemento in elementos:
    print(f'Elemento quimico: {elemento}')

    

# cria lista a partir de uma tupla e add o H na lista do grupo17
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5, 2, 6, 8, 4, 4, 5, 6, 4, 0, 12, 22, 3, 4, 5)

grupo17 = list(halogenios)
grupo17[0] = 'H'
print(grupo17)


# cria uma tupla a partir de uma lista
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5, 2, 6, 8, 4, 4, 5, 6, 4, 0, 12, 22, 3, 4, 5)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)


"""

# sorted = criando uma nova tupla para ordenar em ordem alfabetica
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5, 2, 6, 8, 4, 4, 5, 6, 4, 0, 12, 22, 3, 4, 5)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)
print(sorted(alcalinos))
