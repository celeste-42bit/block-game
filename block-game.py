from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky(texture=load_texture("sky_sunset.jpg"))

boxes = []

def random_color():
    red = random.Random().random() * 255
    green = random.Random().random() * 255
    blue = random.Random().random() * 255
    return color.rgb(red, green, blue)

def add_grass(position):
    boxes.append(
        Button(
        parent=scene,
        model='cube',
        origin=0.5,
        #color=random_color(),   # <--- enable for better contrast
        color=color.rgb(46, 144, 0),
        position=position,
        texture='grass'
        )
    )

def add_dirt(position):
    boxes.append(
        Button(
        parent=scene,
        model='cube',
        origin=0.5,
        color=color.rgb(100, 82, 60),
        position=position,
        texture='perlin_noise.jpg'
        )
    )

def add_stone(position):
    boxes.append(
        Button(
        parent=scene,
        model='cube',
        origin=0.5,
        color=color.rgb(100, 100, 100),
        position=position,
        texture='perlin_noise.png'
        )
    )


# world generator:
for x in range(15):
    for y in range(15):
        add_grass( (x, 5, y) )
for x in range(15):
    for y in range(15):
        for z in range (3, 5):
            add_dirt( (x, z, y) )
for x in range(15):
    for y in range(15):
        for z in range (0, 3):
            add_stone( (x, z, y) )



def input(key):
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                add_dirt(box.position + mouse.normal)
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)

app.run()
