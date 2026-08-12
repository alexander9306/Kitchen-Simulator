class OrderItem:
    def __init__(self, product_id: str, quantity: int, notes: str = "") -> None:
        self.product_id = product_id
        self.quantity = quantity
        self.notes = notes
