from __future__ import annotations

import uuid

from src.entities.order.order import Order
from src.entities.order.order_item import OrderItem


class Customer:
    def __init__(self, name: str, id: str | None = None) -> None:
        self.id = id or str(uuid.uuid4())
        self.name = name

    def place_order(self, items: list[OrderItem]) -> Order:
        return Order(customer_id=self.id, items=items)
