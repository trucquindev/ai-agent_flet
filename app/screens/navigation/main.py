import flet as ft

class NavigationScreen (ft.Container):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    
    self.width = 1400
    self.expand=True
    self.bgcolor=ft.Colors.WHITE
    self.content = ft.Column(
      controls=[
        ft.Text(value="Stack navigation!")
      ]
    )