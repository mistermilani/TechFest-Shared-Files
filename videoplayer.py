import flet as ft
import flet_video as ftv
import flet_audio as fta

def main(page: ft.Page):
    #Functions
    #async def play(e: ft.Event[ft.Button]):
    #    await video1.play_or_pause()
    #    if playstop.content == "Play":
    #        playstop.content = "Pause"
    #    else:
    #        playstop.content = "Play"

    #async def fullscreen(e: ft.Event[ft.Button]):
    #    video1.fullscreen = True


    #def volumechange(e: ft.Event[ft.Slider]):
    #    video1.volume = e.control.value

    async def videoseek(e: ft.Event[ft.Button]):
        await video1.seek()

    async def videoseek2(e: ft.Event[ft.Button]):
        await video1.seek()

    #Page Setup
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    #Controls
    #playstop = ft.Button(content = "Play", on_click = play)
    #sliderv = ft.Slider(value = 100, min = 0, max = 100, divisions = 100, width = 200, height = 50, on_change = volumechange)
    #fullbutton = ft.Button(content = "Fullscreen", on_click = fullscreen)

    #test = ft.Button(content = "get dur", on_click = getduration)
    #test1 = ft.Button(content = "get pos", on_click = getpos)
    #test2 = ft.Text(value = "a", width = 50, height=50)

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
    seekbutton2 = ft.Button(content = "◀", on_click = videoseek2)
    seekrow = ft.Row(controls = [seekbutton2, seekbutton])
    
    
    #controls = ft.Row(controls = [playstop, fullbutton, sliderv])

    page.add(video1, seekrow)
ft.run(main=main, assets_dir = "assets")