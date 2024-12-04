class InvalidAgeException(Exception):
    def __init__(self, message="L'age doit être un entier positif") -> None:
        self.message = message
        super().__init__(self.message)

def verifier_age(age: int):

    if not isinstance(age, int):
        raise ValueError()
    
    if age <= 0:
        raise InvalidAgeException(f"L'âge: {age} est invalide")
    
    
    print(age, "est un age valide")

if __name__ == "__main__":
    try:
        verifier_age("toto")
    except InvalidAgeException as ex:
        print("age exception", ex)
    except (ValueError, ZeroDivisionError) as specific:
        print("specific", specific)
    except Exception as e:
        print("autre", e)