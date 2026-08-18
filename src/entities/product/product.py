from src.entities.entity.entity import Entity

class Product (Entity):
  def __init__(self, name: str, difficulty: float, created_by: str):
    super().__init__(created_by=created_by)

    self.name = name
    self.difficulty = difficulty