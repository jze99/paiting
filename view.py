from flet import *
from class_dir.ClassPaint import GridPixel
from class_dir.ClassPanelRow import RowPanel
from class_dir.ClassDialog import SaveImageDialog

def viewsHendler(page):
    save_image_dialog = SaveImageDialog(page)
    grid_pixel = GridPixel(save_image_dialog=save_image_dialog)
    save_image_dialog.dialog_view.on_dismiss = grid_pixel.LoadPng
    row_panel = RowPanel()
    row_panel.text_field_dsize_image.on_change = grid_pixel.BuildGridView
    row_panel.loading_image_button.on_click = grid_pixel.ChecDialog
    
    
    return {
        '/':View(
            route='/', 
            bgcolor="#22092C",
            controls=[
                Container(
                    expand=True,
                    alignment=alignment.center,
                    content=grid_pixel
                ),
                row_panel
            ]
        )
    }