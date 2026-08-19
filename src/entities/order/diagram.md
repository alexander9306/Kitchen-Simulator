# Order context

What a customer asked for, and how far along it is. `Order` is the entity that
guards its own status and item list.

```mermaid
classDiagram
    class Order {
        +String id
        +Customer customer
        +Chef chef
        +List~OrderItem~ items
        +OrderStatus status
        +DateTime estimated_ready_at
        +DateTime created_at
        +String created_by
        +set_chef(chef: Chef, updated_by: String) void
        +add_item(item: OrderItem, updated_by: String) void
        +update_status(status: OrderStatus, updated_by: String) void
        +take_order(taken_by: String) void
        +search_for_ingredients(search_by: String) void
    }

    class OrderItem {
        +String id
        +Product product
        +int quantity
        +String notes
    }

    class OrderStatus {
        <<enumeration>>
        PENDING
        SEARCHING_FOR_INGREDIENTS
        IN_PREPARATION
        COMPLETED
    }

    class Entity {
        <<external>>
    }
    class Customer {
        <<external>>
    }
    class Chef {
        <<external>>
    }
    class Product {
        <<external>>
    }

    Entity <|-- Order
    Entity <|-- OrderItem
    Order "1" *-- "1..*" OrderItem : contiene
    Order "1" --> "1" OrderStatus : tiene
    OrderItem "0..*" --> "1" Product : referencia
    Customer "1" --> "0..*" Order : crea
    Chef "1" --> "0..*" Order : prepara
```

## Design notes

**Order holds object references, not foreign keys.** `customer` and `chef` are
`Customer` and `Chef` instances rather than `customerId` / `chefId` strings

`*--` to `OrderItem` is composition: an order item has no life of its own once
its order is gone. `-->` to `Customer` is a plain association — customers outlive
orders.