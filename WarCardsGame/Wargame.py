
import karty
import gry


class WarCard(karty.Card):
    """ Karta. """

    @property
    def value(self):
        if self.is_face_up:
            v = WarCard.RANKS.index(self.rank) + 2
        else:
            v = None
        return v


class WarDeck(karty.Deck):
    """ Talia kart. """
    def populate(self):
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                self.cards.append(WarCard(rank, suit))


class WarHand(karty.Hand):
    """ Ręka. """
    def __init__(self, name):
        super(WarHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(WarHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # jeśli karta w ręce ma wartość None, to i wartość wynosi None
        for card in self.cards:
            if not card.value:
                return None

        # zsumuj wartości kart
        t = 0
        for card in self.cards:
            t += card.value
        return t


class WarPlayer(WarHand):
    """ Gracz. """

    def lose(self):
        print(self.name, "przegrywa.")

    def win(self):
        print(self.name, "wygrywa.")

    def push(self):
        print(self.name, "remisuje.")


class WarGame(object):
    """ Gra. """
    def __init__(self, names):

        self.players = []
        for name in names:
            player = WarPlayer(name)
            self.players.append(player)

        # self.dealer = WarDealer("Rozdający")
        self.deck = WarDeck()
        self.deck.populate()
        self.deck.shuffle()


    def prepare(self):
        self.deck.clear()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        # rozdaj każdemu początkowe dwie karty
        self.deck.deal(self.players, per_hand=1)
        for player in self.players:
            print(player)
        # print(self.dealer)

        for player in self.players:
            if player.total > self.players.total:
                player.win()
            if player.total < self.players.total:
                player.lose()
            else:
                player.push()


        # usuń karty wszystkich graczy
        for player in self.players:
            player.clear()
        # self.dealer.clear()


def main():
    print("Welcome to War Cards Game!\n")

    names = []
    number = gry.ask_number("Give number of players (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Gamer's Name: ")
        names.append(name)
    print()

    game = WarGame(names)

    again = None
    while again != "n":
        game.prepare()
        game.play()
        again = gry.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nTo end press the key Enter.")



