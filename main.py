import flet as ft
from app.components import (Header)
from app.providers import ScreenStackPorvider
def main(page:ft.Page):
  page.title = "Ai Agent - Home"
  
  page.window.height = 800
  page.window.width = 1000
  page.window.left = 400
  screenStackProvider = ScreenStackPorvider()
  header = Header()
  page.add(
    header,
    screenStackProvider
    )
  
if __name__ == "__main__":
  ft.app(
    target=main,
  )