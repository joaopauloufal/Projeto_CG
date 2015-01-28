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
    glTranslate(eixoX, eixoY, eixoZ)

    glColor3f(0.09, 0.09, 0.09)
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glutSolidCylinder(0.5, 0.1, 30, 30)
    glPopMatrix()

    glPopMatrix()


def Teclado (tecla, x, y):
    global aux1
    global aux2
    global tempoesteira
    global fire
    global angulocanhao
    global girarPorta

    print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ",tecla)

    if tecla==chr(27): # ESC ?
        sys.exit(0)

    if tecla == b'a':
        girarPorta = 120
    if tecla == b'f':
        girarPorta = -120
#     tela()
    glutPostRedisplay()
