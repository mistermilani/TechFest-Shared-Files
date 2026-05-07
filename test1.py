import flet as ft
 
 
def main(page: ft.Page):
 
    # Page Setup
    page.title = "Jordan vs The World"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(image = ft.DecorationImage(src="https://wallpapercave.com/wp/wp2951422.jpg", fit = ft.BoxFit.COVER))
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT
 
    movie = {
        "title": "Jordan vs The World",
        "genre": "Sci-Fi / Drama",
        "synopsis": "El destino del planeta en las manos menos probables.",
        "image": "jordan_poster.png",
    }
 
    # Functions
    def toggle_details(e):
        details.visible = not details.visible
        page.update()
 
    # Controls
    details = ft.Column(
        visible=False,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(movie["genre"], size=18, weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE),
            ft.Text(movie["synopsis"], size=14,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.WHITE),
            ft.Button(content="Play", width=120),
        ],
    )
 
    thumbnail = ft.Container(
        width=570,
        height=380,
        border_radius=10,
        on_click=toggle_details,
        content=ft.Image(
            src=("images/img0.png"),
            fit=ft.BoxFit.COVER,
            width=570,
            height=380,
            border_radius=10,
        ),
    )
 
    layout = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[thumbnail, details],
    )
 
    page.add(layout)
 
 
ft.run(main, assets_dir="assets")