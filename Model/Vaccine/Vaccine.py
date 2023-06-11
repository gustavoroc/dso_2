class Vaccine:
    def __init__(self, vaccine_name: str, id: int):
        self.__vaccine_name = vaccine_name
        self.__id = id

    @property
    def vaccine_name(self) -> str:
        return self.__vaccine_name

    @vaccine_name.setter
    def vaccine_name(self, vaccine_name: str):
        self.__vaccine_name = vaccine_name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    def __str__(self) -> str:
        return f"Vaccine Name: {self.vaccine_name}\nID: {self.id}"
