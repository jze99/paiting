from flet import*

class Pixel(UserControl):  
    clic = False
    
    def __init__(self):
        super().__init__()
        
        self.interactive_pixel = Container(
            width=450,
            height=450,
            bgcolor="#FFFFFF",
            on_hover=self.PaitingPixel,
            on_click=self.Clic
        )
        self.chec_mouse = False
    
    def SetSize(self, size):
        self.interactive_pixel.width = self.interactive_pixel.width/size
        self.interactive_pixel.height = self.interactive_pixel.height/size
        
    def Clic(slef, e):
        if Pixel.clic:
            Pixel.clic = False
        else:
            Pixel.clic = True
        
    def PaitingPixel(self, e):
        if Pixel.clic:
            self.interactive_pixel.bgcolor = "#000000"
            self.interactive_pixel.update()
    
    def build(self):
        return self.interactive_pixel