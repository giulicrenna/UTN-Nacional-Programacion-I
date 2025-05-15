from typing import List

def unique_combinations(nums: List[int], target: int) -> List[list[int]]:
    """
    Encuentra todas las combinaciones unicas de nums donde los numeros suman target.

    Args:
        nums (List[int]): Lista de numeros enteros candidatos.
        target (int): Suma objetivo.

    Returns:
        List[List[int]]: Todas las conbinaciones válidas.
    """

    results: List[List[int]] = []

    nums.sort()  # Lo sorteamos ya que

    if len(nums) == 0:
        return results

    def backtrack(start: int, path: List[int], total: int) -> None:
        """
        Nos permite realizar las comparaciones pertinentes, utilizando recursividad.
        El algoritmo utiliza poda. (Eliminar los casos inválidos)

        Args:
            start (int): Desde donde vamos a comenzar.
            path (List[int]): Combinacion que estamos construyendo.
            total (int): suma actual de path.
        Returns:
            None
        """

        # Caso base.
        if total == target:
            results.append(
                path.copy()
            )  # Se usa .copy() ya que no queremos copiar la lista en memoria.
            return None
        
        # Caso de poda.
        if total > target:
            return None

        for i in range(start, len(nums)):
            # Evita duplicados, ya que si el numero anterior es igual al actual estamos en el mismo nivel.
            if i > start and nums[i] == nums[i - 1]:
                continue

            #        |--| distintos => Llama a backtrack de nuevo.
            #     |--|  | iguales => continua.
            # [1, 1, 1, 2, 3]

            path.append(nums[i])

            # Caso recursivo
            backtrack(
                start=i + 1, path=path, total=total + nums[i]
            )  # Se usa i + 1 porque cada numero se debe utilizar una unica vez.

            path.pop()

    # A la funcion la llamo una sola vez ya que es una función recursiva.
    backtrack(start=0, path=[], total=0)

    return results


if __name__ == "__main__":
    """
    Nos permite saber si el archivo que estamos ejecutando, es efectivamente ese.
    """

    print(unique_combinations(nums=[1, 2, 3, 4, 5], target=4))

    print(unique_combinations(nums=[3, 6, 8, 4, 2, 33, 21, 19], target=8))

    print(unique_combinations(nums=[1, 5, 6, 4, 1, 1, 1, 1, 1, 2, 0, 6, 1], target=6))
