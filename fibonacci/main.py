def fibonacci(n: int) -> int:
    """
    Calcula la n-enisima posicion de fibonacci.
    
    Teoría: Las funciones recursivas, tienen complejidad O(n) = n!
    
    Args:
        n (int): enésima posición.
        
    Return:
        int: Número de Fibonacci.
    """
    
    # Casos bases    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Caso recursivo
    # 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    return fibonacci(n=n - 1) + fibonacci(n=n-2)
    
if __name__ == '__main__':
    print('Fibonacci: ', fibonacci(4))
    print('Fibonacci: ', fibonacci(5))
    print('Fibonacci: ', fibonacci(8))
