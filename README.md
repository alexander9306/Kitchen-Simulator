# Kitchen-Simulator
# Scope: Kitchen Simulator

**Tipo de proyecto:** Aplicación interna
**Fecha:** 2026-08-05
**Estado:** Borrador MVP

## 1. Objetivo

Construir un simulador de cocina que digitalice el flujo de una orden desde que el mesero la toma hasta que el chef la prepara, con visibilidad en tiempo real del estado de cada orden.

## 2. Alcance (MVP)

El MVP cubre el flujo lineal completo de una orden:

1. **Toma de orden (mesero):** el mesero registra una orden nueva (mesa, ítems, cantidad, notas opcionales) y la envía a cocina.
2. **Recepción en cocina:** la orden llega a una cola visible para los chefs, en el orden en que fue creada.
3. **Preparación (chef):** un chef toma la orden de la cola y actualiza su estado a medida que avanza (ej. pendiente → en preparación → lista).
4. **Vista (view):** pantalla de estado que muestra todas las órdenes activas y su estado actual, visible para mesero y cocina.

## 3. Funcionalidades incluidas

| Funcionalidad | Descripción |
|---|---|
| Crear orden | Mesero ingresa mesa, ítems y cantidad |
| Cola de órdenes | Lista de órdenes pendientes visible para chefs |
| Tomar orden | Un chef se asigna una orden de la cola |
| Actualizar estado | Estados: Pendiente → En preparación → Lista → Entregada |
| Vista general | Tablero con todas las órdenes y su estado en tiempo real |

## 4. Fuera de alcance (por ahora)

- Autenticación/roles de usuario con permisos diferenciados
- Notificaciones push o sonoras
- Reportes o analítica histórica
- Manejo de pagos o facturación
- Integración con inventario
- Multi-restaurante / multi-sucursal

## 5. Roles

- **Mesero:** crea órdenes.
- **Chef:** consume la cola, actualiza estado de preparación.
- No se define aún si habrá login o si los roles serán solo vistas separadas sin autenticación (uso interno).

## 6. Flujo simplificado

```
Mesero crea orden
      ↓
Orden entra a la cola de cocina (Pendiente)
      ↓
Chef toma la orden (En preparación)
      ↓
Chef marca como Lista
      ↓
Vista general refleja el estado en tiempo real
```

## 7. Preguntas abiertas / a definir

- Plataforma y stack técnico (web, móvil, escritorio) — pendiente de decisión.
- ¿Persistencia de datos (base de datos) o solo estado en memoria para el simulador?
- ¿Actualización en tiempo real vía polling o websockets?
- ¿Se simulan múltiples mesas/chefs concurrentes desde el inicio o se agrega después?

## 8. Criterio de éxito del MVP

Un mesero puede crear una orden, esta aparece en la cola de cocina, un chef puede tomarla y avanzar su estado, y ambos roles pueden ver el estado actualizado en la vista general — todo sin recargar manualmente ni intervención externa.