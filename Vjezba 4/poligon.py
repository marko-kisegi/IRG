import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window(400, 400, caption='Poligoni', resizable=True)
peak_x = []
peak_y = []

a = []
b = []
c = []
n = 5
print("Enter coordinates of peaks using the mouse in clockwise direction")
entered_peaks = 0
batch = pyglet.graphics.Batch()
v_x = [0]
v_y = [0]


@window.event
def on_mouse_press(x, y, button, modifiers):
    global entered_peaks
    if button == mouse.LEFT:
        if entered_peaks < n:
            peak_x.append(x)
            peak_y.append(y)
            entered_peaks = entered_peaks + 1
            if entered_peaks == n:
                polygon_drawing()
        else:
            v_x[0] = x
            v_y[0] = y
            print(v_x, v_y)
            is_inside_polygon(v_x[0], v_y[0])
        print(peak_x)
        print(peak_y)
    if button == mouse.RIGHT:
        fill_polygon()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.H:
        print("HELLO THERE")
    glFlush()


@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    batch.draw()


@window.event
def on_display():
    glFlush()


@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(gl.GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(gl.GL_MODELVIEW)


def is_inside_polygon(x1, y1):
    dot_inside = False
    for i in range(n):
        if (x1 * a[i] + y1 * b[i] + c[i]) > 0:
            dot_inside = True
            break
    if dot_inside:
        print("Dot is outside.")
    else:
        print("Dot is inside")


def fill_polygon():
    y_min = min(peak_y)
    y_max = max(peak_y)
    x_min = min(peak_x)
    x_max = max(peak_x)
    for yo in range(y_min, y_max):
        left = x_min
        right = x_max
        for i in range(n):
            if a[i] != 0:
                x1 = (-b[i] * yo - c[i]) / a[i]
                if peak_y[i] < peak_y[i+1]:
                    if x1 > left:
                        left = int(x1)
                if peak_y[i] >= peak_y[i+1]:
                    if x1 < right:
                        right = int(x1)
        if left < right:
            batch.add(2, pyglet.gl.GL_LINES, None,
                      ('v2i', (left, yo, right, yo)),
                      )


def polygon_drawing():
    peak_x.append(peak_x[0])
    peak_y.append(peak_y[0])
    for i in range(n):
        batch.add(2, pyglet.gl.GL_LINES, None,
                  ('v2i', (peak_x[i], peak_y[i], peak_x[i+1], peak_y[i+1])),
                  )
    for i in range(n):
        a.append(peak_y[i] - peak_y[i+1])
        b.append(-peak_x[i] + peak_x[i+1])
        c.append(peak_x[i] * peak_y[i+1] - peak_x[i+1] * peak_y[i])


pyglet.app.run()
