import pytest
from Ingredients import Ingredient,Recipe, ShoppingList

class Testgenerate:
    
    def first(self):
        ing = Ingredient("сосиска", 500.0, "г")
        assert ing.name == "мука"
        assert ing.quantity == 500.0
        assert ing.unit == "г"
        
    def second(self):
        ing = Ingredient("сосиска", 500.0, "г")
        assert str(ing) == "'сосиска', 500.0, 'г'"
        
    def eq_first(self):
        ing1  = Ingredient("сосиска", 500.0, "г")
        ing2 = Ingredient("сосиска", 500.0, "г")
        assert ing1 == ing2
        
    def eq_second(self):
        ing1  = Ingredient("сосиска", 500.0, "г")
        ing2 = Ingredient("yabloko", 500.0, "г")
        assert ing1 != ing2
        
    def eq_third(self):
        ing1  = Ingredient("сосиска", 500.0, "t")
        ing2 = Ingredient("yabloko", 500.0, "г")
        assert ing1 != ing2
        
    
        
        
