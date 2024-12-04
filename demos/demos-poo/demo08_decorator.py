# Fonction décorateur
# Elle prend en paramètre la fonction à décorer
def square_of_result(func):
    # Déclaration de la nouvelle fonction qui rajoute un comportement à la fonction à décorer
    def wrapper(*args, **kwargs):
        # On exécute la fonction initiale avec tous les paramètres
        result = func(*args, **kwargs)
        # Le comportement rajouté
        return result**2

    # On retourne la nouvelle fonction décorée
    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        print(
            f"Appel de la fonction {func.__name__} avec les arguments {args}, {kwargs}"
        )
        result = func(*args, **kwargs)
        print("Fin de l'exécution de la fonction")
        return result

    return wrapper


if __name__ == "__main__":

    def add(a, b):
        return a + b

    print("Avant décorateur")
    print(add(1, 2))

    # Utilisation du décorateur sans l'annotation @
    add = square_of_result(add)
    print("Après décorateur")
    print(add(1, 2))

    @logger
    @square_of_result
    def sub(a, b):
        return a - b

    print(sub(5, 1))
