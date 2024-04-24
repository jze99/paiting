from flet import*

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
        