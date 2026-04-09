import flet as ft

def main(page: ft.Page):

    #Functions
    def changeImage(e):
        images = [""]

    #Page Setup
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Controls
    changeImageButton = ft.Button(content="Get another image", on_click=changeImage)
    page.add(changeImageButton)

ft.run(main=main, assets_dir = "assets")