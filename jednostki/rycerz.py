from wojownik import Wojownik


class Rycerz(Wojownik):
    def __init__(self):
        super().__init__()
        self.life = 60

    def maszeruj(self, dystans):
        self.experience += (int(dystans) * 0.2)
        print(f"Rycerz: przeszedłem {dystans} m.")

    def atakuj(self):
        self.experience += 0.3
        print("Rycerz: machnąłem mieczem!")
