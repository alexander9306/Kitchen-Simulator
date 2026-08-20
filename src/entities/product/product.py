from src.entities.entity.entity import Entity
from datetime import datetime

class Product (Entity):
  def __init__(
    self,
    id: int,
    created_by: str,
    created_at: datetime,
    name: str,
    difficulty: float
  ):
    super().__init__(created_by=created_by, id=id, created_at=created_at)

    self.name = name
    self.difficulty = difficulty
