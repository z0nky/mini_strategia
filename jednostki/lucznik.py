from wojownik import Wojownik


class Lucznik(Wojownik):
    def __init__(self):
        super().__init__()
        self.life = 40
        self.arrows = 10

    def maszeruj(self, dystans):
        self.experience += (dystans * 0.2)
        print(f"Łucznik: przeszedłem {dystans} m.")

    def atakuj(self):
        if self.arrows > 0:
            self.experience += 0.4
            print("Łucznik: wypuściłem strzałę!")
        else:
            print("Łucznik: Nie mam już strzał!")
