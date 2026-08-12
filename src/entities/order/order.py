from __future__ import annotations

import uuid
from datetime import datetime


from src.entities.order.order_item import OrderItem
from src.entities.order.order_status import OrderStatus


class Order:
    def __init__(
        self,
        customer_id: str,
        items: list[OrderItem] | None = None,
        id: list[str] | None = None,
    ) -> None:
        self.id = id or str(uuid.uuid4())
        # this will be change for a customer if cx entity is created
        self.customer_id = customer_id
        self.items: list[OrderItem] = items or []
        self.status = OrderStatus.PENDING
        self.chef_id: str | None = None
        self.created_at = datetime.now()
        self.estimated_ready_at: datetime | None = None

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    def update_status(self, status: OrderStatus) -> None:
        self.status = status
