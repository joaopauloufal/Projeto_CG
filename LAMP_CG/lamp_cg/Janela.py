#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 25/01/2015

@author: grupoLAMP
'''

from math import cos
from math import pi
from math import sin
import timeit
import ctypes
import random
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def janela(eixoX, eixoY, eixoZ, angulo):

    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glRotate(angulo,0,1,0)
    glScale(0.8, 1.0, 1.0)

    #contorno em cima
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslate(0, 1.1, 0.04)
    glRotate(90,0,1,0)
    glRotate(90,1,0,0)
    glScale(0.08, 2.1, 0.09)
    glutSolidCube(2)
    glPopMatrix()

    #contorno na esquerda
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslate(2, 0, 0.04)
    glRotate(90,0,1,0)
    glRotate(90,1,0,0)
    glScale(0.08, 0.1, 1.1)
    glutSolidCube(2)
    glPopMatrix()

    #contorno na direita
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslate(-2, 0, 0.04)
    glRotate(90,0,1,0)
    glRotate(90,1,0,0)
    glScale(0.08, 0.1, 1.1)
    glutSolidCube(2)
    glPopMatrix()

    vidro(-0.5,0,0)
    vidro(0.5,0,0)
    vidro(-1.5,0,-0.06)
    vidro(1.5,0,-0.06)

    #contorno em baixo
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslate(0, -1.1, 0.04)
    glRotate(90,0,1,0)
    glRotate(90,1,0,0)
    glScale(0.08, 2.1, 0.09)
    glutSolidCube(2)
    glPopMatrix()

    glPopMatrix()


def vidro(eixoX, eixoY, eixoZ):


    #contorno em cima
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslate(eixoX, eixoY+1, eixoZ)
    glRotate(90,0,1,0)
    glRotate(90,1,0,0)
    glScale(0.025, 0.5, 0.03)
    glutSolidCube(2)
    glPopMatrix()

    #contorno na esquerda
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslate(eixoX-0.47, eixoY, eixoZ)
    glRotate(90,0,1,0)
    glRotate(90,1,0,0)
    glScale(0.025, 0.03, 1)
    glutSolidCube(2)
    glPopMatrix()

    #contorno na direita
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslate(eixoX+0.47, eixoY, eixoZ)
    glRotate(90,0,1,0)
    glRotate(90,1,0,0)
    glScale(0.025, 0.03, 1)
    glutSolidCube(2)
    glPopMatrix()

    #vidro
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslate(eixoX, eixoY, eixoZ)
    glRotate(90,0,1,0)
    glRotate(90,1,0,0)
    glScale(0.02, 0.5, 1)
    glutSolidCube(2)
    glPopMatrix()

    #contorno em cima
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslate(eixoX, eixoY-1, eixoZ)
    glRotate(90,0,1,0)
    glRotate(90,1,0,0)
    glScale(0.025, 0.5, 0.03)
    glutSolidCube(2)
    glPopMatrix()
