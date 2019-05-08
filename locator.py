import csv

from pokestop import Pokestop
from pokestops_handler import PokestopsHandler


class Locator:
    def __init__(self):
        self.pokestops = PokestopsHandler()
        self.load()

    def load(self):
        with open('export.csv', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                pokestop = Pokestop(row[0], row[1], row[2])
                self.pokestops.add(pokestop)

    def get_position(self, name):
        return self.pokestops.get_position(name)


def main():
    locator = Locator()

    pk = locator.get_position('waterless')
    print(pk.itineraire)



if __name__ == '__main__':
    main()
