from parser.Lexeme import Lexeme


class Unit(Lexeme):
    def __init__(self, number: int):
        super().__init__(number)
        self.__units = ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"]

    def __str__(self) -> str:
        return self.__units[self._number]