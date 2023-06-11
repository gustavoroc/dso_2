from Model.Animal.IAnimal import Animal


class Dog(Animal):
    def __init__(self, chip_number: int, name: str, breed: str, vaccine_history, available: bool, size: str):
        super().__init__(chip_number, name, breed, vaccine_history, available)

        self.__size = size

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    def __str__(self):
        return f"Chip Number: {self.chip_number}\nName: {self.name}\nBreed: {self.breed}\nVaccine History: {self.vaccine_history}\nAvailable: {self.available}\nSize: {self.size}"
