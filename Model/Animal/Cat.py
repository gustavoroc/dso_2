from Model.Animal.IAnimal import Animal


class Cat(Animal):
    def __init__(self, chip_number: int, name: str, breed: str, vaccine_history, available: bool):
        super().__init__(chip_number, name, breed, vaccine_history, available)

    def __str__(self):
        return f"Chip Number: {self.chip_number}\nName: {self.name}\nBreed: {self.breed}\nVaccine History: {self.vaccine_history}\nAvailable: {self.available}"
