#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Danilo Victor Barbosa da Costa

'''
Created on 13/01/2015

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

global aux1
global aux2
global angulo


aux1 = 0
aux2 = 0
angulo = 30
girarPorta = 0


def ventilador(eixoX, eixoY, eixoZ):
    glPushMatrix()
    glRotatef(-90, 1.0, 0.0, 0.0)
    glTranslate(eixoX, eixoY, eixoZ)
    glScalef(0.6,0.6,0.6)

    glColor3f(0.8, 0.8, 0.8)
    glPushMatrix()
    glTranslate(0, 0, 0)
    glutSolidCylinder(0.5, 0.2, 30, 30)
    glPopMatrix()

    glPushMatrix()
    glRotatef(15, 1.0, 0.0, 0.0)
    glTranslate(0, 0, 0.1)
    glScalef(2.8,0.4,0.05)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)
    glRotatef(15, 1.0, 0.0, 0.0)
    glTranslate(0, 0, 0.1)
    glScalef(2.8,0.4,0.05)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.8, 0.8, 0.8)
    glPushMatrix()
    glTranslate(0, 0, 0.1)
    glutSolidCylinder(0.05, 1.2, 30, 30)
    glPopMatrix()

    glPopMatrix()

