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


def tv(eixoX, eixoY, eixoZ):
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glScalef(0.5,0.5,0.5)


    glColor3f(0.8, 0.8, 0.8)
    glPushMatrix()
    glTranslate(0, 1.5, 0)
    glScalef(4.0,0.4,2.0)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-1.8, 0, 0)
    glScalef(0.4,3.0,2.0)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(1.8, 0, 0)
    glScalef(0.4,3.0,2.0)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0, -1.5, 0)
    glScalef(4.0,0.4,2.0)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0, 0.0, -0.65)
    glScalef(1.7,1.3,1.5)
    glutSolidCube(2.0)
    glPopMatrix()

    glColor3f(0.9, 0.1, 0.1)
    glPushMatrix()
    glTranslate(0.8, -1.45, 1)
    glutSolidCylinder(0.04, 0.02, 30, 30)
    glPopMatrix()

    glColor3f(0.09, 0.09, 0.09)
    glPushMatrix()
    glTranslate(0.6, -1.45, 1)
    glutSolidCylinder(0.05, 0.03, 30, 30)
    glPopMatrix()

    glColor3f(0.09, 0.09, 0.09)
    glPushMatrix()
    glTranslate(0.4, -1.45, 1)
    glutSolidCylinder(0.05, 0.02, 30, 30)
    glPopMatrix()

    glColor3f(0.09, 0.09, 0.09)
    glPushMatrix()
    glTranslate(0.2, -1.45, 1)
    glutSolidCylinder(0.05, 0.02, 30, 30)
    glPopMatrix()

    glColor3f(0.09, 0.09, 0.09)
    glPushMatrix()
    glTranslate(0.0, -1.45, 1)
    glutSolidCylinder(0.05, 0.02, 30, 30)
    glPopMatrix()



    glPopMatrix()
















