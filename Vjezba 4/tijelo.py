import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

height = 1000
width = 1000
window = pyglet.window.Window(width, height, caption='Tijela', resizable=True)

label = pyglet.text.Label('Hello user',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

batch = pyglet.graphics.Batch()
# edge
v_x = []
v_y = []
v_z = []
# polygon
f_1 = []
f_2 = []
f_3 = []
# equations
A = []
B = []
C = []
D = []

tx = 0
ty = 0
tz = 0

vertex_list = []


def is_inside_object(c_x, c_y, c_z):
    inside = True
    for i in range(len(f_1)):
        if (A[i] * c_x + B[i] * c_y + C[i] * c_z + D[i]) > 0:
            print("Dot is outside")
            inside = False
            break
    if inside:
        print("Dot is inside")


def read_all_lines(read_from):
    for line in read_from.readlines():
        variables = line.split(" ")
        if variables[0] == "v":
            v_x.append(variables[1])
            v_y.append(variables[2])
            v_z.append(variables[3])
        if variables[0] == "f":
            f_1.append(int(variables[1])-1)
            f_2.append(int(variables[2])-1)
            f_3.append(int(variables[3])-1)


@window.event
def on_mouse_press(x, y, button, modifiers):
    global tx
    global ty
    global tz
    if button == mouse.LEFT:
        draw_stuff()
        is_inside_object(tx, ty, tz)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.H:
        print("HELLO ")
    glFlush()


@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    label.draw()
    glLoadIdentity()
    batch.draw_indexed()


@window.event
def on_display():
    glFlush()


@window.event
def on_resize(re_width, re_height):
    glViewport(0, 0, re_width, re_height)
    glMatrixMode(gl.GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, re_height, -re_width, re_height)
    glMatrixMode(gl.GL_MODELVIEW)


def draw_stuff():
    for i in range(len(f_1)):
        x1 = float(v_x[f_1[i]])
        print(x1, v_x[f_1[i]], f_1[i])
        y1 = float(v_y[f_1[i]])
        print(y1, v_y[f_1[i]], f_1[i])
        z1 = float(v_z[f_1[i]])
        print(z1, v_x[f_1[i]], f_1[i])
        x2 = float(v_x[f_2[i]])
        print(x2, v_x[f_1[i]], f_1[i])
        y2 = float(v_y[f_2[i]])
        print(y2, v_x[f_1[i]], f_1[i])
        z2 = float(v_z[f_2[i]])
        print(z2, v_x[f_1[i]], f_1[i])
        x3 = float(v_x[f_3[i]])
        print(x3, v_x[f_1[i]], f_1[i])
        y3 = float(v_y[f_3[i]])
        print(y3, v_x[f_1[i]], f_1[i])
        z3 = float(v_z[f_3[i]])
        print(z3, v_x[f_1[i]], f_1[i])
        a = (y2-y1)*(z3-z1)-(z2-z1)*(y3-y1)
        b = -(x2-x1)*(z3-z1)+(z2-z1)*(x3-x1)
        c = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
        d = -x1*a - y1 * b - z1 * c
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)



file = open("kocka.obj", "r")
read_all_lines(file)
# float(input("Give Y to check if in cube"))
tx = 0.5
ty = 0.5
tz = 0.5

pyglet.app.run()

