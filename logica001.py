#**Problema -1)**
#Você recebeu seu salário mínimo e fez um depósito na sua conta, que está a mingua, sem nenhum tustão. Ao receber o salário, fez imediatamente os dois pagamamentos que devia na praça. Fazendo esses dois pagamentos com cheques distintos, você foi taxado pelo ICMS do banco. Com base no seu salário, nas suas duas dívidas e na taxação do seu banco, calcule qual o valor do saldo final da sua conta ao realizar todos os pagamentos.

salario = float(input('Digite seu salário: '))
cheque1= float(input('Digite o valor da primeira dívida: '))
cheque2= float(input('Digite o valor da segunda dívida: '))

taxa = float(input('Digite a taxa ICMS do seu banco: '))

saldo1 = salario - (cheque1 + cheque1*taxa)
saldoFinal = saldo1 - (cheque2 + cheque2*taxa)

print(f'O seu saldo final é de: {saldoFinal}')