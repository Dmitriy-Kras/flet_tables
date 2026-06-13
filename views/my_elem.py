import random
from math import pi

import flet as ft


class RichText(ft.Container):
    def __init__(self, txt):
        super().__init__()
        self.padding = 5
        self.txt = txt
        self.content = ft.Stack(
            height=100,
            width=900,
            controls=[
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            txt,
                            ft.TextStyle(
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                foreground=ft.Paint(
                                    color=ft.colors.BLUE_700,
                                    stroke_width=6,
                                    stroke_join=ft.StrokeJoin.ROUND,
                                    style=ft.PaintingStyle.STROKE,
                                ),
                            ),
                        ),
                    ],
                ),
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            txt,
                            ft.TextStyle(
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.GREY_300,
                            ),
                        ),
                    ],
                ),
            ],
        )


def anim_num(page, num):

    size = 60
    gap = 8
    duration = 2000

    c1 = ft.colors.PINK_500
    c2 = ft.colors.AMBER_500
    c3 = ft.colors.LIGHT_GREEN_500
    c4 = ft.colors.DEEP_PURPLE_500
    c5 = ft.colors.BLACK
    c6 = ft.colors.BLUE_ACCENT_700
    c7 = ft.colors.CYAN_ACCENT_700
    c8 = ft.colors.DEEP_ORANGE_400
    c9 = ft.colors.LIME_ACCENT_700

    all_colors = [
        ft.colors.AMBER_400,
        ft.colors.AMBER_ACCENT_400,
        ft.colors.BLUE_400,
        ft.colors.BROWN_400,
        ft.colors.CYAN_700,
        ft.colors.DEEP_ORANGE_500,
        ft.colors.CYAN_500,
        ft.colors.INDIGO_600,
        ft.colors.ORANGE_ACCENT_100,
        ft.colors.PINK,
        ft.colors.RED_600,
        ft.colors.GREEN_400,
        ft.colors.GREEN_ACCENT_200,
        ft.colors.TEAL_ACCENT_200,
        ft.colors.LIGHT_BLUE_500,
    ]

    nums = {
        "0": [
            (0, 0, c2),
            (0, 1, c2),
            (0, 2, c2),
            (0, 3, c2),
            (0, 4, c2),
            (1, 0, c2),
            (1, 4, c2),
            (2, 0, c2),
            (2, 1, c2),
            (2, 2, c2),
            (2, 3, c2),
            (2, 4, c2),
        ],
        "1": [(1, 0, c5), (1, 1, c5), (1, 2, c5), (1, 3, c5), (1, 4, c5), (0, 1, c5)],
        "2": [
            (0, 0, c3),
            (0, 2, c3),
            (0, 3, c3),
            (0, 4, c3),
            (1, 0, c3),
            (1, 2, c3),
            (1, 4, c3),
            (2, 0, c3),
            (2, 1, c3),
            (2, 2, c3),
            (2, 4, c3),
        ],
        "3": [
            (0, 0, c4),
            (0, 2, c4),
            (0, 4, c4),
            (1, 0, c4),
            (1, 2, c4),
            (1, 4, c4),
            (2, 0, c4),
            (2, 1, c4),
            (2, 2, c4),
            (2, 3, c4),
            (2, 4, c4),
        ],
        "4": [
            (0, 0, c6),
            (0, 1, c6),
            (0, 2, c6),
            (1, 2, c6),
            (2, 0, c6),
            (2, 1, c6),
            (2, 2, c6),
            (2, 3, c6),
            (2, 4, c6),
        ],
        "5": [
            (0, 0, c7),
            (0, 1, c7),
            (0, 2, c7),
            (0, 4, c7),
            (1, 0, c7),
            (1, 2, c7),
            (1, 4, c7),
            (2, 0, c7),
            (2, 2, c7),
            (2, 3, c7),
            (2, 4, c7),
        ],
        "6": [
            (0, 0, c1),
            (0, 1, c1),
            (0, 2, c1),
            (0, 3, c1),
            (0, 4, c1),
            (1, 0, c1),
            (1, 2, c1),
            (1, 4, c1),
            (2, 0, c1),
            (2, 2, c1),
            (2, 3, c1),
            (2, 4, c1),
        ],
        "7": [
            (0, 0, c9),
            (1, 0, c9),
            (2, 0, c9),
            (2, 1, c9),
            (2, 2, c9),
            (2, 3, c9),
            (2, 4, c9),
        ],
        "8": [
            (0, 0, c8),
            (0, 1, c8),
            (0, 2, c8),
            (0, 3, c8),
            (0, 4, c8),
            (1, 0, c8),
            (1, 2, c8),
            (1, 4, c8),
            (2, 0, c8),
            (2, 1, c8),
            (2, 2, c8),
            (2, 3, c8),
            (2, 4, c8),
        ],
        "9": [
            (0, 0, c2),
            (0, 1, c2),
            (0, 2, c2),
            (0, 4, c2),
            (1, 0, c2),
            (1, 2, c2),
            (1, 4, c2),
            (2, 0, c2),
            (2, 1, c2),
            (2, 2, c2),
            (2, 3, c2),
            (2, 4, c2),
        ],
    }

    parts = [
        (int(i1) + k * 4, int(i2), i3)
        for k, n in enumerate(str(num))
        for i1, i2, i3 in nums[n]
    ]

    width = 16 * (size + gap)
    height = 5 * (size + gap)

    canvas = ft.Stack(
        width=width,
        height=height,
        animate_scale=duration,
        animate_opacity=duration,
    )

    # spread parts randomly
    for _ in range(len(parts)):
        canvas.controls.append(
            ft.Container(
                animate=duration,
                animate_position=duration,
                animate_rotation=duration,
            )
        )

    def randomize(_):
        random.seed()
        for i in range(len(parts)):
            c = canvas.controls[i]
            part_size = random.randrange(int(size / 2), int(size * 3))
            c.left = random.randrange(0, width)
            c.top = random.randrange(0, height)
            c.bgcolor = all_colors[random.randrange(0, len(all_colors))]
            c.width = part_size
            c.height = part_size
            c.border_radius = random.randrange(0, int(size / 2))
            c.rotate = random.randrange(0, 90) * 2 * pi / 360
        canvas.scale = 5
        canvas.opacity = 0.3
        go_button.visible = True
        again_button.visible = False
        page.update()

    def assemble(_):
        i = 0
        for left, top, bgcolor in parts:
            c = canvas.controls[i]
            c.left = left * (size + gap)
            c.top = top * (size + gap)
            c.bgcolor = bgcolor
            c.width = size
            c.height = size
            c.border_radius = 5
            c.rotate = 0
            i += 1
        canvas.scale = 1
        canvas.opacity = 1
        go_button.visible = False
        again_button.visible = True
        page.update()

    go_button = ft.ElevatedButton("Go!", on_click=assemble)
    again_button = ft.ElevatedButton("Again!", on_click=randomize)

    randomize(None)

    return ft.Container(
        content=ft.Column(controls=[canvas, go_button, again_button]),
        alignment=ft.Alignment(1, 0),
    )


class MySlider(ft.Column):
    def __init__(self, text, max_val, chg=None):
        super().__init__()
        self.min_val = 1
        self.max_val = max_val
        self.visible = False
        self.txt = ft.Text(style=ft.TextStyle(size=25, weight=ft.FontWeight.BOLD))
        self.controls = [
            ft.Text(value=text, style=ft.TextStyle(size=25, weight=ft.FontWeight.BOLD)),
            ft.Slider(
                min=self.min_val,
                max=self.max_val,
                divisions=max_val - 1,
                label="{value}",
                width=300,
                on_change=self.slider_changed,
                on_change_end=chg,
            ),
            self.txt,
        ]

    def slider_changed(self, e):
        self.txt.value = f"Ваше значение {int(e.control.value)}"
        self.value = e.control.value
        self.txt.update()
