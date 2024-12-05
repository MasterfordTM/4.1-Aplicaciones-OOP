from nicegui import app, ui

app.add_static_files('/stl', 'static')

with ui.scene(width=1024, height=800) as scene:
    # Luz para iluminar el modelo
    scene.spot_light(distance=100, intensity=0.5).move(-10, 0, 10)

    # Agregar el modelo STL con un material y color
    model = scene.stl('/stl/BMD-2M-body.stl')
    model.material(color='#3498db')  # Cambia el color del modelo (azul en este caso)
    model.move(x=-0.5).scale(0.06)

ui.run()
