
# **Contar caracteres en un texto** (intermedio-alto)
   Crea una función `contar_caracteres(texto: str) -> dict[str, int]` que reciba una cadena y devuelva un diccionario con la frecuencia de cada carácter (excluyendo espacios).

   ```python
   def contar_caracteres(texto: str) -> dict[str, int]:
       """
       Cuenta cuántas veces aparece cada carácter distinto en texto (sin contar espacios).
       """
       ...
   ```

   **Ejemplos**:

   ```python
   contar_caracteres("hola mundo")
   # → {'h':1, 'o':3, 'l':1, 'a':1, 'm':1, 'u':1, 'n':1, 'd':1}

   contar_caracteres("")
   # → {}
   ```

