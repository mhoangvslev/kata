from parser.Lexeme import Lexeme
from parser.Ten import Ten
from parser.Unit import Unit

class Cent(Lexeme):
    def __init__(self, number: int):
        super().__init__(number)
        self.__cent = Unit(number//100)
        self.__ten = Ten(number%100)

    def __str__(self) -> str:
        #printf"cent = {self.__cent._number}, ten = {self.__ten._number}")
        cent_part = ""
        if self.__cent._number > 1:
            cent_part = f"{str(self.__cent)} cents"
        elif self.__cent._number == 1:
            cent_part = "cent"
        
        ten_part = ""
        if self.__ten._number > 0:
            ten_part = f" {str(self.__ten)}"
        return f"{cent_part}{ten_part}"
