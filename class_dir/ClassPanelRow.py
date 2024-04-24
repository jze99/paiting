from flet import *

class RowPanel(UserControl):
    def __init__(self):
        super().__init__()
                
        self.text_field_dsize_image = TextField(
            expand=True,
            border_radius = border_radius.all(10),
            cursor_height = 20,
            label="Размер картинки",
            border_color = "#F05941",
            cursor_color = "#F05941",
        )
        
        self.loading_image_button = TextButton(
            icon=icons.ADD,
            text="Добавить картинку",
        )
        
        self.grid_element = Column(
            spacing=10,
            controls=[
                Row(
                    height=40,
                    controls=[
                        self.text_field_dsize_image,
                    ]
                ),
                Row(
                    height=40,
                    controls=[
                        self.loading_image_button,
                    ]
                )
            ]
        )
        
        self.bg_container = Container(
            bgcolor="#872341",
            expand=True,
            padding=10,
            border_radius=border_radius.all(10),
            content=self.grid_element
        )
        
        self.row_panel=Row(
            height=110,
            controls=[self.bg_container]
        )
    
    def build(self):
        return self.row_panel