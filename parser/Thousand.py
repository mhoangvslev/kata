from parser.Cent import Cent
from parser.Lexeme import Lexeme
from parser.Ten import Ten
from parser.Unit import Unit

class Thousand(Lexeme):
    def __init__(self, number: int, power_of_thousand: int):
        super().__init__(number)
        self._cent = Cent(number)
        self.__power_of_thousand = power_of_thousand
        self.__thousands = ["", "mille", "million", "milliard", "billion", "billiard"]

        number_length = len(str(number))
        if number_length == 1:
            self.__cent = Unit(number)
        elif number_length == 2:
            self.__cent = Ten(number)
        else:
            self.__cent = Cent(number)

    def __str__(self):
        cent_part = str(self.__cent)
        thousand_part = self.__thousands[self.__power_of_thousand]
        
        if self.__cent._number == 0:
            return ""
        elif self.__cent._number == 1 and self.__power_of_thousand == 1:
            return thousand_part
        elif self.__power_of_thousand > 0:
            if self.__cent._number > 1:
                thousand_part += "s"
        
        return f"{str(self.__cent)}" if self.__power_of_thousand == 0 else f"{str(self.__cent)} {thousand_part}"
        