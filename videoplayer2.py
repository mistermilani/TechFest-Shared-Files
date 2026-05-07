import flet as ft
import flet_video as ftv
import flet_audio as fta

def main(page: ft.Page):
    #Functions
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

    #Page Setup
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    #Controls
    videos = [ftv.VideoMedia("https://user-images.githubusercontent.com/28951144/229373720-14d69157-1a56-4a78-a2f4-d7a134d7c3e9.mp4")]
    video1 = ftv.Video(
                        playlist = videos,
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

    page.add(stack)
ft.run(main=main, assets_dir = "assets")