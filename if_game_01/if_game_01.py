print('Bem vindo ao meu primeiro jogo!')
name = input('Qual é o seu nome? ')
age = int(input('Quantos anos você tem? '))

print('Olá,', name, 'você tem', age, 'anos.')

health = 10

if age >= 18:
    print('Você tem idade suficiente para jogar.')

    wants_to_play = input('Você deseja jogar (Sim/Nao)? ').lower()
    if wants_to_play == 'sim':
        print('Você está iniciando com', health, 'de vida.')
        print('Bom jogo!')

        left_or_right = input('Faça sua escolha... Esquerda ou Direita? ').lower()
        if left_or_right == 'esquerda':
            ans = input('Boa, você seguiu o caminho e achou um lago. '
                        'Você deseja nadar ou dar a volta (nadar/retorno) ? ').lower()

            if ans == 'retorno':
                print('Você fez o retorno no lago e chegou ao outro lado.')

            elif ans == 'nadar':
                print('Você conseguiu atravesar mas foi mordido por um peixe e perdeu 5 de vida!')
                health -= 5
                print('Vida atual', health)

            ans = input('Você avistou uma casa e um rio. Para onde deseja seguir (rio/casa)? ').lower()
            if ans == 'casa':
                print('Você entrou na casa e foi agredido pelo dono... '
                      'Ele te acertou em cheio e você perdeu 5 de vida.')
                health -= 5

                if health <= 0:
                    print('Você chegou a 0 de vida, entrou em colapso e perdeu o jogo!')
                else:
                    print('Você sobrevviveu... Você vencêu o jogo!')

            else:
                print('Você caiu no rio e morreu.')

        else:
            print('Você caiu e perdeu!')

    else:
        print('Até depois...')

else:
    print('Você não tem idade suficiente para jogar!')
