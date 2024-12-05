from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=100).bind_value(demo, 'numero')
    ui.toggle({7: 'mate', 8: 'algebra', 9: 'llo'}).bind_value(demo, 'numero')
    ui.number().bind_value(demo, 'number')

ui.run()