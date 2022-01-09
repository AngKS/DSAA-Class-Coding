from Pokemon import Pokemon

class Pikachu(Pokemon):  # 'is a' relationship, Pikachu is a Pokemon
    def __init__(self, height, weight, gender, cp=100):
        # have access to whatever the parent has
        super().__init__(height, weight, gender, cp)

    def cry(self):
        print("PIKKAAAA")

    def printMe(self):  # override the behavior of the print function
        super().printMe()
        print(f'Type: {self.__type}')
