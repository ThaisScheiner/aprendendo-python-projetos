"""
print('Imprime a msg e muda de linha')
print('Imprime a msg e permanece na linha.', end='') # quebra de linha
print(' Continuo na mesma linha!')



nome = 'Maria'
idade = 30
msg_formatada = 'O nome dela é {0} e ela tem {1} anos.'.format(nome, idade)
print(msg_formatada)


nome = 'Fábio'
peso = 73.50
msg = f'Olá, meu nome é {nome} e eu peso {peso} quilos.'
print(msg)


a = 10
b = 5
res = f'A soma de {a} com {b} é igual a {a+b}'
print(res)


# mostrar somente 2 casas decimais
valor = 125.573637
print(f'O valor é {valor:.2f}')


# mostra o valor entre aspas simples
valor = 125.573637
print(f'O valor é \'{valor:.2f}\'')

"""
# Tabulação
nome = 'João'
idade = 32
print(f'Nome:{nome}\tIdade:{idade}')