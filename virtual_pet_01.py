class Menu:
    def __init__(self):
        print('Selecione abaixo o que você deseja fazer:')
        self.menu = input('Comer, Acordar, Dormir ou Sair? ').lower()


class VirtualPet:
    def __init__(self):
        self.status = 'acordado'

    def feed(self):
        if self.status == 'dormindo':
            self.status = 'acordado'
        self.food = input('Com o que deseja alimenta-lo? ')
        print('Comendo {alimento}...\n'.format(alimento=self.food))

    def wakeup(self):
        if self.status == 'dormindo':
            self.status = 'acordado'
            print('Acordei!\n')
        else:
            print('Já estou acordado\n')

    def sleep(self):
        if self.status == 'acordado':
            self.status = 'dormindo'
            print('ZzzzZzzzZ\n')
        else:
            self.status = 'acordado'
            print('Você me acordou!\n')


pet = VirtualPet()

print('\nSeja bem vindo!\n')

while True:

    m = Menu()

    if m.menu == 'comer':
        pet.feed()
    elif m.menu == 'acordar':
        pet.wakeup()
    elif m.menu == 'dormir':
        pet.sleep()
    elif m.menu == 'sair':
        print('Te vejo depois!')
        break
