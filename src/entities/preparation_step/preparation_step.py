from __future__ import annotations
from src.entities.entity.entity import Entity
from datetime import datetime

class PreparationStep (Entity):
  def __init__(
    self,
    id: int,
    created_by: str,
    created_at: datetime,
    name: str,
    step_time: float,
    depend_on: list[PreparationStep] | None = None
  ):
    super().__init__(created_by=created_by, id=id, created_at=created_at)

    self.name = name
    self.step_time = step_time
    self.depend_on = depend_on