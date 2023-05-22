import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
import numpy as np

height = 1000
width = 1000
window = pyglet.window.Window(width, height, caption='Tijela', resizable=True)

batch = pyglet.graphics.Batch()
# edge
v_x = []
v_y = []
v_z = []
# polygon
f_1 = []
f_2 = []
f_3 = []
edges = [] 
# equations
A = []
B = []
C = []
D = []
#scaling
scaling = 0

tx = 0
ty = 0
tz = 0
vertices = []
colors = []
ociste_x = 2
ociste_y = 2
ociste_z = 2
glediste_x = 5
glediste_y = 5
glediste_z = 5

def transformacije(x_ociste, y_ociste, z_ociste, x_glediste, y_glediste, z_glediste):
    t1 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-x_ociste, -y_ociste, -z_ociste, 1]]
    g1 = np.matmul([x_glediste, y_glediste, z_glediste, 1], t1)
    naz = np.sqrt(g1[0]*g1[0] + g1[1] * g1[1])
    sinKut = g1[1] / naz
    cosKut = g1[0] / naz
    t2 = [[cosKut, -sinKut, 0, 0], [sinKut, cosKut, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    g2 = np.matmul(g1, t2)
    naz2 = np.sqrt(g2[0]*g2[0] + g2[1]*g2[1])
    sinKut2 = g2[0] / naz2
    cosKut2 = g2[2] / naz2
    t3 = [[cosKut2, 0, sinKut2, 0], [0, 1, 0, 0], [-sinKut2, 0, cosKut2, 0], [0, 0, 0, 1]]
    g3 = np.matmul(g2, t3)
    t4 = [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    t5 = [[-1, 0, 0, 0,], [0, 1, 0, 0,], [0, 0, 1, 0], [0, 0, 0, 1]]
    ukupnaTransformacija = np.matmul(t2, t3)
    ukupnaTransformacija = np.matmul(ukupnaTransformacija, t4)
    ukupnaTransformacija = np.matmul(ukupnaTransformacija, t5)
    ukupnaTransformacija = np.matmul(t1, ukupnaTransformacija)
    ociste_razlika_x = x_ociste - x_glediste
    ociste_razlika_y = y_ociste - y_glediste
    ociste_razlika_z = z_ociste - z_glediste
    h = np.sqrt( ociste_razlika_z**2 + ociste_razlika_y**2 + ociste_razlika_x**2)
    tr_tocka = []
    p = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1/h], [0, 0, 0, 0]]
    for i in range(len(v_x)):
        current_dot = np.matmul([v_x[i] , v_y[i] , v_z[i], 1], ukupnaTransformacija)
        current_dot = np.matmul(current_dot, p)
        current_dot = np.multiply(current_dot, 1/current_dot[3])
        tr_tocka.append(tr_tocka)
    return ukupnaTransformacija


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
    global scaling
    for line in read_from.readlines():
        variables = line.split(" ")
        if variables[0] == "v":
            v_x.append(float(variables[1]))
            v_y.append(float(variables[2]))
            v_z.append(float(variables[3]))
            scaling = variables[1] + variables[2] + variables[3]
        if variables[0] == "f":
            f_1.append(int(variables[1])-1)
            f_2.append(int(variables[2])-1)
            f_3.append(int(variables[3])-1)
            edges.append([int(variables[1]), int(variables[2]) , int(variables[3])])


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        is_inside_object(tx, ty, tz)
    if button == mouse.RIGHT:
        on_draw()


@window.event
def on_key_press(symbol, modifiers):
    global ociste_x, ociste_y, ociste_z
    if symbol == key.H:
        print("HELLO ")
    if symbol == key.Q:
        ociste_x += 1
    if symbol == key.W:
        ociste_y += 1
    if symbol == key.E:
        ociste_z += 1
    if symbol == key.R:
        ociste_x -= 1
    if symbol == key.T:
        ociste_y -= 1
    if symbol == key.Y:
        ociste_z -= 1
    draw_stuff()
    glFlush()


@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
def draw_stuff():
    x_min = min(v_x)
    x_max = max(v_x)
    y_min = min(v_y)
    y_max = max(v_y)
    x_avg = ((float(x_max)) + (float(x_min))) / 2
    y_avg = ((float(y_max)) + (float(y_min))) / 2
    l_w = float(x_avg)
    l_h = float(y_avg)
    he_hf = height / 2
    wi_hf = width / 2
    ratio_width = ((width) - (x_min)) / (x_max-x_min)
    ratio_height = ((height) - (y_min)) / (y_max-y_min)
    if ratio_width > ratio_height:
        k = ratio_height * 0.5
    else:
        k = ratio_width * 0.5
    print("k = ", k, "h_f = ", he_hf, "wi_hf = ", wi_hf, "x_avg = ", x_avg, "y_avg", y_avg," l_w =", l_w, "h_w =", l_h)
    for i in range(len(f_1)):
        x1 = float(v_x[f_1[i]])
        y1 = float(v_y[f_1[i]])
        z1 = float(v_z[f_1[i]])
        x2 = float(v_x[f_2[i]])
        y2 = float(v_y[f_2[i]])
        z2 = float(v_z[f_2[i]])
        x3 = float(v_x[f_3[i]])
        y3 = float(v_y[f_3[i]])
        z3 = float(v_z[f_3[i]])
        print(x1, y1, z1, x2, y2, z2, x3, y3, z3)
        a = (y2-y1)*(z3-z1)-(z2-z1)*(y3-y1)
        b = -(x2-x1)*(z3-z1)+(z2-z1)*(x3-x1)
        c = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
        d = -x1*a - y1 * b - z1 * c
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
        first = np.array([x1, y1, z1, 1])
        second = np.array([x2, y2, z2, 1])
        third = np.array([x3, y3, z3, 1])

        rotation_angle = 45
        rotation_matrix = transformacije(ociste_x, ociste_y, ociste_z,
                        glediste_x, glediste_y, glediste_z)      
        result_first = np.dot(rotation_matrix, first)
        result_second = np.dot(rotation_matrix, second)
        result_third = np.dot(rotation_matrix, third)
        vertices.extend([
            (result_first[0] - l_w) * k + wi_hf, (result_first[1] - l_h) * k + he_hf,
            (result_second[0]- l_w) * k + wi_hf, (result_second[1] - l_h)* k + he_hf,
            (result_third[0] - l_w) * k + wi_hf, (result_third[1] - l_h) * k + he_hf
        ])
        
        pyglet.gl.glVertex2f((result_first[0] - l_w) * k + wi_hf, (result_first[1] - l_h) * k + he_hf)
        pyglet.gl.glVertex2f((result_second[0] - l_w) * k + wi_hf, (result_second[1] - l_h) * k + he_hf)

        pyglet.gl.glVertex2f((result_second[0] - l_w) * k + wi_hf, (result_second[1] - l_h) * k + he_hf)
        pyglet.gl.glVertex2f((x3 - l_w) * k + wi_hf, (y3 - l_h) * k + he_hf)

        pyglet.gl.glVertex2f((result_third[0] - l_w) * k + wi_hf, (result_third[1] - l_h) * k + he_hf)
        pyglet.gl.glVertex2f((result_first[0] - l_w) * k + wi_hf, (result_first[1] - l_h) * k + he_hf)

        pyglet.gl.glEnd()


@window.event
def on_display():
    glFlush()


@window.event
def on_resize(re_width, re_height):
    glViewport(0, 0, re_width, re_height)
    glMatrixMode(gl.GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(gl.GL_MODELVIEW)


def draw_stuff():
    x_min = min(v_x)
    x_max = max(v_x)
    y_min = min(v_y)
    y_max = max(v_y)
    x_avg = ((float(x_max)) + (float(x_min))) / 2
    y_avg = ((float(y_max)) + (float(y_min))) / 2
    l_w = float(x_avg)
    l_h = float(y_avg)
    he_hf = height / 2
    wi_hf = width / 2
    ratio_width = ((width) - (x_min)) / (x_max-x_min)
    ratio_height = ((height) - (y_min)) / (y_max-y_min)
    if ratio_width > ratio_height:
        k = ratio_height * 0.5
    else:
        k = ratio_width * 0.5
    print("k = ", k, "h_f = ", he_hf, "wi_hf = ", wi_hf, "x_avg = ", x_avg, "y_avg", y_avg," l_w =", l_w, "h_w =", l_h)
    for i in range(len(f_1)):
        x1 = float(v_x[f_1[i]])
        y1 = float(v_y[f_1[i]])
        z1 = float(v_z[f_1[i]])
        x2 = float(v_x[f_2[i]])
        y2 = float(v_y[f_2[i]])
        z2 = float(v_z[f_2[i]])
        x3 = float(v_x[f_3[i]])
        y3 = float(v_y[f_3[i]])
        z3 = float(v_z[f_3[i]])
        print(x1, y1, z1, x2, y2, z2, x3, y3, z3)
        a = (y2-y1)*(z3-z1)-(z2-z1)*(y3-y1)
        b = -(x2-x1)*(z3-z1)+(z2-z1)*(x3-x1)
        c = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
        d = -x1*a - y1 * b - z1 * c
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
        first = np.array([x1, y1, z1, 1])
        second = np.array([x2, y2, z2, 1])
        third = np.array([x3, y3, z3, 1])

        rotation_angle = 45
        rotation_matrix = transformacije(ociste_x, ociste_y, ociste_z,
                        glediste_x, glediste_y, glediste_z)      
        result_first = np.dot(rotation_matrix, first)
        result_second = np.dot(rotation_matrix, second)
        result_third = np.dot(rotation_matrix, third)
        vertices.extend([
            (result_first[0] - l_w) * k + wi_hf, (result_first[1] - l_h) * k + he_hf,
            (result_second[0]- l_w) * k + wi_hf, (result_second[1] - l_h)* k + he_hf,
            (result_third[0] - l_w) * k + wi_hf, (result_third[1] - l_h) * k + he_hf
        ])
        
        pyglet.gl.glVertex2f((result_first[0] - l_w) * k + wi_hf, (result_first[1] - l_h) * k + he_hf)
        pyglet.gl.glVertex2f((result_second[0] - l_w) * k + wi_hf, (result_second[1] - l_h) * k + he_hf)

        pyglet.gl.glVertex2f((result_second[0] - l_w) * k + wi_hf, (result_second[1] - l_h) * k + he_hf)
        pyglet.gl.glVertex2f((x3 - l_w) * k + wi_hf, (y3 - l_h) * k + he_hf)

        pyglet.gl.glVertex2f((result_third[0] - l_w) * k + wi_hf, (result_third[1] - l_h) * k + he_hf)
        pyglet.gl.glVertex2f((result_first[0] - l_w) * k + wi_hf, (result_first[1] - l_h) * k + he_hf)

        pyglet.gl.glEnd()


file = open("kocka.obj", "r")
read_all_lines(file)
# float(input("Give Y to check if in cube"))
draw_stuff()
'''tx = input("Give x")
ty = input("Give y")
tz = input("Give z") '''


pyglet.app.run()
