from datetime import date

from Model.Animal.IAnimal import Animal


class DonorRegister:
    def __init__(self, date_of_donation: date, donated_animal: Animal, donor_reason: str, donor_cpf: int):
        self.__date_of_donation = date_of_donation
        self.__donated_animal = donated_animal
        self.__donor_reason = donor_reason
        self.__donor_cpf = donor_cpf

    @property
    def date_of_donation(self) -> date:
        return self.__date_of_donation

    @property
    def donated_animal(self) -> Animal:
        return self.__donated_animal

    @property
    def donor_reason(self) -> str:
        return self.__donor_reason

    @property
    def donor_cpf(self) -> int:
        return self.__donor_cpf

    @date_of_donation.setter
    def date_of_donation(self, date_of_donation: date):
        self.__date_of_donation = date_of_donation

    @donated_animal.setter
    def donated_animal(self, donated_animal: Animal):
        self.__donated_animal = donated_animal

    @donor_reason.setter
    def donor_reason(self, donor_reason: str):
        self.__donor_reason = donor_reason

    @donor_cpf.setter
    def donor_cpf(self, donor_cpf: int):
        self.__donor_cpf = donor_cpf

    def __str__(self):
        return f"Date of donation: {self.date_of_donation}\nDonated animal: {self.donated_animal}\nDonor reason: {self.donor_reason}\nDonor CPF: {self.donor_cpf}"
