from flet import*
from class_dir.ClassPixel import Pixel

class SaveImageDialog():
    def __init__(self, page):
        super().__init__()
        
        self.page = page
        self.name_file = ""
        
        self.text_field_path_mage = TextField(
            expand=True,
            border_radius = border_radius.all(10),
            cursor_height = 20,
            border_color = "#F05941",
            cursor_color = "#F05941",
        )
        
        self.dialog_view = AlertDialog(
            modal=True,
            title=Text("Сохранения изображения"),
            content=Column(
                controls=[
                    Row(
                        controls=[
                            Text("Название изображения"),
                        ],
                    ),
                    Row(
                        controls=[
                            self.text_field_path_mage
                        ]
                    )
                ]
            ),
            actions=[
                TextButton("Yes", on_click=self.CloseAcept),
            ],
            actions_alignment=MainAxisAlignment.END,
            
        )
        
    def CloseAcept(self, e):
        self.dialog_view.open = False
        self.dialog_view.update()
        self.name_file = self.text_field_path_mage.value
        return True
        
    def open_dlg_modal(self):
        self.page.dialog = self.dialog_view
        self.dialog_view.open = True
        self.page.update()
        
class ColorPicerDialog():
    def __init__(self, page):
        super().__init__()
        
        self.page = page
        self.r = 0
        self.g = 0 
        self.b = 0
        
        self.temp_r = 0
        self.temp_g = 0 
        self.temp_b = 0
        
        self.text_field_color_name = TextField(
            expand=True,
            border_radius = border_radius.all(10),
            cursor_height = 20,
            border_color = "#F05941",
            cursor_color = "#F05941",
        )
        
        self.slider_red = Slider(
            max=255,
            min=0,
            label="{value}#",
            on_change=self.ChengRed
        )
        self.slider_grean = Slider(
            max=255,
            min=0,
            label="{value}#",
            on_change=self.ChengGrean
        )
        self.slider_blue = Slider(
            max=255,
            min=0,
            label="{value}#",
            on_change=self.ChengBlue
        )
        
        self.color_container = Container(
            border_radius=border_radius.all(10),
            height=20,
            expand=True,
        )
        
        self.dialog_view = AlertDialog(
            modal=True,
            title=Text("Цвет кисти"),
            content=Column(
                scroll=True,
                controls=[
                    Row(
                        controls=[
                            Text("Название цвета"),
                        ],
                    ),
                    Row(
                        controls=[
                            self.text_field_color_name
                        ]
                    ),
                    Row(
                        controls=[Text("Красный")]
                    ),
                    Row(
                        controls=[self.slider_red]
                    ),
                    Row(
                        controls=[Text("Зеленый")]
                    ),
                    Row(
                        controls=[self.slider_grean]
                    ),
                    Row(
                        controls=[Text("Синий")]
                    ),
                    Row(
                        controls=[self.slider_blue]
                    ),
                    Row(
                        controls=[self.color_container]
                    )
                ]
            ),
            actions=[
                TextButton("Yes", on_click=self.CloseAcept),
            ],
            actions_alignment=MainAxisAlignment.END,
            
        )
        
    def ChengRed(self,e):
        self.r = self.slider_red.value
        self.UpdateText()
    def ChengGrean(self,e):
        self.g = self.slider_grean.value
        self.UpdateText()
    def ChengBlue(self,e):
        self.b = self.slider_blue.value
        self.UpdateText()
        
    def TranslateToHex(self, dec):
        if dec < 15:
            return hex(int(dec))[:1] + hex(int(dec))[2:]
        elif hex(int(dec))[2:] == "f":
            return "0"+hex(int(dec))[2:]
        else:
            return hex(int(dec))[2:]
    
    def UpdateText(self):
        self.temp_r = self.TranslateToHex(self.r)
        self.temp_g = self.TranslateToHex(self.g)
        self.temp_b = self.TranslateToHex(self.b)
        self.text_field_color_name.value = "#"+self.temp_r+self.temp_g+self.temp_b
        self.text_field_color_name.update()
        self.color_container.bgcolor = self.text_field_color_name.value
        self.color_container.update()
        
    def CloseAcept(self, e):
        self.dialog_view.open = False
        self.dialog_view.update()
        Pixel.color_paint = self.text_field_color_name.value
        self.page.update()
    
    def ChengColorTextField(self, e):
        pass
        
    def open_dlg_modal(self, e):
        self.page.dialog = self.dialog_view
        self.dialog_view.open = True
        self.page.update()