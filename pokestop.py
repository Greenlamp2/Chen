class Pokestop:
    def __init__(self, name=None, lat=None, long=None):
        self.name = name
        self.lat = lat
        self.long = long

    @property
    def maps(self):
        return 'https://www.google.com/maps/@%s,%sz' % (self.lat, self.long)

    @property
    def itineraire(self):
        # return 'https://www.google.com/maps/dir/%s,%s/@%s,%sz' % (self.lat, self.long, self.lat, self.long)
        return 'https://www.google.com/maps/search/?api=1&query=%s,%s' % (self.lat, self.long)
