class Wojownik:
    def __init__(self):
        self.experience = 0

    def __repr__(self):
        return f'{self.__class__.__name__}: hp={self.life}, exp={self.experience}'

    def maszeruj(self, dystans):
        print(f'Wojownik: Przeszedłem {dystans}m')
        self.experience += 0.02 * dystans
