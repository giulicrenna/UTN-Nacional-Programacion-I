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
    
    nums.sort() # Lo sorteamos ya que 

    if len(nums) == 0: return results

    def backtrack(start: int, path: List[int], total: int) -> None:
        if total == target:
            results.append(path.copy()) # Se usa .copy() ya que no queremos copiar la lista en memoria.
            return None
        if total > target:
            return None
        
        for i in range(start, len(nums)):
            # Evita duplicados, ya que si el numero anterior es igual al actual estamos en el mismo nivel.
            if i > start and nums[i] == nums[i-1]:
                continue
            
            #        |--| distintos => Llama a backtrack de nuevo.
            #     |--|  | iguales => continua.
            # [1, 1, 1, 2, 3]

            path.append(nums[i])
            
            backtrack(i + 1, path, total + nums[i]) # Se usa i + 1 porque cada numero se debe utilizar una unica vez.
        
            path.pop()

    # A la funcion la llamo una sola vez ya que es una función recursiva.
    backtrack(0, [], 0)
    
    return results


