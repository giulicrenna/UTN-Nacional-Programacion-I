def fibonacci(n: int) -> list[int]:
    """
    Devuelve la sucesion de fibonacci [F0, F1, …, F_{n-1}]. Lanza ValueError si n < 0
    
    Args
        n (int): Posición n-enesima de Fibonacci.
        
    Returns:
        list[int] : Sucesión de Fibonacci hasta la posición n.
    """
    
    seed: list[int] = [0, 1]
    
    if n < 0:
        raise ValueError
    if n == 0:
        return [0]
    if n == 1:
        return seed
    
    for _ in range(n-2):
        follow: int = seed[-1] + seed[-2]
        
        seed.append(follow)
    
    return seed        
        
if __name__ == '__main__':
    print(fibonacci(n=1))
    print(fibonacci(n=2))
    print(fibonacci(n=3))
    print(fibonacci(n=4))
    print(fibonacci(n=9))
    print(fibonacci(n=15))



