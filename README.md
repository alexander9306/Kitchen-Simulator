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

