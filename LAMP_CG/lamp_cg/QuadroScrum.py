from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import ctypes
from math import cos
from math import pi
from math import sin
# from numpy import angle
from sys import argv

def quadroScrum(eixoX, eixoY, eixoZ):
    glColor3f(0.87, 0.72, 0.53)
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glScale(3, 2, 0.2)
    glutSolidCube(0.5)
    glPopMatrix()