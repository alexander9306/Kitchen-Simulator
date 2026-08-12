from __future__ import annotations

import uuid

from src.entities.order.order_status import OrderStatus
from src.entities.order.order import Order


class Chef:
    def __init__(self, name: str, experience: float, id: str | None = None) -> None:
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.experience = experience

    def take_order(self, order: "Order") -> None:
        order.chef_id = self.id
        order.update_status(OrderStatus.IN_PREPARATION)

    def search_for_ingredients(self, order: "Order") -> None:
        order.update_status(OrderStatus.SEARCHING_FOR_INGREDIENTS)

