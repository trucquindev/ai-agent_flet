import flet as ft

class Header(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = 50
        self.width = 1400
        self.bgcolor = ft.Colors.DEEP_PURPLE_500
        self.border_radius=ft.border_radius.all(10)
        self.padding=ft.padding.only(right=10)
        self.content = ft.Row(
          controls=[
            ft.IconButton(
              icon=ft.Icons.MENU,
              icon_size=24,
              icon_color=ft.Colors.WHITE,
              ),
            ft.CircleAvatar(
              content=ft.Icon(
                name=ft.Icons.PERSON,
                size=24,
                color=ft.Colors.WHITE
                ),
              bgcolor=ft.Colors.DEEP_PURPLE_500,
            )
          ],
          alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )