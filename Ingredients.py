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
        self.allingredient = []
        
    def add_ingredient(self, onceingredient):
        for i in self.allingredient:
            if i == onceingredient:
                i.quantity += onceingredient.quantity
                return
        self.allingredient.append(onceingredient)

    def is_valid_ratio(ratio: float):
        try:
            return ratio > 0
        except:
            return False
        
    def 
        


        
        
        
    