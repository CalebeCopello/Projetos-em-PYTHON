#funções para colorir o texto
def yt (msg):
    return f'\033[0;33;40m{msg}\033[0;37;40m'
def rt (msg):
    return f'\033[0;31;40m{msg}\033[0;37;40m'
def gt (msg):
    return f'\033[0;32;40m{msg}\033[0;37;40m'


#código principal
#importanto a função do módulo
from random import randint
#gerando o número
nr = randint(1,10)
#variavel para tentativas
t_nr = 0
while True:
    t_nr +=1
    #tratamento de erros
    while True:
        try:
            print(f'Digite um número entre {yt(1)} e {yt(10)}!')
            p_nr = int(input('Qual é o número? '))
        except:
            print(f'{rt("ERRO!")}: Digite um número válido')
        else:
            if p_nr > 10:
                print(f'Você digitou um número {rt("maior que 10")}, tente novamente!')
            elif p_nr < 1:
                print(f'Você digitou um número {rt("menor que 1")}, tente novamente!')
            else:
                break
    #guiando o usuário
    if p_nr < nr:
        print(f'{rt("Errou")}, tente um número {rt("maior!")}')
    elif p_nr > nr:
        print(f'{rt("Errou")}, tente um número {rt("menor!")}')
    else:
        break
#mensagem do resultado
print(f'Parabéns, você {gt("acertou!")}\nO computador pensou em: {yt(nr)}\nVocê tentou: {yt(p_nr)}\nVocê acertou depois de {yt(t_nr)} tentativas')
