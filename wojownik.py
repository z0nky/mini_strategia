class Wojownik:
    def __init__(self, life):
        self.experience = 0
        self.life = life

    def __repr__(self):
        try:
            assert self.life > 0
            return f'{self.__class__.__name__}: hp={self.life}, exp={self.experience}'
        except AssertionError:
            return "Should be positive"

    def maszeruj(self, dystans):
        print(f'Wojownik: Przeszedłem {dystans}m')
        self.experience += 0.02 * dystans

    # def exception_life(self):
    #     try:
    #         assert self.life > 0
    #     except AssertionError:
    #         print("Should be positive")