from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
x=0
f=True
z=0
h=0
def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    gluPerspective(60,1,.1,500)
    gluLookAt(-40,40,0,0,0,0,1,0,0)
    glEnable(GL_DEPTH_TEST)




def draw():
    global x,f,z,h
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glColor(.5,1,.5)
    glRotate(-90,1,0,0)
    glutSolidCone(10,10,50,50)
    glColor(.7,.3,1)
    glLoadIdentity()
    glBegin(GL_LINE_LOOP)
    for theta in np.arange(0,2*pi,0.01):
        a=24 * cos(theta)
        b=24 * sin(theta)
        glVertex(a,0,b)
    glEnd()
    glBegin(GL_LINE_LOOP)
    for theta in np.arange(0,2*pi,0.01):
        a=17 * cos(theta)
        b=17 * sin(theta)
        glVertex(a,0,b)
    glEnd()

    glColor(1,0,0)
    glLoadIdentity()
    glTranslate(17,0,0)
    glRotate(-90,1,0,0)
    glutSolidCone(1,2,15,15)

    glLoadIdentity()
    glRotate(36,0,1,0)
    glTranslate(24,0,0)
    glRotate(-90,1,0,0)
    glutSolidCone(1,2,15,15)

    glLoadIdentity()
    glRotate(h,0,1,0)
    h+=72
    glTranslate(17,0,0)
    glRotate(-90,1,0,0)
    glutSolidCone(1,2,15,15)

    glLoadIdentity()
    glRotate(h+36,0,1,0)
    glTranslate(24,0,0)
    glRotate(-90,1,0,0)
    glutSolidCone(1,2,15,15)

    glLoadIdentity()
    glRotate(h,0,1,0)
    h+=72
    glTranslate(17,0,0)
    glRotate(-90,1,0,0)
    glutSolidCone(1,2,15,15)

    glLoadIdentity()
    glRotate(h+36,0,1,0)
    glTranslate(24,0,0)
    glRotate(-90,1,0,0)
    glutSolidCone(1,2,15,15)

    glLoadIdentity()
    glRotate(h,0,1,0)
    h+=72
    glTranslate(17,0,0)
    glRotate(-90,1,0,0)
    glutSolidCone(1,2,15,15)

    glLoadIdentity()
    glRotate(h+36,0,1,0)
    glTranslate(24,0,0)
    glRotate(-90,1,0,0)
    glutSolidCone(1,2,15,15)

    glLoadIdentity()
    glRotate(h,0,1,0)
    h+=72
    glTranslate(17,0,0)
    glRotate(-90,1,0,0)
    glutSolidCone(1,2,15,15)

    glLoadIdentity()
    glRotate(h+36,0,1,0)
    glTranslate(24,0,0)
    glRotate(-90,1,0,0)
    glutSolidCone(1,2,15,15)
    h=0
    #kber
    glLoadIdentity()
    glColor3f(1,0,0)
    glRotate(x,0,1,0)
    glTranslate(0,1.1,20)
    glScale(1,.25,.5)
    glutWireCube(5)
#so8ayr
    glLoadIdentity()
    glColor3f(.5,.5,1)
    glRotate(x,0,1,0)
    glTranslate(0,1.1,20)
    glTranslate(0,1.25,0)
    glScale(.5,.25,.5)
    glutWireCube(5)

    glColor(1,0,1)
    glLoadIdentity()
    glRotate(x,0,1,0)
    glTranslate(0,1.1,20)
    glTranslate(2,-.5,1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)

    glLoadIdentity()
    glRotate(x,0,1,0)
    glTranslate(-2,-.5,-1.25)
    glTranslate(0,1.1,20)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)

    glLoadIdentity()
    glRotate(x,0,1,0)
    glTranslate(0,1.1,20)
    glTranslate(2,-.5,-1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)

    glLoadIdentity()
    glRotate(x,0,1,0)
    glTranslate(0,1.1,20)
    glTranslate(-2,-.5,1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)


    glColor(1,1,0)
    glLoadIdentity()
    glRotate(x,0,1,0)
    glTranslate(0,1.1,20)
    glTranslate(2.2,-.3,.4)
    glScale(.25,1,1)
    glutSolidSphere(.3,20,20)

    glLoadIdentity()
    glRotate(x,0,1,0)
    glTranslate(0,1.1,20)
    glTranslate(2.2,-.3,-.4)
    glScale(.25,1,1)
    glutSolidSphere(.3,20,20)

    x+=.25
    z+=10
    if x==360:
        z=0
        x=0
    glLoadIdentity()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutInitDisplayMode(GLUT_DEPTH)
glutCreateWindow(b"looool")
myinit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

