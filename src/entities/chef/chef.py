from src.entities.entity.entity import Entity

class Chef(Entity):
    def __init__(self, name: str, experience: float, created_by: str ) -> None:
        super().__init__(created_by=created_by)

        self.name = name
        self.experience = experience
