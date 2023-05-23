from src.models.ingredient import (Ingredient, Restriction)


def test_ingredient():
    test_1 = Ingredient("ovo")
    test_2 = Ingredient("frango")
    test_3 = Ingredient("ovo")

    assert test_1.name == "ovo"
    assert hash(test_1) == hash(test_3)
    assert hash(test_1) != hash(test_2)
    assert test_1.__eq__(test_3) is True
    assert test_1.__eq__(test_2) is False
    assert repr(test_1) == "Ingredient('ovo')"
    assert test_1.restrictions == {
        Restriction.ANIMAL_DERIVED,
    }
