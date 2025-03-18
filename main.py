import flet as ft

def main(page:ft.Page):
  page.title = "Ai Agent - Home"
  
  page.window.height = 800
  page.window.width = 1000
  
  page.window.center()
  
  page.add(ft.Text(value="Hello Alias, World!"))
  
if __name__ == "__main__":
  ft.app(
    target=main,
  )