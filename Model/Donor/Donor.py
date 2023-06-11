from datetime import date
from Model.Animal.IAnimal import Animal

from Model.Donor.DonorRegister import DonorRegister


class Donor:
    def __init__(self, cpf: str, name: str, dob: date, address: str, id: int,  date_of_donation: date, donated_animal: Animal, donor_reason: str, donor_cpf: int):
        self.__cpf = cpf
        self.__name = name
        self.__dob = dob
        self.__address = address
        self.__donation_register = DonorRegister(
            date_of_donation, donated_animal, donor_reason, donor_cpf)

    @property
    def cpf(self) -> str:
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
    def donation_register(self) -> DonorRegister:
        return self.__donation_register

    @cpf.setter
    def cpf(self, cpf: str):
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

    @donation_register.setter
    def donation_register(self, donation_register: DonorRegister):
        self.__donation_register = donation_register

    def __str__(self):
        return f"CPF: {self.cpf}\nName: {self.name}\nDate of birth: {self.dob}\nAddress: {self.address}\nDonation register: {self.donation_register}"
