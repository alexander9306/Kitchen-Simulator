# Entities

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
    }

    class Order {
        +String id
        +Customer customer
        +Chef chef
        +List~OrderItem~ items
        +OrderStatus status
        +DateTime estimated_ready_at
        +DateTime created_at
        +String created_by
        +add_item(item: OrderItem) void
        +update_status(status: OrderStatus) void
        +take_order() void
        +search_for_ingredients() void
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

    class Ingredient {
        +String name
        +int quantity_in_stock
    }

    class Product {
        +String name
        +float difficulty
    }

    class PreparationStep {
        +String name
        +float step_time
    }

    class Chef {
        +String name
        +float experience
    }

    class Customer {
        +String name
    }

    Entity <|-- Customer
    Entity <|-- Order
    Entity <|-- OrderItem
    Entity <|-- Product
    Entity <|-- PreparationStep
    Entity <|-- Ingredient
    Entity <|-- Chef
    Order "1" *-- "1..*" OrderItem : contiene
    Order "1" --> "1" OrderStatus : tiene
    OrderItem "0..*" --> "1" Product : referencia
    Customer "1" --> "0..*" Order : crea
    Chef "1" --> "0..*" Order : prepara
```

## Entity

Shared base for every **entity** in the domain: identity plus audit trail

### Design notes

- `id` defaults to a `uuid4` when not supplied, so entities are identifiable
  before they ever reach a service or store.

## Ingredient

A raw material consumed while preparing a product. An ingredient knows *what it
is*; how much of it exists is a stock concern.

## Product

What the customer buys — the menu item. A product knows how hard it is to make
and which steps produce it; it does not know anything about stock.

### Design notes

`difficulty` exists to feed the preparation-time formula of requirement 10:

```
step_duration = step.step_time / chef.experience * product.difficulty
```

It is stored here, on the product, because difficulty is a property of the dish
itself and is set by the company — not by the customer and not by the chef.

**Product is not Ingredient.** A product is *sold*; an ingredient is *consumed*.
Nothing stocks a product and nothing orders an ingredient. They look similar
because both carry `id` and `name`, but merging them would leave `difficulty`
and `PreparationStep[]` meaningless on a tomato, and `quantity_in_stock`
meaningless on a hamburger.

Requirement 9c blurs this — it says *"productos en existencia"* and then names
the resulting status *"En busca de ingredientes"*. The model follows the second
reading: only ingredients are stocked.

Composition (`*--`) is used for the step relationship because a `PreparationStep`
has no meaning outside the product that defines it.

### Pending decisions

- **Items sold ready-made** (a bottled drink, a bag of chips) are both sellable
  and stocked. Current plan: model them as a `Product` with a single ~0-time
  `PreparationStep` that consumes one same-named `Ingredient`, so that
  `PreparationStep.execute` stays the only path by which anything is produced.
- Requirement 10 says *"la dificultad del pedido (de la orden del cliente)"*.
  Difficulty currently lives on `Product`. Confirm whether an order containing
  several products derives its difficulty from them (max? sum? per-item?) or
  whether `Order` carries its own.

## PreparationStep

One step in the recipe for a product ("toast the bread"), with the time it takes
at baseline. Steps are what make requirement 9d real: the simulator must
actually wait for each one.

## Chef

Who prepares the orders. A chef knows how skilled they are; the work of moving
an order through its states belongs to the order.

### Design notes

`experience` is the chef's speed factor in the preparation-time formula of
requirement 10:

```
step_duration = step.step_time / chef.experience * product.difficulty
```

It divides, so a higher number means a faster chef. This is the only reason the
chef participates in the simulation's timing at all — which is why it belongs on
the entity rather than being looked up elsewhere.

**`take_order` and `search_for_ingredients` are not here.** They used to be, but
they read only `self.id` and wrote everything to the order — Feature Envy. Both
are status transitions, so they moved onto `Order`, the object whose state
actually changes. See the Order section below.

A chef is associated with the orders they prepare, but that link is navigated
from `Order.chef`, so it is drawn in the Order section rather than duplicated
here.

### Pending decisions

- **`experience` is missing from the code.** `chef.py` currently defines only
  `name`. The formula in requirement 10 cannot be implemented until the field
  exists.
- **Range and meaning of `experience` are undefined.** Requirement 10 leaves the
  scale to you ("un numero que le pueden poner al chef ustedes mismos"). Decide
  the baseline — `1.0` meaning "cooks exactly at the step's stated time" is the
  reading that makes `step_time` self-explanatory — and whether values below
  that (a slower chef) are allowed. Guard against zero either way, since it
  divides.
- **Assigning a chef to an order** needs the queue and chef availability, so it
  is service work, not a method here.

## Customer

The person who places orders. A customer knows *who they are*, not how the
kitchen works.

## Order

What a customer asked for, and how far along it is. `Order` is the entity that
guards its own status and item list.

### Design notes

**Order holds object references, not foreign keys.** `customer` and `chef` are
`Customer` and `Chef` instances rather than `customerId` / `chefId` strings

`*--` to `OrderItem` is composition: an order item has no life of its own once
its order is gone. `-->` to `Customer` is a plain association — customers outlive
orders.
