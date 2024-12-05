from nicegui import ui
ui.icon('thumb_up', color='primary').classes('text-5xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('masterfor').style('color: #888; font-weight: bold  font-family: "Times New Roman", serif; font-size: 24px;')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()