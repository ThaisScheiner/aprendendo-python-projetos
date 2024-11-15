"""
# Acessar o indice 2 da string
nome = 'Thais'
letra = nome[2]

print(letra)




# saber o tamanho, qtos caracteres da string
nome = 'Thais'
letra = nome[2]

print(len(nome))


# concatenacao '+'
nome = 'Curso de Python'
instrutor = 'Fábio'

print(nome + ' com ' + instrutor)


# split = divide a string em partes em forma de lista
frase = 'Vamos aprender Python hoje.'
palavras = frase.split()
print(palavras)


# split = divide a string em partes em forma de lista 
# e verificar o conteudo na posicao 1
frase = 'Vamos aprender Python hoje.'
palavras = frase.split()
print(palavras[1])

# slice imprimir da posicao 0 ate 5 a palavra vamos
frase = 'Vamos aprender Python hoje.'
print(frase[0:5])


# slice imprimir da posicao 6 ate 15 a palavra aprender
frase = 'Vamos aprender Python hoje.'
print(frase[6:15])


# slice imprimir os 3 ultimos caracteres da string
frase = 'Vamos aprender Python hoje.'
print(frase[-3:])



# find = encontrar dentro da string email qual posicao esta o arroba
email = input('Digite seu endereço de email:')
arroba = email.find('@')
print(arroba)



# slice = separar o nome do usuario do nome do dominio
email = input('Digite seu endereço de email:')
arroba = email.find('@')
print(arroba)
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)



# operadores de associação pra saber se um  
# caracter esta ou nao dentro da string
produtos = 'carbonato de sódio e oxído de zinco'
print('sódio' in produtos)
print('magnésio' in produtos)




# operadores de associação pra saber se um  
# caracter esta ou nao dentro da string
produtos = 'carbonato de sódio e oxído de zinco'
print('sódio' in produtos)
print('magnésio' not in produtos) # nao esta em produtos = true




# find = encontrar 1ª ocorrencia ou inicio de qualquer substring a posicao
item = 'hipoclorito'
pos = item.find('clor') # encontrou a partir da posicao 4
print(pos)
pos = item.find('flu') # nao encontrou, entao retorna -1
print(pos)


# string maiuscula
objeto_celeste = 'galáxia esPiral M31'
print(objeto_celeste.upper())


# string minuscula
objeto_celeste = 'galáxia esPiral M31'
print(objeto_celeste.lower())


# somente a 1ª letra em maiusculo
objeto_celeste = 'galáxia esPiral M31'
print(objeto_celeste.capitalize())


# coloca cada letra de cada palavra em maiusculo
objeto_celeste = 'galáxia esPiral M31'
print(objeto_celeste.title())


# trocar, substituir a string
suplemento = 'cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio', 'zinco')
print(suplemento)
print(n_suplemento)


# remover espaços em branco
frase = '       ômega 3 é bom para a saúde!        '  
print(frase)
print(frase.lstrip()) # esquerda
print(frase.rstrip()) # direita
print(frase.strip())  # elimina espaços a esquerda e direita



# alinhamento de texto para exibição = alinhar a direita, 
# e use 20 espaços para escrever a palavra abacate
fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20))



# alinhamento de texto para exibição = centralizar 

fruta = 'Abacate'
print(fruta)
print(fruta.center(20))


# alinhamento de texto para exibição = alinhar a esquerda 

fruta = 'Abacate'
print(fruta)
print(fruta.ljust(20))


# alinhamento de texto para exibição a esquerda
# passar um caracter diferente nos espaços em branco

fruta = 'Abacate'
print(fruta)
print(fruta.ljust(20, "-"))




# alinhamento de texto para exibição centralizado
# passar um caracter diferente nos espaços em branco

fruta = 'Abacate'
print(fruta)
print(fruta.center(20, "-"))



# prefixos e sulfixos
# dentro da variavel p, o texto começa com a sequencia de caracteres'Bó'
# startswith = prefixo
p = 'Bóson Treinamentos'
print(p.startswith('Bó'))



# prefixos e sulfixos
# dentro da variavel p, o texto termina com a sequencia de caracteres's'
# endswith = sulfixos
p = 'Bóson Treinamentos'
print(p.endswith('s'))



"""
# prefixos e sulfixos
# dentro da variavel p, o texto termina com a sequencia de caracteres's'
# endswith = sulfixos
p = 'Bóson Treinamentos'
print(p.endswith('s'))
 
