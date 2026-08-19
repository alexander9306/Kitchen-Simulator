from src.entities.entity.entity import Entity

class Chef(Entity):
  def __init__(self, created_by:str, name:str, experience: float):
    super().__init__(created_by)

    self.name = name
    self.experience = experience