from datetime import datetime
import uuid

class Entity:
  def __init__(self,  created_by: str | None = None, id: str | None = None) -> None:
    self.id = id or str(uuid.uuid4())
    self.created_at = datetime.now()
    self.created_by = created_by

    self.updated_at = datetime.now()
    self.updated_by = created_by

    self.deleted_at: datetime | None = None
    self.deleted_by: str | None = None

  def soft_delete(self, by: str) -> None:
    self.deleted_at = datetime.now()
    self.deleted_by = by
    self.touch(by)

  def touch(self, updated_by: str | None = None) -> None:
    self.updated_at = datetime.now()
    self.updated_by = updated_by or self.created_by