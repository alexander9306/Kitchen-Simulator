from __future__ import annotations

from src.entities.order.order import Order


class KitchenQueue:
    def __init__(self) -> None:
        self.__orders: list[Order] = []

    def add_order(self, order: Order) -> None:
        self.__orders.append(order)

    def get_next_order(self) -> Order | None:
        return self.__orders[0] if self.__orders else None

    def remove_order(self, order_id: str) -> None:
        self.__orders = [order for order in self.__orders if order.id != order_id]

