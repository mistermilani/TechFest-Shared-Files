import flet as ft
import flet_video as ftv
import math

def main(page: ft.Page):
    movie = {
        "title": "Jordan vs The World",
        "genre": "Suspense / Action",
        "synopsis": "The planet's destiny in the most unprobable hands.",
        "image": "img0.png",
    }

    movie2 = {
        "title": "Jordan vs Jay",
        "genre": "Suspense / Action",
        "synopsis": "The most powerful weapon in wrong hands: who will wield it?.",
        "image": "img0.png",
    }
    def toggle_details(e):
        details.visible = not details.visible

    def toggle_details1(e):
        details1.visible = not details1.visible

    def movieplay(e):
        page.controls.clear()
        page.add(exit, stack)

    def movieplay1(e):
        page.controls.clear()
        page.add(exit, stack2)

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
            ft.Button(content="Play", width=120, on_click = movieplay),
        ],
    )

    details1 = ft.Column(
        visible=False,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(movie2["genre"], size=18, weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE),
            ft.Text(movie2["synopsis"], size=14,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.WHITE),
            ft.Button(content="Play", width=120, on_click = movieplay1),
        ],
    )

    thumb1 = ft.Container(
        width=380,
        height=570,
        border_radius=10,
        on_click=toggle_details,
        content=ft.Image(
            src=("images/img0.png"),
            fit=ft.BoxFit.COVER,
            width=380,
            height=570,
            border_radius=10,
        ),
    )

    thumb2 = ft.Container(
        width=380,
        height=570,
        border_radius=10,
        on_click=toggle_details1,
        content=ft.Image(
            src=("images/img1.png"),
            fit=ft.BoxFit.COVER,
            width=380,
            height=570,
            border_radius=10,
        ),
    )

    thumbnails = ft.Row(controls = [thumb1, thumb2], alignment = "center")
    detail = ft.Row(controls = [details, details1], alignment = "center")
    containermov = ft.Container()
    #Controls
    
    layout = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[thumbnails, detail],
    )
    
    def show_form(e):
        page.controls.clear()
        
        page.add(containerlog2)

    def moviepage(e):
        page.controls.clear()
        page.add(
        layout)
        
    logintext = ft.Text("Login", size=40, weight=ft.FontWeight.BOLD)
    name1 = ft.TextField(label="First Name")
    name2 = ft.TextField(label="Last Name")
    age = ft.TextField(label="Age")
    username = ft.TextField(label="Username")
    email = ft.TextField(label="Email")
    password = ft.TextField(label="Password", password=True)
    regibutton = ft.Button("Register", on_click = moviepage)

    
    containerlog2 = ft.Container(
        width = 520,
        height = 720,
        bgcolor = ft.Colors.BLUE_GREY_200,
        border = ft.Border.all(3, ft.Colors.BLUE_GREY_500),
        border_radius = 15,
        content = ft.Column(controls = [logintext, name1, name2, age, username, email, password, regibutton],
                            alignment = "center", horizontal_alignment = "center"))
    
    async def videoseek(e):
        position = await video1.get_current_position()
        duration = await video1.get_duration()

        positionms = position.in_milliseconds
        durationms = duration.in_milliseconds

        new_position = positionms + 5000

        if new_position > durationms:
            new_position = durationms

        await video1.seek(new_position)

    async def videoseek2(e):
        position = await video1.get_current_position()

        positionms = position.in_milliseconds
        new_position = max(0, positionms - 10000)

        await video1.seek(new_position)

    #Controls
    videos = [ftv.VideoMedia("https://1drv.ms/v/c/4cc49e5504c17ff1/IQAKrUPyx40pS6U_f1J-RmG-AVWAGFKa-B401-D40SFZ9oo?e=abCS8h")]
    videos2 = [ftv.VideoMedia("https://1drv.ms/v/c/4cc49e5504c17ff1/IQCfaDpdZiIbQr-W6jT0Yrr4ATTQv9Qa3FayUIkJcK_9dPM?e=nqkNeo")]
    video1 = ftv.Video(
                        playlist = videos,
                        playlist_mode=ftv.PlaylistMode.LOOP,
                        fill_color=ft.Colors.BLUE_400,
                        aspect_ratio = 12/5,
                        volume=100,
                        autoplay=False,
                        filter_quality=ft.FilterQuality.HIGH,
                        muted=False)
    
    video2 = ftv.Video(
                        playlist = videos2,
                        playlist_mode=ftv.PlaylistMode.LOOP,
                        fill_color=ft.Colors.BLUE_400,
                        aspect_ratio = 12/5,
                        volume=100,
                        autoplay=False,
                        filter_quality=ft.FilterQuality.HIGH,
                        muted=False)
    
    seekbutton = ft.Button(content = "▶", on_click = videoseek)
    seekbutton2 = ft.Button(content = "◀", height = 30, on_click = videoseek2)
    seekrow = ft.Row(controls = [seekbutton2, seekbutton], alignment = ft.MainAxisAlignment.SPACE_BETWEEN)
    stack = ft.Stack(controls = [video1, seekrow])
    exit = ft.Button(content = "⨉", on_click = moviepage, align = ft.Alignment.TOP_LEFT)

    stack = ft.Stack(controls = [video1, seekrow])
    stack2 = ft.Stack(controls = [video2, seekrow])
    
    page.title = "Cinebrary"
    
    subtitle = ft.Text(
        value="Start now",
        size=16,
        
        text_align=ft.TextAlign.CENTER
    )
 
    button = ft.Button(
        content="Login",
        on_click=show_form
    )
    
    #Page Setup
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(image = ft.DecorationImage(src="https://wallpapercave.com/wp/wp2951422.jpg", fit = ft.BoxFit.COVER))
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT

    #Controls
    subtitle = ft.Text(value="Start now", size = 16)

    logo = ft.Container(image = ft.DecorationImage(src = "images/cinebrary1.png"), width = 385, height = 76)
    containerlog1 = ft.Container(
        width = 520,
        height = 650,
        bgcolor = ft.Colors.BLUE_GREY_200,
        border = ft.Border.all(3, ft.Colors.BLUE_500),
        border_radius = 15,
        content = ft.Column(controls = [
            logo, subtitle, button],
            alignment = "center", horizontal_alignment = "center"
            )
        )
    page.add(containerlog1)

ft.run(main = main, assets_dir = "assets")