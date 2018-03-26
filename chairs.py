from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    gluPerspective(60,1,.1,500)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glEnable(GL_DEPTH_TEST)

def draaw():

    #base-back
    glMatrixMode(GL_MODELVIEW)
    glColor(0,0,0)
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glScale(1,.2,1)
    glutSolidCube(3)

    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glTranslate(0,2.5,-1.3)
    glRotate(90,1,0,0)
    glScale(1,.2,1)
    glutSolidCube(3)


    glColor(.2294,.2294,.2294)
    #front legs
    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glTranslate(-1.28,-1.9,1.28)
    glScale(0.1,1,0.1)
    glutSolidCube(4)

    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glTranslate(1.28,-1.9,1.28)
    glScale(0.1,1,0.1)
    glutSolidCube(4)

    #back legs
    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glTranslate(1.28,0,-1.28)
    glScale(0.1,2,0.1)
    glutSolidCube(4)

    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glTranslate(-1.28,0,-1.28)
    glScale(0.1,2,0.1)
    glutSolidCube(4)
    glPopAttrib()
    glPopMatrix()
    glLoadIdentity()



def draw():
    glTranslate(3.5,0,0)
    draaw()
    glLoadIdentity()
    glTranslate(-5,0,0)
    draaw()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutInitDisplayMode(GLUT_DEPTH)
glutCreateWindow(b"lol")
myinit()
glutDisplayFunc(draw)

glutMainLoop()
