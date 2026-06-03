class Ingredient:
    def __init__(self,name: str, quantity: float,unit: str ):
        self.name = name
        self.unit = unit
        self._quantity = quantity
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self,data):
        if data<0: 
            raise ValueError("Количество должно быть положительным")
        self._quantity = data
        
    def __str__(self):
        return f"'{self.name}', {self._quantity}, '{self.unit}'"
    
    def __repr__(self):
        return f"Ingredient('{self.name}', {self._quantity}, '{self.unit}')"
    
    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit
    

class Recipe:
    def __init__(self,title: str, allingredient: list):
        self.title = title
        self.allingredient = allingredient
        
    def add_ingredient(self, onceingredient):
        for i in self.allingredient:
            if i == onceingredient:
                i.quantity += onceingredient.quantity
                return
        self.allingredient.append(onceingredient)

    @staticmethod
    def is_valid_ratio(ratio: float):
        try:
            return ratio > 0
        except:
            return False
        
    def scale(self,ratio: float):
        kopi_allingredient =[]
        for i in self.allingredient:
            kopi = i.quantity * ratio
            kopi_allingredient.append(kopi)
            
        return Recipe(self.title, kopi_allingredient)
    
    def __len__(self):
        return len(self.allingredient)
    
    def __str__(self):
        return f"{self.title}: {self.allingredient}"


class ShoppingList:
    def __init__(self,items: list):
        self._items = []
    
    def add_recipe(self,recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        mashtab_reciped = recipe.scale(portions)
        for i in mashtab_reciped.allingredient:
            self._items.append((i,recipe.title))
            
    def remove_recipe(self,title: str):
        self._items = [i for i in self._items if i[1] != title]
        
    def get_list(self):
        shopping_dict = {}
        for item in self._items:
            ingredient = item[0]
            key = (ingredient.name, ingredient.unit)
            if key in shopping_dict:
                shopping_dict[key] += ingredient.quantity
            else:
                shopping_dict[key] = ingredient.quantity
    
        result = []
        for (name, unit), quantity in shopping_dict.items():
            result.append(Ingredient(name, quantity, unit))
    
        result.sort(key=lambda x: x.name)
        return result
    
    def __add__(self,other):
        all_the_big_name_in_europe = ShoppingList()
        all_the_big_name_in_europe._items = self._items + other._items
        return all_the_big_name_in_europe
    
    
        
        
        
        
        

            
        
        
        
    
    



        
        
        
    