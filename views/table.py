import flet as ft


class CellData(ft.DataCell):
    def __init__(self, content=None):
        super().__init__(content)
        self.content = ft.Text(
            value="",
            size=14,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.RED_ACCENT_700,
        )


class Table(ft.Container):
    def __init__(self, rows, columns, raw_tbl):
        super().__init__()
        self.alignment = ft.alignment.center
        self.expand = True
        self.rows = int(rows)
        self.columns = int(columns)
        self.raw_tbl = raw_tbl
        self.tbl_data = {}
        for i in range(self.rows):
            for j in range(self.columns):
                self.tbl_data[(i, j)] = CellData()
        self.content = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(str(i)), numeric=True)
                for i in range(self.columns)
            ],
            rows=[
                ft.DataRow(cells=[self.tbl_data[(i, j)] for j in range(self.columns)])
                for i in range(self.rows)
            ],
            border=ft.border.all(width=4, color=ft.colors.INDIGO_800),
            border_radius=10,
            horizontal_lines=ft.BorderSide(width=2, color=ft.colors.INDIGO_800),
            vertical_lines=ft.BorderSide(width=2, color=ft.colors.INDIGO_800),
            divider_thickness=3,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=30,
            bgcolor=ft.colors.LIGHT_BLUE_50,
        )
        self.rotate = ft.transform.Rotate(0, alignment=ft.alignment.center)
        self.animate_rotation = ft.animation.Animation(
            300, ft.AnimationCurve.BOUNCE_OUT
        )
        self.offset = ft.transform.Offset(0, 0)
        self.animate_offset = ft.animation.Animation(500)
        self.scale = ft.transform.Scale(scale=1)
        self.animate_scale = ft.animation.Animation(600, ft.AnimationCurve.DECELERATE)
