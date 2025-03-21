import flet as ft 

class AnimationUtils:
  
  @staticmethod
  def animation_shrink(obj:ft.Control, event:ft.ControlEvent):
    if not hasattr(obj,'state_shink'):
      obj.state_shink = False
    if not obj.state_shink:
      obj.state_shink= True
      obj.scale = ft.transform.Scale(
        .65,
        alignment=ft.alignment.center_right
      )
    else:
      obj.state_shink= False
      obj.scale = ft.transform.Scale(
        1,
        alignment=ft.alignment.center_right
      )
    obj.update()