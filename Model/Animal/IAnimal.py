from abc import ABC

from Model.Vaccine.VaccineHistory import VaccineHistory


class Animal(ABC):
    def __init__(self, chip_number: int, name: str, breed: str, vaccine_history: VaccineHistory, available: bool):
        self.__chip_number = chip_number
        self.__name = name
        self.__breed = breed
        self.__vaccine_history = vaccine_history
        self.__available = available

    @property
    def chip_number(self) -> int:
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, chip_number: int):
        self.__chip_number = chip_number

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def breed(self) -> str:
        return self.__breed

    @breed.setter
    def breed(self, breed: str):
        self.__breed = breed

    @property
    def vaccine_history(self) -> VaccineHistory:
        return self.__vaccine_history

    @vaccine_history.setter
    def vaccine_history(self, vaccine_history: VaccineHistory):
        self.__vaccine_history = vaccine_history

    @property
    def available(self) -> bool:
        return self.__available

    @available.setter
    def available(self, available: bool):
        self.__available = available

    def __str__(self):
        return f"Chip Number: {self.chip_number}\nName: {self.name}\nBreed: {self.breed}\nVaccine History: {self.vaccine_history}\nAvailable: {self.available}"
