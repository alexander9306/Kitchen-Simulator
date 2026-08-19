from src.entities.entity.entity import Entity

class PreparationStep (Entity):
  def __init__(self, name: str, stepTime: float, created_by: str):
    super().__init__(created_by=created_by)

    self.name = name
    self.stepTime = stepTime