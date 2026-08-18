from src.entities.entity.entity import Entity

class Ingredient(Entity):
  def __init__(self, name: str, quantityInStock: int, created_by: str):
    super().__init__(created_by=created_by)

    self.name = name
    self.quantityInStock = quantityInStock
