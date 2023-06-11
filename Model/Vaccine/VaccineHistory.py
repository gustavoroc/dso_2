from datetime import date

from Model.Vaccine.Vaccine import Vaccine


class VaccineHistory:
    def __init__(self, updated_in: date, last_updated_vaccine: Vaccine, vaccines: list[Vaccine], animal_chip_number: int):
        self.__updated_in = updated_in
        self.__last_updated_vaccine = last_updated_vaccine
        self.__vaccines = vaccines
        self.__animal_chip_number = animal_chip_number

    @property
    def updated_in(self) -> date:
        return self.__updated_in

    @updated_in.setter
    def updated_in(self, updated_in: date):
        self.__updated_in = updated_in

    @property
    def last_updated_vaccine(self) -> Vaccine:
        return self.__last_updated_vaccine

    @last_updated_vaccine.setter
    def last_updated_vaccine(self, last_updated_vaccine: Vaccine):
        self.__last_updated_vaccine = last_updated_vaccine

    @property
    def vaccines(self) -> list[Vaccine]:
        return self.__vaccines

    @vaccines.setter
    def vaccines(self, vaccines: list[Vaccine]):
        self.__vaccines = vaccines

    @property
    def animal_chip_number(self) -> int:
        return self.__animal_chip_number

    @animal_chip_number.setter
    def animal_chip_number(self, animal_chip_number: int):
        self.__animal_chip_number = animal_chip_number

    def __str__(self) -> str:
        return f"Updated In: {self.updated_in}\nLast Updated Vaccine: {self.last_updated_vaccine}\nVaccines: {self.vaccines}\nAnimal Chip Number: {self.animal_chip_number}"
