import flet as ft
from ..screens import (HomeScreen,NavigationScreen)
class ScreenStackPorvider(ft.Stack):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.homeScreen = HomeScreen()
    self.navigationScreen = NavigationScreen()
    
    self.controls=[
      self.navigationScreen,
      self.homeScreen
    ]