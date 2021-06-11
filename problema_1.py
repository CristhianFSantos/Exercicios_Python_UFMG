'''
Escreva um programa que solicita ao usuário três números inteiros e imprime na tela o número do
meio (mediana).
Observação: as mensagens exibidas para o usuário deverão ser exatamente como apresentado abaixo
(mensagens exibidas com os comandos input() e print()).
Exemplo de execução 1 do programa:
Digite o primeiro número: 2
Digite o segundo número: 8
Digite o terceiro número: 6
Mediana: 6
Exemplo de execução 2 do programa:
Digite o primeiro número: 1
Digite o segundo número: 3
Digite o terceiro número: 1
Mediana: 1
'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

numOrder = sorted([num1, num2, num3])
print(f'Mediana: {numOrder[1]}')