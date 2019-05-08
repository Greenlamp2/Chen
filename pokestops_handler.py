class PokestopsHandler:
    def __init__(self):
        self.pokestops = []

    def add(self, pokestop):
        self.pokestops.append(pokestop)

    def get_position(self, name):
        for pokestop in self.pokestops:
            if name.upper() in pokestop.name.upper():
                return pokestop

        return None
