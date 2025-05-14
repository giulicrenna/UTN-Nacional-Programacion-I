# 📚 Ejercicio: Combinaciones de Números Únicos

**Enunciado:**

Dado un arreglo de números enteros positivos `nums` y un número entero `target`, implementa una función:

```python
def unique_combinations(nums: list[int], target: int) -> list[list[int]]:
```

que devuelva **todas** las combinaciones **únicas** de elementos de `nums` que sumen exactamente `target`.

* Cada número en `nums` **puede ser usado una sola vez** en cada combinación.
* Las combinaciones **no deben repetirse** (mismo conjunto aunque en distinto orden se considera repetido).
* El resultado debe ser una lista de listas, donde cada sublista es una combinación válida.
* El orden de los elementos dentro de cada combinación y entre combinaciones **no importa**.

**Restricciones:**

* `1 <= len(nums) <= 15`
* `1 <= nums[i] <= 50`
* `1 <= target <= 100`

**Ejemplos:**

```python
unique_combinations([2,3,6,7], 7)
# Resultado esperado: [[7]]

unique_combinations([10,1,2,7,6,1,5], 8)
# Resultado esperado: [[1,1,6], [1,2,5], [1,7], [2,6]]

unique_combinations([2,5,2,1,2], 5)
# Resultado esperado: [[1,2,2], [5]]
```

---

# 🔥 Tips para resolverlo

* Usar **backtracking** (búsqueda con poda).
* Sería bueno **ordenar** `nums` primero para evitar combinaciones repetidas.
* Usar una **función auxiliar recursiva** dentro de `unique_combinations` puede ayudarte.
