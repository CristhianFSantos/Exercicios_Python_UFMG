'''
Escreva um programa que calcule as raízes da equação de segundo grau, dado os valores de a, b e c:
ax^2 + bx + c = 0
Lembrando que:
x = 
-b +- Rd / 2a

d = b^2 - 4ac
A variável a tem que ser diferente de zero. Caso seja igual a zero, imprima a mensagem "Não é uma
equação quadrática".

• Se d < 0 , não existe raiz real. Imprima a mensagem "Não existe raiz real".
• Se d = 0 , existe uma raiz real. Imprima a mensagem "Raiz única"e o valor da raiz.
• Se d >= 0, imprima as duas raízes.
Observação: as mensagens exibidas para o usuário deverão ser exatamente como apresentado abaixo
(mensagens exibidas com os comandos input() e print()).

Exemplo 1 de execução do programa:
Digite o valor de a: 2
Digite o valor de b: 5
Digite o valor de c: 8
Não existe raiz real

Exemplo 2 de execução do programa:
Digite o valor de a: 4
Digite o valor de b: -4
Digite o valor de c: 1
Raiz única
Raiz = 0.50

Exemplo 3 de execução do programa:
Digite o valor de a: 3
Digite o valor de b: 6
Digite o valor de c: 2
Raiz 1 = -0.42
Raiz 2 = -1.58
'''


a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b**2 - 4*a*c)
if a != 0:
    if delta < 0:
        print('Não existe raiz real')
    elif delta == 0:
        print('Raiz única')
        print(f'Raiz = {round((-b + delta**(1/2)) / (2*a),1)}0')
    elif delta >= 0:
        print(f'Raiz 1 = {round((-b + delta**(1/2)) / (2*a),2)}')
        print(f'Raiz 2 = {round((-b - delta**(1/2)) / (2*a),2)}')
else:
    print('Não é uma equação quadrática')

