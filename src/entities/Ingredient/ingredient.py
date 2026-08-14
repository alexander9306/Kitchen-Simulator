import uuid

class Ingredient:
  def __init__(self, name: str, quantityInStock: int, id: str | None = None):
    self.id = id or str(uuid.uuid4())
    self.name = name
    self.quantityInStock = quantityInStock
