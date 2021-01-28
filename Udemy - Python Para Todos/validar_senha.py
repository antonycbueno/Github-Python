usuario = 'antony'
senha = 'antonyemilene'

usuario_informado = input('Informe o usuário: ')
senha_informada = input('Informe a senha: ')

if (usuario == usuario_informado and
    senha == senha_informada):
    print('Acesso autorizado!')
else:
    print('Acesso negado.')