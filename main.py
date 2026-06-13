from math import pi
from time import sleep

import flet as ft
import views.my_elem as el
from assets.mystyles import button_style
from core import tables as tb
from views.index import Index
from views.table import Table


def main(page: ft.Page):
    transfer_data = {"scale": 1}

    def drow_table():
        types = {
            "Змейка": tb.Snake,
            "Спираль": tb.Spiral,
            "Диагональ": tb.Diagonal,
            "Дартс": tb.Darts,
        }
        args = ["type_table", "start", "reflex_switch", "rows", "columns"]
        tab_args = [getattr(transfer_data["index"], arg).value for arg in args]
        typ, start, reflex, rows, cols = tab_args
        return rows, cols, types[typ](int(rows), int(cols), int(start), reflex).raw()

    def show_number(e):
        transfer_data["number"] = e.control.data
        page.go("/table/number")

    def fill_table(_):
        fill_button.visible = False
        rotate_button.visible = True
        reveal_button.visible = True
        scale_button_minus.visible = True
        scale_button_plus.visible = True
        table = transfer_data["table"]
        for i, j, val in table.raw_tbl:
            cell = table.tbl_data[(i, j)]
            cell.content.value = cell.data = val
            cell.on_tap = show_number
            sleep(0.05)
            page.update()

    def clk_rotate(_):
        table = transfer_data["table"]
        table.rotate.angle += pi / 2
        page.update()

    def clk_reveal(e):
        table = transfer_data["table"]
        table.offset = ft.transform.Offset(*e.control.data)
        table.update()

    def clk_scale_plus(_):
        table = transfer_data["table"]
        if transfer_data["scale"] < 2:
            scale_button_minus.disabled = False
            transfer_data["scale"] += 0.25
        else:
            scale_button_plus.disabled = True
        table.scale = transfer_data["scale"]
        page.update()

    def clk_scale_minus(_):
        table = transfer_data["table"]
        if transfer_data["scale"] > 0.25:
            scale_button_plus.disabled = False
            transfer_data["scale"] -= 0.25
        else:
            scale_button_minus.disabled = True
        table.scale = transfer_data["scale"]
        page.update()

    fill_button = ft.ElevatedButton(text="Заполнить", on_click=fill_table)
    rotate_button = ft.ElevatedButton(
        "Повернуть", style=button_style, on_click=clk_rotate
    )
    reveal_button = ft.IconButton(
        style=button_style,
        icon=ft.icons.ZOOM_IN_MAP_OUTLINED,
        on_click=clk_reveal,
        data=(0, 0),
    )
    move_left = ft.IconButton(
        style=button_style,
        icon=ft.icons.ARROW_BACK,
        on_click=clk_reveal,
        data=(-0.5, 0),
    )
    move_up = ft.IconButton(
        style=button_style,
        icon=ft.icons.ARROW_UPWARD,
        on_click=clk_reveal,
        data=(0, -0.5),
    )
    move_right = ft.IconButton(
        style=button_style,
        icon=ft.icons.ARROW_FORWARD,
        on_click=clk_reveal,
        data=(0.5, 0),
    )
    move_down = ft.IconButton(
        style=button_style,
        icon=ft.icons.ARROW_DOWNWARD,
        on_click=clk_reveal,
        data=(0, 0.5),
    )
    scale_button_plus = ft.ElevatedButton(
        "Масштаб", style=button_style, on_click=clk_scale_plus, icon=ft.icons.ADD
    )
    scale_button_minus = ft.ElevatedButton(
        "Масштаб", style=button_style, on_click=clk_scale_minus, icon=ft.icons.REMOVE
    )

    def route_change(_):
        match page.route, page.views[-1].route:
            case "/", _:
                index = transfer_data["index"] = Index()
                page.views[0] = ft.View(
                    "/",
                    [
                        ft.AppBar(
                            title=ft.Text("Выбор таблицы"),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        index,
                    ],
                )
            case "/table", "/table":
                pass
            case "/table", _:
                table = transfer_data["table"] = Table(*drow_table())
                fill_button.visible = True
                rotate_button.visible = False
                reveal_button.visible = False
                scale_button_minus.visible = False
                scale_button_plus.visible = False
                page.views.append(
                    ft.View(
                        "/table",
                        [
                            ft.AppBar(
                                title=ft.Text("Ваша таблица"),
                                bgcolor=ft.colors.SURFACE_VARIANT,
                            ),
                            table,
                            fill_button,
                            ft.Row(
                                controls=[
                                    rotate_button,
                                    reveal_button,
                                    move_left,
                                    move_up,
                                    move_down,
                                    move_right,
                                    scale_button_minus,
                                    scale_button_plus,
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                )
            case "/table/number", _:
                number = transfer_data["number"]
                page.views.append(
                    ft.View(
                        "/table/number",
                        [
                            ft.AppBar(
                                title=ft.Text(f"Вы выбрали номер {number}"),
                                bgcolor=ft.colors.SURFACE_VARIANT,
                            ),
                            el.anim_num(page, number),
                        ],
                    )
                )
        page.update()

    def view_pop(_):
        # if page.views.pop().route == "/table":
        # del transfer_data["table"]
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)
