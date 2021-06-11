'''
Escreva um programa que solicita ao usuário três valores x, y e z e verifica se eles podem ser os comprimentos
do lado de um triângulo. Caso eles formem um triângulo, imprima se o mesmo é um triângulo
equilátero, isósceles ou escaleno. 
Considere o que segue:
• Para verificar se é um triângulo, confira se os lados obedecem a desigualdade triangular: 
z < x + y e y < x + z e x < y + z
Tipo do triângulo Lados
Triângulo Equilátero 3 lados iguais
Triângulo Isósceles 2 lados iguais
Triângulo Escaleno 3 lados diferentes
Observação: as mensagens exibidas para o usuário deverão ser exatamente como apresentado abaixo
(mensagens exibidas com os comandos input() e print()).
Exemplo de execução 1 do programa:
Digite o comprimento do primeiro lado: 1
Digite o comprimento do segundo lado: 2
Digite o comprimento do terceiro lado: 5
Não é um triângulo
Exemplo de execução 2 do programa:
Digite o comprimento do primeiro lado: 16
Digite o comprimento do segundo lado: 20
2
Digite o comprimento do terceiro lado: 30
Triângulo Escaleno
Exemplo de execução 3 do programa:
Digite o comprimento do primeiro lado: 11
Digite o comprimento do segundo lado: 11
Digite o comprimento do terceiro lado: 20
Triângulo Isósceles
'''

z = int(input('Digite o comprimento do primeiro lado: '))
x = int(input('Digite o comprimento do segundo lado: '))
y = int(input('Digite o comprimento do terceiro lado: '))

if  (z < x + y and y < x + z and x < y + z):
    if x == z and x == y:
        print('Triângulo Equilátero')
    elif x != z and x != y:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Não é um triângulo')
