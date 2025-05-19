"""
Ejemplo de diccoinario.
    mi_dict = {
        "nombre" : "giuliano",
        "apellido" : "crenna"
    }

    print(mi_dict["nombre"])

    print(mi_dict.keys())

    print(mi_dict.values())

    print(mi_dict.items())
"""
def contar_caracteres(texto: str) -> dict[str, int]:
    """
    Cuenta la cantidad de palabras que hay en una
    cadena de texto:
    
    Args:
        texto (str): Texto al cual se contabilizan las letras.
        
    Returns:
        dict[str, int]: Conteo de cada letra.
    """
    conteo_caracteres: dict[str, int] = dict()
    
    for caracter in texto:
        if not caracter in conteo_caracteres.keys():
            conteo_caracteres[caracter] = 1
            
            continue
        
        conteo_caracteres[caracter] += 1
    
    return conteo_caracteres

if __name__ == '__main__':
    print(contar_caracteres(texto="Giuliano"))
    print(contar_caracteres(texto="UTN"))
    print(contar_caracteres(texto="Tecnicatura en programacion"))
    print(contar_caracteres(texto="Python"))
    print(contar_caracteres(texto="Ejercicio de caracteres"))  
    
    print("La letra a aparece en tecnicatura en programacion: ",
          contar_caracteres(texto="Tecnicatura en programacion")["a"],
          " veces.")  
         
            
    