# Kitchen Simulator

A simulator of how a restaurant kitchen handles an order — from the customer placing it, to checking ingredients, to the chef cooking it step by step, to completion.

## 1. What it does

1. A customer places an order.
2. The system estimates when it'll be ready, based on the order and the current queue.
3. A chef picks it up and checks if the ingredients are in stock.
4. **No stock?** The order goes to a "Searching for ingredients" state.
5. **Stock available?** The chef follows the preparation steps. Each step takes its real defined time (non-blocking).
6. Once every step is done, the order is **Completed**.
7. Every state change is saved to the order's history.
```
Order placed
   ↓
Time estimated
   ↓
Chef picks it up → checks stock
   ↓                      ↓
Stock OK             No stock
   ↓                      ↓
Cook step by step   "Searching for ingredients"
   ↓                      ↓
Completed  ←──────── (back to cooking once stock arrives)
```

Ingredients get locked while an order is using them, so another order can't take them at the same time.

## 2. How preparation time is calculated

```
time = (step_time / chef_experience) * order_difficulty
```

| Value | Meaning |
|---|---|
| `step_time` | How long the step normally takes (e.g. toasting bread = 5 min) |
| `chef_experience` | A number we assign to each chef |
| `order_difficulty` | A number the business assigns to each dish |

Applied per step. The simulator actually waits that long before moving on — without blocking the main thread.

## 3. Build plan

Each item below is its own PR, with a description and a UML diagram.

**Phase 1 — Research**
- Native language tools (no libraries) for OOP
- Native tools for design patterns: Singleton, Decorator, Adapter, MVC, Observer, Builder, Factory, Strategy, DAO
- Native tools for SOLID
- Repo setup + review access for `reynoldmorel@gmail.com`
**Phase 2 — Domain**
- Entities, **one context per PR** (Product and Customer can't share a PR)
- Custom dependency injection mechanism — the PR explains why it's needed and what it buys us
**Phase 3 — Services & Controllers**
- Services: store the models efficiently. One PR each. Single instance only.
- Controllers: the bridge between the simulator and the services. One PR each. Single instance only.
**Phase 4 — Simulation**
- The simulation module itself
- The preparation time formula
- Order history
## 4. Done when

- An order can be placed and gets a time estimate.
- Stock is checked correctly, and missing ingredients route to the right state.
- Each step respects its real duration without freezing the app.
- The order reaches Completed.
- Every state change shows up in the history.
- The OOP tools, patterns, SOLID principles, and the DI mechanism are all in place and documented with UML.
