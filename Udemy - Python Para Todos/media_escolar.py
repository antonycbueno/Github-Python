nome = input('Inform o nome do aluno: ')
n1 = float(input('Informa a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))
n4 = float(input('Informe a quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4

if media < 5:
    resultado = 'reprovado'
elif media >= 5:
    resultado = 'recuperação'
else:
    resultado = 'aprovado'

print(f'O aluno {nome} está {resultado}.\n'
      f'Sua média foi {media}.')