from src.entities.entity.entity import Entity

class Customer(Entity):
    def __init__(self, name: str, created_by: str) -> None:
        super().__init__(created_by=created_by)

        self.name = name
