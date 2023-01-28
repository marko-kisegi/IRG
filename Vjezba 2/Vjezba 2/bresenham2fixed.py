from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

#window opening
width = 400
height = 400
window = pyglet.window.Window(width, height, caption='Bresenham', resizable=False)
triCol = [1.0, 0.0, 0.0]
ix = 0
lx = [0,0]
ly = [0,0]
linefull = []


@window.event
def on_mouse_press(x, y, button, modifiers):
    global triCol
    global lx
    global ly
    global linefull
    global width
    global height
    global ix
    if button == mouse.LEFT:
        linefull.append(x)
        linefull.append(y)
        if len(linefull) == 4:
            line(linefull[0], linefull[1], linefull[2], linefull[3])
            ix = ix + 1
            linefull = []
        print 'Dot coordinates:', ix, ' : ', x, y
        glFlush()
        if len(linefull) > 4:
            linefull.clear()
    elif button == mouse.RIGHT:
        lx = []
        ly = []




@window.event
def on_key_press(symbol, modifiers):
    global triCol
    if symbol == key.R:
        triCol[0] = 1.0
        triCol[1] = 0.0
        triCol[2] = 0.0
    if symbol == key.G:
        triCol[0] = 0.0
        triCol[1] = 1.0
        triCol[2] = 0.0
    if symbol == key.B:
        triCol[0] = 0.0
        triCol[1] = 0.0
        triCol[2] = 1.0
    if symbol == key.K:
        triCol[0] = 1.0
        triCol[1] = 1.0
        triCol[2] = 1.
    glRecti(width - 15, height-15, width, height)
    glFlush()

@window.event
def on_draw():
    global width, height, lx, ly, ix
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(triCol[0], triCol[1], triCol[2])
    glBegin(GL_POINTS)
    for i in range(len(lx)):
        glVertex2i(lx[i], ly[i])
    glEnd()

@window.event
def on_resize(re_width, re_height):
    global ix
    width = re_width
    height = re_height
    ix = 0
    glViewport(0, 0, width, height)
    glMatrixMode(gl.GL_PROJECTION)
    glLoadIdentity()
    gl.glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(gl.GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1.0)
    glColor3f(0.0, 0.0, 0.0)


@window.event
def on_display():
    glFlush()


def line(xa, ya, xb, yb):
    glBegin(GL_LINES)
    glVertex2i(xa, ya)
    glVertex2i(xb, yb)
    glEnd()
    if xa <= xb:
        if ya <= yb:
            bresenham1(xa, ya, xb, yb)
        else :
            bresenham2(xa, ya, xb, yb)
    else:
        if ya >= yb:
            bresenham1(xb, yb, xa, ya)
        else:
            bresenham2(xb, yb, xa, ya)


def bresenham1(xs, ys, xe, ye):
    global lx, ly
    if (ye-ys) <= (xe-xs):
        a = 2 * (ye-ys)
        yc = ys
        yf = -(xe - xs)
        korekcija = -2 * (xe-xs)
        for x in range(xs, xe):
            lx[ix].append(x)
            ly[ix].append(yc)
            yf = yf + a
            if yf >= 0:
                yf = yf + korekcija
                yc = yc + 1
    else:
        x = xe
        xe = ye
        ye = x
        x = xs
        xs = ys
        ys = x
        a = 2 * (ye - ys)
        yc = ys
        yf = -(xe - xs)
        korekcija = -2 * (xe - xs)
        for x in range(xs, xe):
            lx[ix].append(yc)
            ly[ix].append(x)
            yf = yf + a
            if  yf >= 0:
                yf = yf + korekcija
                yc = yc + 1


def bresenham2(xs, ys, xe, ye):
    global lx, ly
    if (-(ye - ys)) <= (xe-xs):
        a = 2 * (ye - ys)
        yc = ys
        yf = (xe - xs)
        korekcija = 2 * (xe - xs)
        for x in range(xs, xe):
            lx.append(x)
            ly.append(yc)
            yf = yf + a
            if yf <= 0:
                yf = yf + korekcija
                yc = yc - 1
    else:
        x = xe
        xe = ys
        ys = x
        x = xs
        xs = ye
        ye = x
        a = 2 * (ye - ys)
        yc = ys
        yf = xe - xs
        korekcija = 2 * (xe-xs)
        for x in range(xs, xe):
            lx[ix].append(yc)
            ly[ix].append(x)
            yf = yf + a
            if yf <= 0:
                yf = yf + korekcija
                yc = yc - 1



print('r,g,b,k mijenjaju boju')

pyglet.app.run()
