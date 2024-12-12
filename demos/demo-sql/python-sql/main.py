import mariadb
import sys

def main():
    # Connect to MariaDB Platform
    # 127.0.0.1 : l'adresse IP locale de toute machine
    try:
        conn = mariadb.connect(
            user="root", password="", host="127.0.0.1", database="demo_rock"
        )
        print("Connexion ok!")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()

    # Exécute permet d'exécuter une requête SQL
    cur.execute("SHOW DATABASES;")

    # Les résultats des requêtes renvoie des tuplues avec les colonnes sélectionnées
    for db, in cur:
        print(f"Nom base de données: {db}")

    # # On prépare les requêtes sans les paramètres pour se protéger de l'injection SQL
    # query = "INSERT INTO label (nom) VALUES (%s)"
    # # Les paramètres sont passés sous forme de tuples
    # label = input("Saisir le nom d'un label: ")
    # parameters = (label,)

    # cur.execute(query, parameters)

    # # Pour appliquer les modifications, il faut valider la transaction sur la connexion
    # conn.commit()

    last_id = cur.lastrowid
    print(f'Last id: {last_id}')

    query = "INSERT INTO single (titre, duree) VALUES (?, ?)"
    parameters = [
        ('Money For Nothing', 300),
        ('The Less I Know The Better', 290),
        ('Last Nite', 250),
        ('You Really Got Me', 310),
    ]

    cur.executemany(query, parameters)

    print(f"Nombre de lignes affectées: {cur.rowcount}")
    conn.commit()

    cur.close()
    conn.close()

def use_with():
    connection_info = {'user':'root', 'password':'', 'host':'127.0.0.1', 'database':'demo_rock'}
    with mariadb.connect(**connection_info) as con:
        with con.cursor() as cur:
            cur.execute("SELECT prenom, nom FROM artiste;")
            for prenom, nom in cur:
                print(f"Artiste: {prenom} {nom}")

if __name__ == "__main__":
    # main()
    hello = "hello"
    print(type([hello]))
    print(type((hello,)))
    use_with()