from parser.Number import Number


def test():
    """
    Test number conversion of increasing digits count
    """

    digit_1 = Number(5)
    assert str(digit_1) == "cinq"

    digit_2_1 = Number(15)
    assert str(digit_2_1) == "quinze"

    digit_2_2 = Number(17)
    assert str(digit_2_2) == "dix-sept"

    digit_2_3 = Number(41)
    assert str(digit_2_3) == "quarante-et-un"

    digit_2_4 = Number(91)
    assert str(digit_2_4) == "quatre-vingt-onze"

    digit_2_5 = Number(68)
    assert str(digit_2_5) == "soixante-huit"

    digit_3_1 = Number(100)
    assert str(digit_3_1) == "cent"

    digit_3_2 = Number(201)
    assert str(digit_3_2) == "deux cents un"

    digit_3_3 = Number(999)
    assert str(digit_3_3) == "neuf cents quatre-vingt-dix-neuf"

    digit_4_1 = Number(1337)
    assert str(digit_4_1) == "mille trois cents trente-sept"

    digit_4_2 = Number(2041)
    assert str(digit_4_2) == "deux milles quarante-et-un"

    digit_4_3 = Number(5468)
    assert str(digit_4_3) == "cinq milles quatre cents soixante-huit"

    digit_5_1 = Number(10345)
    assert str(digit_5_1) == "dix milles trois cents quarante-cinq"

    digit_5_2 = Number(24387)
    assert str(digit_5_2) == "vingt-quatre milles trois cents quatre-vingt-sept"

    digit_6_1 = Number(376981)
    assert str(digit_6_1) == "trois cents soixante-seize milles neuf cents quatre-vingt-un"

    digit_6_2 = Number(237892)
    assert str(digit_6_2) == "deux cents trente-sept milles huit cents quatre-vingt-douze"

    digit_7_1 = Number(1137568)
    assert str(digit_7_1) == "un million cent trente-sept milles cinq cents soixante-huit"

if __name__ == "__main__":
    test()