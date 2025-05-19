# **Agrupar palabras por longitud** (avanzado)
   Implementa `agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]` que reciba una lista de palabras y devuelva un diccionario donde cada clave es una longitud y el valor es la lista de palabras con esa longitud.

   ```python
   def agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]:
       """
       Agrupa las palabras según su longitud.
       """
       ...
   ```

   **Ejemplos**:

   ```python
   agrupar_por_longitud(["casa", "sol", "luna", "mar", "árbol"])
   # → {4: ["casa", "luna"], 3: ["sol", "mar"], 5: ["árbol"]}

   agrupar_por_longitud([])
   # → {}
   ```
