import flet as ft
import math

images = [f"images/img{i}.png" for i in range(6)]

def main(page: ft.Page):
    max_carousel_controls = 4
    carousel_shift = 0

    def carousel_next(e):
        nonlocal carousel_shift
        carousel_shift += 1

        carousel.controls.clear()
        for i in range(carousel_shift, carousel_shift + max_carousel_controls):
            image_index = i - (len(images) * math.floor(i / len(images)))
            carousel.controls.append(ft.Container(image = ft.DecorationImage(src = images[image_index]), width = 265, height = 160, on_click = on_click1))
            

    def carousel_previous(e):
        nonlocal carousel_shift
        carousel_shift -= 1

        carousel.controls.clear()
        for i in range(carousel_shift, carousel_shift + max_carousel_controls):
            image_index = i - (len(images) * math.floor(i / len(images)))
            carousel.controls.append(ft.Container(image = ft.DecorationImage(src = images[image_index]), width = 265, height = 160, on_click = on_click1))
    
    def on_click1(e):
        page.add(ft.Text(value = "Pequeno", size = 30))
            

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    carousel = ft.Row(
        controls = [ft.Container(image = ft.DecorationImage(src = images[i]), width = 265, height = 160, on_click = on_click1) for i in range(carousel_shift, max_carousel_controls + carousel_shift)],
        alignment = ft.CrossAxisAlignment.CENTER
    )

    carousel_next_button = ft.Button(content = "▶", on_click = carousel_next)
    carousel_previous_button = ft.Button(content = "◀", on_click = carousel_previous)

    page.add(
        carousel,
        ft.Row(
            controls = [carousel_previous_button, carousel_next_button],
            alignment = ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main = main, assets_dir = "assets")