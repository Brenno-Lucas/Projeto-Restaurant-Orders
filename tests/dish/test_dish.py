from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("bigmac", "43")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("bigmac", -43)
    test_1 = Dish("lanche", 25.00)
    test_2 = Dish("pizza", 60.00)
    assert test_1.name == "lanche"
    assert test_1.__hash__() != test_2.__hash__()
    assert test_1.__hash__() == test_1.__hash__()
    assert (test_1 == test_1) is True
    assert (test_1 == test_2) is False
    assert test_1.__repr__() == "Dish('lanche', R$25.00)"
    test_1.add_ingredient_dependency(Ingredient("carne"), 3)
    assert test_1.get_ingredients() == {Ingredient('carne')}
    assert test_1.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
