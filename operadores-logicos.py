""" 

AND - e
OR  - ou 
NOT - inverte


# AND
idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode participar do evento? ' + str(resultado)

print(msg)



# OR
# Programa de disparo de alarme

porta = 'f'    # f = fechar a = aberto
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = 'Alarme disparado? ' +str(alarme)
print(msg)

"""

# NOT  inverte o estado logico

tem_dinheiro = False
tem_dinheiro = not tem_dinheiro

msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)