'''
Escreva um programa que peça ao usuário o valor da sua hora de trabalho, a quantidade de horas trabalhadas no mês e calcula a sua folha de pagamento. 
São descontados do salário o Imposto de Renda, que depende do salário bruto (conforme tabela abaixo), e o INSS, que corresponde a 10% do salário bruto.
O FGTS corresponde a 11% do salário bruto, no entanto o FGTS não é descontado do salário, pois é a empresa que deposita. 
O salário líquido corresponde ao salário bruto menos os descontos.

Salário Bruto                    |   Imposto de Renda
---------------------------------|----------------------
Até R$900                        |   Isento
Maior que R$900 até R$1500       |   Desconto de 5%
Maior que R$1500 até R$2500      |   Desconto de 10%
Maior que R$2500                 |   Desconto de 20%

Observação: as mensagens exibidas para o usuário deverão ser exatamente como apresentado abaixo
(mensagens exibidas com os comandos input() e print()).

Exemplo de execução 1 do programa:
Digite o valor da hora de trabalho: 16.0
Digite a quantidade de horas trabalhadas no mês: 160
Salário Bruto: R$ 2560.00
IR: R$ 512.00
INSS: R$ 256.00
FGTS: R$ 281.60
Total de descontos: R$ 768.00
Salário líquido: R$ 1792.00

Exemplo de execução 2 do programa:
Digite o valor da hora de trabalho: 7.5
Digite a quantidade de horas trabalhadas no mês: 120
Salário Bruto: R$ 900.00
IR: R$ 0.00
INSS: R$ 90.00
FGTS: R$ 99.00
Total de descontos: R$ 90.00
3
Salário líquido: R$ 810.00
'''

valor_hora = float(input('Digite o valor da hora de trabalho: '))
qtde_hora = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora * qtde_hora
print(f'Salário Bruto: R$ {round(salario_bruto,1)}0')

ir = 0.0
if  round(salario_bruto,0) <= 900:
    print(f'IR: R$ {ir}0')
elif round(salario_bruto,0) > 900 and round(salario_bruto,0) <= 1500:
    ir = ((5 * salario_bruto)/100)
    print(f'IR: R$ {ir}0')
elif round(salario_bruto,0) > 1500 and round(salario_bruto,0) <= 2500:
    ir = ((10 * salario_bruto)/100)
    print(f'IR: R$ {ir}0')
else:   
    ir = ((20 * salario_bruto)/100)
    print(f'IR: R$ {ir}0')

inss = ((10*salario_bruto)/100)
print(f'INSS: R$ {inss}0')
print(f'FGTS: R$ {((11*salario_bruto)/100)}0')

print(f'Total de descontos: R$ {ir+inss}0')
print(f'Salário líquido: R$ {salario_bruto - (ir+inss)}0')