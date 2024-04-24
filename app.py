from flet import *
from view import viewsHendler

def main(page: Page):
       
    page.window_min_height = 300
    page.window_height = 300
    page.window_min_width = 450
    page.window_width = 450
    page.title = "Парсер1"
    page.theme = Theme(
        color_scheme=ColorScheme(
            primary="#F05941"
        )
    )
    
    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(viewsHendler(page)[page.route])
    
    page.on_route_change = route_change
    page.go('/')


app(target=main)