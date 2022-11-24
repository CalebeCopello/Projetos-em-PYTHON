#importanto a função do módulo
from random import randint
#gerando o número
nr = randint(1,10)
#variavel para tentativas
t_nr = 0
while True:
    t_nr +=1
    while True:
        try:
            print('Digite um número entre 1 e 10!')
            p_nr = int(input('Qual é o número? '))
        except:
            print('ERRO!: Digite um número válido')
        else:
            if p_nr > 10:
                print('Você digitou um número maior que 10, tente novamente!')
            elif p_nr < 1:
                print('Você digitou um número menor que 1, tente novamente!')
            else:
                break
    if p_nr < nr:
        print('Errou, tente um número mais alto!')
    elif p_nr > nr:
        print('Errou, tente um número mais baixo!')
    else:
        break
    
print(f'Parabéns, você acertou!\nO computador pensou em: {nr}\nVocê tentou: {p_nr}\nVocê acertou depois de {t_nr} tentativas')