import random

class Player:
    """Gracz w strzelance."""
    # def die(self):
    #     print('Wróg wygrywa. Bohater pada w kałuży krwi.')
    def die(self):
        print('Wróg wygrywa. Wróg rozszarpuje bohatera i pozostawia go w kałuży krwi.')

    def blast(self, enemy):
        shoot = random.randrange(1, 10)
        if shoot >= 3:
            print('Gracz razi wroga.\n')
            enemy.die()
            print('Wróg wygrywa. Bohater pada w kałuży krwi.')
        else:
            hero.die()

class Alien:
    """Obcy w strzelance."""
    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')

if __name__ == '__main__':
    print('************** Śmierć Obcego **************\n')
hero = Player()
invader = Alien()
hero.blast(invader)
input('\n\nAby zakończyć program, naciśnij klawisz Enter.')