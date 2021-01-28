salario = float(input('Informe o seu salário atual: '))
aumento = float(input('Informe a porcentagem de aumento que você deseja: '))
resultado = salario + (salario * (aumento / 100))
print(f'O valor do salário atualizado é: {resultado:,.2f}')