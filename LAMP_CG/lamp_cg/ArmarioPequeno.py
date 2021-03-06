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
from TV import *

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


def armarioPequeno(eixoX, eixoY, eixoZ, verificaTV, rotacao):
    global aux1
    global aux2
    global tec
    global girarPorta

    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glScale(0.7, 0.6, 0.7)
    glRotate(rotacao, 0, 1, 0)

    if (verificaTV == True):
        tv(0,1.6,0)
        glColor3f(0.87, 0.72, 0.53)
    else:
        glColor3f(0.8, 0.8, 0.8)



    ##prancha de cima
    glRotate(90, 0,0,1)
    glPushMatrix()
    glTranslate(0.75,0,0)
    prancha()

    #prancha de baixo
    glTranslate(-2,0,0)
    prancha()
    glPopMatrix()


    glPushMatrix()
    glTranslate(-0.3,0,0)
    prancha()
    glPopMatrix()


    ##prancha esquerda
    glPushMatrix()
    glRotate(90, 0,0,1)
    glTranslate(1,0.21,0)
    prancha()
    glTranslate(-2,0,0)
    prancha()
    glPopMatrix()

    #prancha de trás
    glPushMatrix()
    glRotate(90,0,1,0)
    glTranslate(0.6,0.0,-0.25)
    glScalef(1,1,1.7)
    prancha()
    glPopMatrix()

    glTranslate(-0.21,-0.5,0.6)
    if girarPorta == 120:
        glRotate(girarPorta,1,0,0)
        glTranslate(0.0,0.5,0.0)
    portaDireita()
    glTranslate(0.2,0.5,-1)
    if girarPorta == 120:
        glRotate(girarPorta,1,0,0)
        glTranslate(0,-0.5,0.4)
    portaEsquerda()


def portaEsquerda():
    #porta esquerda
#     glColor3f(0.87, 0.72, 0.53)
    glPushMatrix()
    glRotate(90,0,1,0)
    glTranslate(-1,0.5,-0.21)
    glPushMatrix()
    glScale(0.04, 0.5, 1)
    glutSolidCube(2)
    glPopMatrix()

    #maçaneta
    glRotate(90,0,0,1)
    glTranslate(-0.3,0.1,0.7)
    glutWireTorus(0.04,0.045,30,30)   # rosquinha
    glPopMatrix()
    glPopMatrix()

def portaDireita():
    #porta direita
#     glColor3f(0.87, 0.72, 0.53)
    glPushMatrix()
    glRotate(90,0,1,0)
    glPushMatrix()
    glScale(0.04, 0.5, 1)
    glutSolidCube(2)
    glPopMatrix()

    #maçaneta
    glRotate(90,0,0,1)
    glTranslate(0.3,0.1,0.7)
    glutWireTorus(0.04,0.045,30,30)   # rosquinha
    glPopMatrix()


def prancha():
    glPushMatrix()
    glScale(0.04, 1, 0.6)
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
