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

global esquerdaDireita
global cimaBaixo
global aux1
global aux2
global angulo


esquerdaDireita = 0
cimaBaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 30
girarPorta = 0


def janela(eixoX, eixoY, eixoZ):
    global aux1
    global aux2
    global tec
    global girarPorta

    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
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
