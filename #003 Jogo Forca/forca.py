from random import randint
#definindo variaveis
palavras = ['agua', 'pão', 'carro', 'dado', 'fogueira']
pal_secreta = palavras[randint(0,len(palavras) - 1)]
pal_dica = []
tentativas = 5
#colocando a dica em uma lista
for c in range(0, len(pal_secreta)):
    pal_dica.append('_')
#interação com o usuário
print(f'A palavra secreta tem {len(pal_secreta)} letras')
#mostrando a quantidade de letras
print('      _______')
print('     |/      |')
print('     |')
print('     |')
print('     |')
print('     |')
print('     |')
print('  ___|___')
print('')
for c in range(0, len(pal_dica)):
    print(f'{pal_dica[c]}', end=' ')
print('')
print('')
#iniciando o loop do jogo
while tentativas > 0:
#pegando informação do usuário
    while True:
        tentativa = str(input('Digite uma letra: ')).lower()
        if tentativa.isalpha():
            if len(tentativa.strip()) > 1:
                print('Digite apenas uma letra!')
            if len(tentativa.strip()) == 1:
                break
        else:
            print('Você não digitou uma letra!')
        print('')
#verificando se a letra está contida na palavra
#DO TO colocar uma condição caso a letra ja tenha sido escolhida
#DO TO ajustar para aceitar letras com acentos também
    if tentativa in pal_secreta:
        print(f'Parabéns a letra {tentativa} está na palavra, essa aparece na palavra {pal_secreta.count(tentativa)}')
        for c in range(0, len(pal_secreta)):
            if pal_secreta[c] == tentativa:
                pal_dica[c] = tentativa.upper()
    else:
        print(f'Que pena! A letra {tentativa} não está na palavra')
        tentativas -= 1
    for c in range(0, len(pal_dica)):
        print(f'{pal_dica[c]}', end=' ')
    print('')
    if '_' not in pal_dica:
        print(f'Parabéns você ganhou')
        break
    if tentativas == 0:
        print(f'Você perdeu\nA palavra era {pal_secreta}')

'''print('      _______')
print('     |/      |')
print('     |      (_)')
print('     |      \|/')
print('     |       |')
print('     |      / \\')
print('     |')
print('  ___|___')
'''