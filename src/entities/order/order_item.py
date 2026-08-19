from __future__ import annotations

from src.entities.entity.entity import Entity
from src.entities.product.product import Product

class OrderItem(Entity):
    def __init__(self, product: Product, quantity: int, created_by: str, notes: str = "") -> None:
        super().__init__(created_by=created_by)

        self.product = product
        self.quantity = quantity
        self.notes = notes
