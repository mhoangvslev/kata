from parser.Lexeme import Lexeme
from parser.Unit import Unit


class Ten(Lexeme):
    def __init__(self, number: int):
        super().__init__(number)
        self.__tens = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]
        if self._number == 0:
            self.__unit = Unit(0)
        elif self._number > 0 and self._number <= 16:
            self.__unit = Unit(number)
        else:
            self.__ten = Unit(number // 10) 
            if self.__ten._number == 7 or self.__ten._number == 9:
                self.__unit = Ten((number % 10) + 10)
            else:
                self.__unit = Ten(number % 10)

    def __str__(self) -> str:
        if self._number == 0:
            return ""
        elif self._number <= 16:
            return str(self.__unit)
        # If the digit is zero, return the corresponding tens
        elif self.__unit._number == 0:
            return f"{str(self.__tens[self.__ten._number])}"
        elif self.__unit._number == 1 and self.__ten._number != 8: # quatre-vingt-un et non quatre-vingt-et-un, bizarre
            return f"{str(self.__tens[self.__ten._number])}-et-{str(self.__unit)}"
        else:
            return f"{str(self.__tens[self.__ten._number])}-{str(self.__unit)}"
