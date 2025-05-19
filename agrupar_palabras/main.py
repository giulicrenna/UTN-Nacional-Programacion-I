def agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]:
    """
    Agrupa las palabras según su longitud.
    
    Args:
        palabras (list[str]): Las palabras a agrupar.
        
    Returns:
        dict[int, list[str]]: Grupos de palabras.
    """
    
    grupos: dict[int, list[str]] = dict()
    
    for palabra in palabras:
        if len(palabra) not in grupos.keys():
            grupos[len(palabra)] = [palabra]
            
            continue
        
        grupos[len(palabra)].append(palabra)
        
    return grupos

if __name__ == '__main__':
    grupos: dict = agrupar_por_longitud(palabras=["casa", "sol", "luna", "mar", "árbol"])
    
    print(grupos)
    
    print("las siguientes palabras tienen longitud 4: ")
    
    for i in grupos[4]:
        print(f'\t- {i}')    
    