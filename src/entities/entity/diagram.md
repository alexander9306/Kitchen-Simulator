# Entity (base) context

Shared base for every **entity** in the domain: identity plus audit trail
(who created / updated / soft-deleted it, and when).

```mermaid
classDiagram
    class Entity {
        +String id
        +DateTime created_at
        +String created_by
        +DateTime updated_at
        +String updated_by
        +DateTime deleted_at
        +String deleted_by
        +soft_delete(by: String) void
        +touch(updated_by: String) void
    }

    class Customer {
        <<external>>
    }
    class Order {
        <<external>>
    }
    class OrderItem {
        <<external>>
    }
    class Product {
        <<external>>
    }
    class PreparationStep {
        <<external>>
    }
    class Ingredient {
        <<external>>
    }

    Entity <|-- Customer
    Entity <|-- Order
    Entity <|-- OrderItem
    Entity <|-- Product
    Entity <|-- PreparationStep
    Entity <|-- Ingredient
```

## Design notes

- `id` defaults to a `uuid4` when not supplied, so entities are identifiable
  before they ever reach a service or store.
- `touch()` is called by every mutator on every subclass, which is what keeps
  `updated_at` / `updated_by` honest without each subclass re-implementing it.
- `soft_delete()` never removes data — it marks it.
