from datetime import date
from Model.Adopter.Adopter import Adopter

from Model.Animal.IAnimal import Animal


class ResponsabilityTerm:
    def __init__(self, date: date, animal: Animal, adopter: Adopter, signed: bool, id: int):
        self.__date = date
        self.__animal = animal
        self.__adopter = adopter
        self.__signed = signed
        self.__id = id

    @property
    def date(self) -> date:
        return self.__date

    @property
    def animal(self) -> Animal:
        return self.__animal

    @property
    def adopter(self) -> Adopter:
        return self.__adopter

    @property
    def signed(self) -> bool:
        return self.__signed

    @property
    def id(self) -> int:
        return self.__id

    @date.setter
    def date(self, date: date):
        self.__date = date

    @animal.setter
    def animal(self, animal: Animal):
        self.__animal = animal

    @adopter.setter
    def adopter(self, adopter: Adopter):
        self.__adopter = adopter

    @signed.setter
    def signed(self, signed: bool):
        self.__signed = signed

    @id.setter
    def id(self, id: int):
        self.__id = id

    def __str__(self):
        return f"Date: {self.date}\nAnimal: {self.animal}\nAdopter: {self.adopter}\nSigned: {self.signed}\nID: {self.id}"
