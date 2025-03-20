import flet as ft

class HomeScreen (ft.Container):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    
    self.width = 1400
    self.bgcolor=ft.Colors.WHITE
    self.expand=True
    self.animate_scale=ft.animation.Animation(
      duration=600,
      curve=ft.animation.AnimationCurve.DECELERATE,
    )
    self.content= ft.Column(
      controls=[
        ft.Text(value="Main screen!")
      ]
    )
  def handle_animation_shrink(self, event:ft.ControlEvent):
    self.scale = ft.transform.Scale(
      .65,
      alignment=ft.alignment.center_right
    )