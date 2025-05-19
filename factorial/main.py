def factorial_recursivo(n: int) -> int:
    """
    Calcula el factorial de n de forma recursiva,
    donde n! = n * n-1 * n-2 * ... * 1.
    
    Args:
        n (int): Numero a calcular el factorial.

    Returns:
        int: El factorial de n.
    
    Example:    
        factorial_recursivo(5)
        5 * factorial_recursivo(4)
        5 * 4 * factorial_recursivo(3)
        5 * 4 * 3 * factorial_recursivo(2)
        5 * 4 * 3 * 2 * factorial_recursivo(1)
        5 * 4 * 3 * 2 * 1 = 120
    """
    
    if n < 0:
        raise ValueError("El numero a calcular el factorial debe ser mayor a 0.")
    
    if n == 1 or n == 0:
        return n
    
    return n * factorial_recursivo(n=n-1)

def factorial_iterativo(n: int) -> int:
    """
    Calcula el factorial de n de forma iterativa,
    donde n! = n * n-1 * n-2 * ... * 1.
    
    Args:
        n (int): Numero a calcular el factorial.

    Returns:
        int: El factorial de n.
    """
    
    res: int = 1
    
    """
    range(1, 4) = [1, 2, 3]
    range(n, m) -> [n, m)
    """
    
    for num in range(1, n+1):
        res *= num
    
    """
    Se calcula lo mismo pero de forma inversa.
    for num in range(n, 1, -1):
        res *= num
    """
       
    return res

if __name__ == '__main__':
    print('-'*5, ' Factorial Recursivo ', '-'*5)
    print(factorial_recursivo(n=5))
    print(factorial_recursivo(n=10))
    print(factorial_recursivo(n=15))
    print(factorial_recursivo(n=45))
    print('-'*5, ' Factorial Iterativo ', '-'*5)
    print(factorial_iterativo(n=5))
    print(factorial_iterativo(n=10))
    print(factorial_iterativo(n=15))
    print(factorial_iterativo(n=45))
    