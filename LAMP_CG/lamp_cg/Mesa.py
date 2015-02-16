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


def mesa(eixoX, eixoY, eixoZ, rotacao):
    glPushMatrix()
    glRotatef(rotacao, 1.0, 0.0, 0.0)
    glTranslate(eixoX, eixoY, eixoZ)
    glColor(0.7,0.7,0.7)

    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.9, 0.05, 0.0)  #Transtaçao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScalef(0.06,0.6,0.75)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( -0.9, 0.05, 0.0)  #Transtaçao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScalef(0.06,0.6,0.75)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    glPushMatrix()
    glTranslate(0, 0.8, 0.0)
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(1.0,0.05,1.5)
    glutSolidDodecahedron()
    glPopMatrix()


    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.0, 0.2, -0.1)  #Transtaçao do objeto
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.06,0.9,0.3)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    glPopMatrix()







