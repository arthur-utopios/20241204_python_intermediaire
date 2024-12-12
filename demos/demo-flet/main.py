import flet as ft

from task import Task


# Définition de notre application
def main(page: ft.Page):
    # titre de la page
    page.title = "Compteur Flet"

    # Définition de l'affichage vertical
    # L'application est centrée sur l'axe des ordonnées
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Création d'un champ de texte
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    # Deux fonctions pour gérer l'événement d'un click button
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)

        # On force la mise à jour de l'affichage
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Column(
            [
                Task(text="Do laundry"),
                Task(text="Cook dinner"),
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )

    # On ajoute un composant à notre page
    page.add(
        # Composant qui permet d'afficher plusieurs contrôles sur une ligne
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            # Les éléments sont alignés par rapport à l'axe des abscisses
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)
