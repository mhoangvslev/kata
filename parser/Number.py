from parser.Lexeme import Lexeme
from parser.Thousand import Thousand


class Number(Lexeme):
    def __init__(self, number: int):
        super().__init__(number)
        
        # Split the string into groups of thousands
        self._thousands = []
        number_str = str(number)[::-1]
        for i in range(0, len(number_str), 3):
            lexeme = number_str[i:i+3][::-1]
            ##printlexeme, len(self._thousands))
            number = Thousand(
                number=int(lexeme), 
                power_of_thousand=len(self._thousands)
            )
            self._thousands.append(number)

    def __str__(self):
        return " ".join([str(thousand) for thousand in self._thousands[::-1]])

    