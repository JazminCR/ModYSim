# Justificación de por qué las funciones mapean a (0,1)

La clave está en que usamos funciones que transforman los intervalos originales hacia (0,1) de forma:

- **Biyectiva**: uno a uno.
- **Monótona**: siempre creciente o decreciente.
- **Suave**: continua y diferenciable.

---

## 1. De (a, b) a (0, 1)

**Cambio de variable:**

```
x = a + (b - a) * u
```

Donde `u ∈ (0, 1)` ⇒ `x ∈ (a, b)`.

**Justificación:**

- Es una función lineal (estrictamente creciente si `b > a`).
- Continua y diferenciable.
- Cubre todo el intervalo `(a, b)` cuando `u` recorre `(0, 1)`.

---

## 2. De (0, ∞) a (0, 1)

**Cambio de variable:**

```
x = u / (1 - u)
```

Donde `u ∈ (0, 1)` ⇒ `x ∈ (0, ∞)`.

**Justificación:**

- Cuando `u → 0⁺`, `x → 0`.
- Cuando `u → 1⁻`, `x → ∞`.
- Función creciente, continua y diferenciable.
- Recorre todo el intervalo `(0, ∞)` sin saltos ni repeticiones.

---

## 3. De (−∞, 0) a (0, 1)

**Cambio de variable:**

```
x = (1 / u) - 1
```

Donde `u ∈ (0, 1)` ⇒ `x ∈ (−∞, 0)`.

**Justificación:**

- Cuando `u → 0⁺`, `x → ∞`.
- Cuando `u → 1⁻`, `x → 0⁺` ⇒ cambiar signo: `x → -∞`.
- Entonces usamos:  
  ```
  x = -((1 / u) - 1)
  ```
  para que `x` crezca de `−∞` a `0`.

- Función decreciente, continua y diferenciable.

---

## 4. De (1, ∞) a (0, 1)

**Cambio de variable:**

```
x = (1 + u) / (1 - u)
```

Donde `u ∈ (0, 1)` ⇒ `x ∈ (1, ∞)`.

**Justificación:**

- Cuando `u → 0⁺`, `x → 1`.
- Cuando `u → 1⁻`, `x → ∞`.
- Función creciente, continua y diferenciable.

---

---

## 5. De (−1, ∞) a (0, 1)

**Cambio de variable:**

```math
x = \frac{2u}{1 - u} - 1
```

Donde `u ∈ (0, 1)` ⇒ `x ∈ (−1, ∞)`.

**Justificación:**

- Cuando `u → 0⁺`, `(2 * u) / (1 - u) → 0`, entonces `x → -1`.
- Cuando `u → 1⁻`, `(2 * u) / (1 - u) → ∞`, entonces `x → ∞`.
- Por lo tanto, `x = (2 * u) / (1 - u) - 1` recorre todo el intervalo `(−1, ∞)`.
- Función creciente, continua y diferenciable.

---


**Teorema de Fubini**  
Si `f(x,y)` es continua (o integrable absoluta) sobre una región rectangular `[a,b] × [c,d]`, entonces:

```math
\int_a^b \int_c^d f(x,y) \, dy \, dx = \int_c^d \int_a^b f(x,y) \, dx \, dy

