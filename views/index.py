import flet as ft
import views.my_elem as el


class Index(ft.Container):
    # def __init__(self):
    #     super().__init__()
    def build(self):
        self.type_table = ft.Dropdown(
            width=250,
            options=[
                ft.dropdown.Option("Змейка"),
                ft.dropdown.Option("Спираль"),
                ft.dropdown.Option("Дартс"),
                ft.dropdown.Option("Диагональ"),
            ],
            on_change=self.choose_variant,
        )
        self.type_button = ft.ElevatedButton(
            "Ввод",
            on_click=self.clk_type_button,
            visible=False,
        )
        self.rows = el.MySlider("Сколько рядов ?", 10, self.show_columns)
        self.columns = el.MySlider("Сколко столбцов ?", 15)
        self.reflex_switch = ft.Switch(
            label="Нарисовать отражение ?",
            label_style=ft.TextStyle(size=25, weight=ft.FontWeight.BOLD),
            label_position=ft.LabelPosition.LEFT,
            value=False,
            visible=False,
        )
        self.data_button = ft.ElevatedButton(
            "Рисуем ?", on_click=self.enter_data, visible=False
        )
        self.start_text = ft.Text(
            "С какой цифры начнем ?",
            style=ft.TextStyle(size=25, weight=ft.FontWeight.BOLD),
            visible=False,
        )
        self.start = ft.TextField(
            label="Начало отсчета",
            value=1,
            visible=False,
            input_filter=ft.NumbersOnlyInputFilter(),
            text_style=ft.TextStyle(size=25, weight=ft.FontWeight.BOLD),
            width=100,
        )
        self.content = ft.Column(
            [
                ft.Row(
                    [el.RichText("Привет какую таблицу нарисуем ?")],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [self.type_table],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    [self.rows, self.columns],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    [self.type_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        self.start_text,
                        self.start,
                        self.reflex_switch,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    [self.data_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment="center",
        )

    def choose_variant(self, _):
        self.rows.visible = True
        self.page.update()

    def clk_type_button(self, _):
        self.start_text.visible = True
        self.start.visible = True
        self.reflex_switch.visible = True
        self.data_button.visible = True
        self.page.update()

    def show_columns(self, _):
        if self.type_table.value != "Дартс":
            self.columns.visible = True
        else:
            self.columns.value = self.rows.value
            self.columns.visible = True
            self.columns.disabled = True
        self.type_button.visible = True
        self.update()

    def enter_data(self, _):
        self.page.go("/table")
