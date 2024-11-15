"""
# Simples, Composto, encadeado

# Simples
n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if (media >= 7):
    print('Resultado aprovado!')
    print('Parabéns"')

print('Sua média é {}'.format(media))

# Composto
n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if (media >= 7):
    print('Resultado aprovado!')
    print('Parabéns"')
else:
    print('Aluno reprovado...')

print('Sua média é {}'.format(media))


"""
# Encadeado elif = else if

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if (media >= 7):
    print('Resultado aprovado!')
    print('Parabéns"')
elif(media >= 5):
    print('Você está de Recuperação')
else:
    print('Aluno reprovado...')

print('Sua média é {}'.format(media))