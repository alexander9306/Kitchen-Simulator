from datetime import datetime

class Entity:
  def __init__(self,  created_by: str | None = None, id: int | None = None, created_at: datetime | None = None) -> None:
    self.id = id

    self.created_by = created_by
    self.created_at = created_at

    self.updated_by = created_by
    self.updated_at: datetime = created_at

    self.deleted_at: datetime | None = None
    self.deleted_by: str | None = None
