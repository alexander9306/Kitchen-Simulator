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
        id: int,
        created_by: str,
        created_at: datetime,
        customer: Customer,
        chef: Chef | None = None,
        items: list[OrderItem] | None = None,

    ) -> None:
        super().__init__(created_by=created_by, id=id, created_at=created_at)

        self.customer = customer
        self.chef = chef
        self.items: list[OrderItem] = items or []
        self.status = OrderStatus.PENDING
        self.estimated_ready_at: datetime | None = None


    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    def update_status(self, status: OrderStatus) -> None:
        self.status = status

    def take_order(self) -> None:
        self.update_status(OrderStatus.IN_PREPARATION)

    def search_for_ingredients(self, search_by: str) -> None:
        self.update_status(OrderStatus.SEARCHING_FOR_INGREDIENTS)

