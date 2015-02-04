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


def armarioImpressora(eixoX, eixoY, eixoZ):
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)

#     glColor3f(0.87, 0.72, 0.53)
#     glPushMatrix()
#     glTranslate(-1.1, 0, 0)
#     glScalef(0.1,2.5,1.6)
#     glutSolidCube(1)
#     glPopMatrix()
#
#     glPushMatrix()
#     glRotatef(90, 0.0, 0.0, 1.0)
#     glTranslate(1.3, 0, 0)
#     glScalef(0.1,2.3,1.6)
#     glutSolidCube(1)
#     glPopMatrix()
#
#     gaveta(0, 0.63, 0)
#     gaveta(0, -0.63, 0)
#
#     glPushMatrix()
#     glTranslate(1.1, 0, 0)
#     glScalef(0.1,2.5,1.6)
#     glutSolidCube(1)
#     glPopMatrix()
#
#     glPushMatrix()
#     glRotatef(90, 0.0, 0.0, 1.0)
#     glTranslate(-1.3, 0, 0)
#     glScalef(0.1,2.3,1.6)
#     glutSolidCube(1)
#     glPopMatrix()
#
#     glPushMatrix()
#     glRotatef(90, 0.0, 1.0, 0.0)
#     glTranslate(0.75, 0, 0)
#     glScalef(0.1,2.5,2.2)
#     glutSolidCube(1)
#     glPopMatrix()

    impressora(0,0,0)

    glPopMatrix()

def gaveta(eixoX, eixoY, eixoZ):
    glColor3f(0.87, 0.72, 0.53)
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)

    glPushMatrix()
    glTranslate(-1, 0, 0)
    glScalef(0.1,1.2,1.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(1, 0, 0)
    glScalef(0.1,1.2,1.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)
    glTranslate(-0.55,0, 0)
    glScalef(0.1,1.9,1.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(0.71,0, 0)
    glScalef(0.1,1.9,1.2)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-0.71,0, 0)
    glScalef(0.1,2.1,1.2)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0,0.8, 0)
    glScalef(2.0,1.0,0.5)
    glutWireTorus(0.04,0.12,30,30)   # rosquinha
    glPopMatrix()

    glPopMatrix()

def impressora(eixoX, eixoY, eixoZ):
    glColor3f(0.9, 0.9, 0.9)
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)

    glPushMatrix()
    glTranslate(-1, 0, 0)
    glScalef(0.1,1.2,1.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(1, 0, 0)
    glScalef(0.1,1.2,1.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)
    glTranslate(-0.55,0, 0)
    glScalef(0.1,1.9,1.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(0.71,0, 0)
    glScalef(0.1,1.9,1.2)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-0.71,0, 0)
    glScalef(0.1,2.1,1.2)
    glutSolidCube(1)
    glPopMatrix()



    glPopMatrix()
