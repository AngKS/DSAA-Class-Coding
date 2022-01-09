class Pokemon:  # generic pokemon
    def __init__(self, height, weight, gender, cp=100):
        self.__height = height
        self.__weight = weight
        self.__gender = gender
        self.__type = ''  # unknown type for now
        self.__cp = cp

    def cry(self):
        # Method overriding to enforce child classes to implement the abstract functions
        raise NotImplementedError(
            "Subclass must be implemented for abstract functions")

    def __str__(self):
        return f"Height: {self.__height}\tWeight: {self.__weight}\tGender: {self.__gender}\tCP: {self.__cp}"

    def printMe(self):
        print(f'Height: {self.__height}')
        print(f'Weight: {self.__weight}')
        print(f'Gender: {self.__gender}')
        print(f'CP: {self.__cp}')
        # print(f'Type: {self.__type}')
