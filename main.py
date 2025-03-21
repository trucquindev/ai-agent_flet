import flet as ft
from app.components import (Header)
from app.providers import ScreenStackPorvider
def main(page:ft.Page):
  page.title = "Ai Agent - Home"
  
  page.window.height = 800
  page.window.width = 1400
  page.window.left = 400
  page.bgcolor=ft.Colors.PINK_100
  screenStackProvider = ScreenStackPorvider()
  header = Header(
    handle_animation_shrink= screenStackProvider.homeScreen.handle_animation_shrink
  )
  page.add(
    header,
    screenStackProvider
    )
  
if __name__ == "__main__":
  ft.app(
    target=main,
  )