#função para retirar acentos
def acento(p):
    p = p.replace('á','a')
    p = p.replace('ã','a')
    p = p.replace('â','a')
    p = p.replace('é','e')
    p = p.replace('ê','e')
    p = p.replace('í','i')
    p = p.replace('ó','o')
    p = p.replace('õ','o')
    p = p.replace('ô','o')
    p = p.replace('ú','u')
    return p

#importando modulos
from random import randint
#definindo variaveis
palavras = ['água', 'pão', 'carro', 'dado', 'fogueira']
pal_secreta = palavras[randint(0,len(palavras) - 1)]
pal_dica = []
tentativas = 6
tentativa_erro = ''
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
    if tentativa in acento(pal_secreta) and tentativa.upper() not in pal_dica:
        print(f'Parabéns a letra {tentativa.upper()} está na palavra, essa letra aparece na palavra {acento(pal_secreta).count(tentativa)} vez(es)')
        for c in range(0, len(pal_secreta)):
            if acento(pal_secreta[c]) == tentativa:
                pal_dica[c] = tentativa.upper()
    elif tentativa.upper() in pal_dica or tentativa.upper() in tentativa_erro.upper():
        print(f'Você já tentou a letra {tentativa.upper()}, tente outra letra')
    elif tentativa not in acento(pal_secreta):
        print(f'Que pena! A letra {tentativa} não está na palavra')
        tentativas -= 1
        tentativa_erro = tentativa + tentativa_erro
        if tentativas == 5:
            print('      _______')
            print('     |/      |')
            print('     |      (_)')
            print('     | ')
            print('     |')
            print('     |')
            print('     |')
            print('  ___|___')
        print(tentativa_erro)
    for c in range(0, len(pal_dica)):
        print(f'{pal_dica[c]}', end=' ')
    print('')
    if '_' not in pal_dica:
        print(f'Parabéns você ganhou\nA palavra era {pal_secreta}')
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