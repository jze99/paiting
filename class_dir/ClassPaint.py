from flet import*
from PIL import Image, ImageDraw
from class_dir.ClassPixel import Pixel

class GridPixel(UserControl):
    def __init__(self, save_image_dialog, text_field_dsize_image):
        super().__init__()
        
        self.text_field_dsize_image = text_field_dsize_image
        
        self.save_image_dialog = save_image_dialog
        
        self.grid_pixel = GridView(
            expand=False,
            spacing=0,
            max_extent=50,
            runs_count=0,
            child_aspect_ratio=1.0,
            run_spacing=0,
        )
        
        self.size = 0
    
    def ConvertInt(self, input_string:str):
        if input_string.strip() == "":
            return 0
        try:
            integer_value = int(input_string)
            return integer_value
        except ValueError:
            return 0
        
    def BuildGridView(self, e):
        self.size = self.ConvertInt(self.text_field_dsize_image.value)
        if self.size == 0:
            return
        self.grid_pixel.controls.clear()
        self.grid_pixel.runs_count = self.size
        self.grid_pixel.height = (450/self.size)*self.size
        self.grid_pixel.width = (450/self.size)*self.size
        self.grid_pixel.max_extent = 450 / self.size
        
        for i in range(self.size**2):
            temp = Pixel()
            temp.SetSize(self.size)
            self.grid_pixel.controls.append(temp)
            
        self.grid_pixel.update()
        
    def LoadPng(self, e):
        image = Image.new('RGB', (self.size, self.size)) 
        vector = [pix.interactive_pixel.bgcolor for pix in self.grid_pixel.controls]
        self.BuildGridView(e=e)
        
        for y in range(self.size):
            for x in range(self.size):
                index = y * self.size + x
                color = vector[index % len(vector)]
                image.putpixel((x, y), tuple(int(color[i:i+2], 16) for i in (1, 3, 5)))
        self.Interpolation(image=image)
        
        
    def Interpolation(self, image):
        import numpy as np
        from PIL import Image
        interpolated_image = image.resize((28, 28), Image.BILINEAR)
        interpolated_image.save("dataset/" + self.save_image_dialog.name_file + ".png")
        
    def ChecDialog(self, e):
        self.save_image_dialog.open_dlg_modal()
        
    def build(self):
        return self.grid_pixel