from flet import *
from class_dir.ClassPaint import GridPixel
from class_dir.ClassPanelRow import RowPanel
from class_dir.ClassDialog import SaveImageDialog, ColorPicerDialog

def viewsHendler(page):
    color_picer_dialog = ColorPicerDialog(page=page)
    save_image_dialog = SaveImageDialog(page=page)
    row_panel = RowPanel()
    grid_pixel = GridPixel(save_image_dialog=save_image_dialog, text_field_dsize_image=row_panel.text_field_dsize_image)
    save_image_dialog.dialog_view.on_dismiss = grid_pixel.LoadPng
    row_panel.text_field_dsize_image.on_change = grid_pixel.BuildGridView
    row_panel.loading_image_button.on_click = grid_pixel.ChecDialog
    row_panel.color_picer_button.on_click = color_picer_dialog.open_dlg_modal
    row_panel.load_II_button.on_click = grid_pixel.TempPain
    GridPixel.ii_text = row_panel.number_text
    
    
    
    
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