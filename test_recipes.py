import pytest
from Ingredients import Ingredient,Recipe, ShoppingList

class TestIngredient:
    
    def test_first(self):
        ing = Ingredient("сосиска", 500.0, "г")
        assert ing.name == "сосиска"
        assert ing.quantity == 500.0
        assert ing.unit == "г"

    def test_second(self):
        ing = Ingredient("сосиска", 500.0, "г")
        assert str(ing) == "'сосиска', 500.0, 'г'"

    def test_eq_first(self):
        ing1  = Ingredient("сосиска", 500.0, "г")
        ing2 = Ingredient("сосиска", 500.0, "г")
        assert ing1 == ing2

    def test_eq_second(self):
        ing1  = Ingredient("сосиска", 500.0, "г")
        ing2 = Ingredient("yabloko", 500.0, "г")
        assert ing1 != ing2

    def test_eq_third(self):
        ing1  = Ingredient("сосиска", 500.0, "t")
        ing2 = Ingredient("yabloko", 500.0, "г")
        assert ing1 != ing2
        
        
class TestRecipe:
    def test_recipe_creation(self):
        ing1 = Ingredient("хлеб", 500, "г")
        ing2 = Ingredient("масло", 3, "шт")
        recipe = Recipe("Блины", [ing1, ing2])
        assert recipe.title == "Блины"
        assert len(recipe.allingredient) == 2
    
    def test_add_ingredient_new(self):
        recipe = Recipe("Блины", [])
        ing = Ingredient("молоко", 500, "мл")
        recipe.add_ingredient(ing)
        assert len(recipe.allingredient) == 1
        assert recipe.allingredient[0] == ing
    
    def test_add_ingredient_existing(self):
        ing1 = Ingredient("молоко", 500, "мл")
        recipe = Recipe("Блины", [ing1])
        ing2 = Ingredient("молоко", 200, "мл")
        recipe.add_ingredient(ing2)
        assert len(recipe.allingredient) == 1
        assert recipe.allingredient[0].quantity == 700
    
    def test_scale_returns_new_recipe(self):
        ing = Ingredient("сыр", 500, "г")
        recipe = Recipe("Каша", [ing])
        scaled = recipe.scale(2)
        assert recipe != scaled
        assert recipe.allingredient[0].quantity == 500
    
    def test_scale_multiplies_quantity(self):
        ing1 = Ingredient("яйцо", 500, "г")
        ing2 = Ingredient("соль", 3, "г")
        recipe = Recipe("Торт", [ing1, ing2])
        scaled = recipe.scale(2)
        assert scaled.allingredient[0].quantity == 1000
        assert scaled.allingredient[1].quantity == 6
    
    def test_scale_invalid_ratio_zero(self):
        recipe = Recipe("Пирог", [Ingredient("сахар", 500, "г")])
        with pytest.raises(ValueError):
            recipe.scale(0)
    
    def test_scale_invalid_ratio_negative(self):
        recipe = Recipe("Суп", [Ingredient("вода", 500, "мл")])
        with pytest.raises(ValueError):
            recipe.scale(-2)
    
    def test_recipe_len(self):
        ing1 = Ingredient("помидор", 500, "г")
        ing2 = Ingredient("огурец", 3, "шт")
        recipe = Recipe("Салат", [ing1, ing2])
        assert len(recipe) == 2


class TestShoppingList:
    def test_add_recipe(self):
        ing = Ingredient("хлеб", 500, "г")
        recipe = Recipe("Завтрак", [ing])
        shopping = ShoppingList([])
        shopping.add_recipe(recipe, 1)
        assert len(shopping._items) == 1
        assert shopping._items[0][1] == "Завтрак"
    
    def test_add_recipe_invalid_portions_zero(self):
        recipe = Recipe("Блюдо", [Ingredient("колбаса", 500, "г")])
        shopping = ShoppingList([])
        with pytest.raises(ValueError):
            shopping.add_recipe(recipe, 0)
    
    def test_add_recipe_invalid_portions_negative(self):
        recipe = Recipe("Паста", [Ingredient("макароны", 500, "г")])
        shopping = ShoppingList([])
        with pytest.raises(ValueError):
            shopping.add_recipe(recipe, -1)
    
    def test_remove_recipe(self):
        ing1 = Ingredient("яйцо", 500, "шт")
        ing2 = Ingredient("сок", 200, "мл")
        recipe1 = Recipe("Омлет", [ing1])
        recipe2 = Recipe("Напиток", [ing2])
        shopping = ShoppingList([])
        shopping.add_recipe(recipe1, 1)
        shopping.add_recipe(recipe2, 1)
        shopping.remove_recipe("Омлет")
        assert len(shopping._items) == 1
        assert shopping._items[0][1] == "Напиток"
    
    def test_remove_recipe_nonexistent(self):
        recipe = Recipe("Хлеб", [Ingredient("мука", 500, "г")])
        shopping = ShoppingList([])
        shopping.add_recipe(recipe, 1)
        shopping.remove_recipe("Масло")
        assert len(shopping._items) == 1
    
    def test_get_list_combines_same_ingredients(self):
        ing1 = Ingredient("сахар", 500, "г")
        ing2 = Ingredient("сахар", 300, "г")
        recipe1 = Recipe("Десерт1", [ing1])
        recipe2 = Recipe("Десерт2", [ing2])
        shopping = ShoppingList([])
        shopping.add_recipe(recipe1, 1)
        shopping.add_recipe(recipe2, 1)
        result = shopping.get_list()
        assert len(result) == 1
        assert result[0].quantity == 800
    
    def test_get_list_sorted_by_name(self):
        ing1 = Ingredient("перец", 3, "г")
        ing2 = Ingredient("масло", 500, "мл")
        recipe = Recipe("Смесь", [ing1, ing2])
        shopping = ShoppingList([])
        shopping.add_recipe(recipe, 1)
        result = shopping.get_list()
        assert result[0].name == "масло"
        assert result[1].name == "перец"
    
    def test_add_shopping_lists(self):
        ing1 = Ingredient("мука", 500, "г")
        ing2 = Ingredient("молоко", 3, "л")
        recipe1 = Recipe("Блины", [ing1])
        recipe2 = Recipe("Каша", [ing2])
        shopping1 = ShoppingList([])
        shopping2 = ShoppingList([])
        shopping1.add_recipe(recipe1, 1)
        shopping2.add_recipe(recipe2, 1)
        shopping3 = shopping1 + shopping2
        assert len(shopping3._items) == 2
        assert len(shopping1._items) == 1
        assert len(shopping2._items) == 1
    
    
    
        
        
