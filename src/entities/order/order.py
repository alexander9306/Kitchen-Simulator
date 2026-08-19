from __future__ import annotations

from datetime import datetime

from src.entities.order.order_item import OrderItem
from src.entities.order.order_status import OrderStatus
from src.entities.entity.entity import Entity
from src.entities.chef.chef import Chef
from src.entities.customer.customer import Customer

class Order(Entity):
    def __init__(
        self,
        created_by: str,
        customer: Customer,
        chef: Chef | None = None,
        items: list[OrderItem] | None = None,
    ) -> None:
        super().__init__(created_by=created_by)

        self.customer = customer
        self.chef = chef
        self.items: list[OrderItem] = items or []
        self.status = OrderStatus.PENDING
        self.estimated_ready_at: datetime | None = None

    def set_chef(self, chef: Chef, updated_by: str) -> None:
        self.touch(updated_by=updated_by)
        self.chef = chef

    def add_item(self, item: OrderItem, updated_by: str) -> None:
        self.touch(updated_by=updated_by)
        self.items.append(item)

    def update_status(self, status: OrderStatus, updated_by: str) -> None:
        self.touch(updated_by=updated_by)
        self.status = status

    def take_order(self, taken_by: str) -> None:
        self.update_status(OrderStatus.IN_PREPARATION, updated_by=taken_by)

    def search_for_ingredients(self, search_by: str) -> None:
        self.update_status(OrderStatus.SEARCHING_FOR_INGREDIENTS, updated_by=search_by)

