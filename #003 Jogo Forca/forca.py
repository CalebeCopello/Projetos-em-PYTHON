from random import randint
palavras = ['agua', 'pao', 'carro', 'dado', 'fogueira']
pal_secreta = palavras[randint(0,len(palavras) - 1)]
print(f'A palavra secreta tem {len(pal_secreta)} letras')
for c in range(0, len(pal_secreta)):
    print(f'_', end=' ')
print('')
while True:
    while True:
        tentativa = str(input('Qual é a primeira letra da palavra?'))
        if tentativa.isalpha():
            if len(tentativa.strip()) > 1:
                print('Digite apenas uma letra!')
            if len(tentativa.strip()) == 1:
                break
        else:
            print('Você não digitou uma letra!')
    break