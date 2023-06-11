from datetime import date


class Adopter:
    def __init__(self, cpf: int, name: str, dob: date, address: str, habitation_type: str, has_other_animals: bool, responsability_term_id: list[int] = []):
        self.__cpf = cpf
        self.__name = name
        self.__dob = dob
        self.__address = address
        self.__habitation_type = habitation_type
        self.__has_other_animals = has_other_animals
        self.__responsability_term_id = responsability_term_id

    @property
    def cpf(self) -> int:
        return self.__cpf

    @property
    def name(self) -> str:
        return self.__name

    @property
    def dob(self) -> date:
        return self.__dob

    @property
    def address(self) -> str:
        return self.__address

    @property
    def habitation_type(self) -> str:
        return self.__habitation_type

    @property
    def has_other_animals(self) -> bool:
        return self.__has_other_animals

    @property
    def responsability_term_id(self) -> list[int]:
        return self.__responsability_term_id

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @name.setter
    def name(self, name: str):
        self.__name = name

    @dob.setter
    def dob(self, dob: date):
        self.__dob = dob

    @address.setter
    def address(self, address: str):
        self.__address = address

    @habitation_type.setter
    def habitation_type(self, habitation_type: str):
        self.__habitation_type = habitation_type

    @has_other_animals.setter
    def has_other_animals(self, has_other_animals: bool):
        self.__has_other_animals = has_other_animals

    @responsability_term_id.setter
    def responsability_term_id(self, responsability_term_id: list[int]):
        self.__responsability_term_id = responsability_term_id

    def __str__(self):
        return f"CPF: {self.cpf}\nName: {self.name}\nDate of birth: {self.dob}\nAddress: {self.address}\nHabitation type: {self.habitation_type}\nHas other animals: {self.has_other_animals}\nResponsability term ID: {self.responsability_term_id}"
