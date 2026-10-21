from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    SEARCHING_FOR_INGREDIENTS = "searching_for_ingredients"
    IN_PREPARATION = "in_preparation"
    COMPLETED = "completed"


