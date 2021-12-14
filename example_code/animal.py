
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return self._complicated_private_method()

    def move(self, distance):
        self.other_complicated_private_method(distance)

    def _complicated_private_method(self):
        return 'foo'

    def other_complicated_private_method(self, distance):
        pass