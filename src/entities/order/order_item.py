from __future__ import annotations

from datetime import datetime

from src.entities.entity.entity import Entity
from src.entities.product.product import Product

class OrderItem(Entity):
    def __init__(self, id: int, created_by: str, created_at: datetime, product: Product, quantity: int, notes: str = "") -> None:
        super().__init__(created_by=created_by, id=id, created_at=created_at)

        self.product = product
        self.quantity = quantity
        self.notes = notes
