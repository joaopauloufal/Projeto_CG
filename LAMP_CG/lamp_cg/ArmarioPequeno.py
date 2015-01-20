#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Danilo Victor Barbosa da Costa


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


def eixos():
    glColor3f(.9, .1, .1)
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate( 0.0, 0.0, -2.0)
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .1, .9)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate( 0.0, 0.0, -2.0)
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .9, .1)
    glPushMatrix()
    glTranslate( 0.0, 0.0, -2.0)
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()


def desenho():
    global aux1
    global aux2
    global tec
    global girarPorta

    ##prancha de cima
    glColor(.8, .4, .4)
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
    glColor(.7, .4, .4)
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
    glPushMatrix()
    glColor(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(-1,0.5,-0.21)
    glPushMatrix()
    glScale(0.04, 0.5, 1)
    glutSolidCube(2)
    glPopMatrix()

    #maçaneta
    glColor(1,1,1)
    glRotate(90,0,0,1)
    glTranslate(-0.3,0.1,0.7)
    glutWireTorus(0.04,0.045,30,30)   # rosquinha
    glPopMatrix()

def portaDireita():
    #porta direita
#     glTranslate(-0.21,-0.5,0.6)
    glPushMatrix()
    glColor(0,0,0)
    glRotate(90,0,1,0)
    glPushMatrix()
    glScale(0.04, 0.5, 1)
    glutSolidCube(2)
    glPopMatrix()

    #maçaneta
    glColor(1,1,1)
    glRotate(90,0,0,1)
    glTranslate(0.3,0.1,0.7)
    glutWireTorus(0.04,0.045,30,30)   # rosquinha
    glPopMatrix()


def prancha():
    glPushMatrix()
    glScale(0.04, 1, 0.6)
    glutSolidCube(2)
    glPopMatrix()


def tela():
    global angulo

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(angulo,1,0.1,500)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(sin(esquerdaDireita) * 10, 0 + cimaBaixo ,cos(esquerdaDireita) * 10, aux1,aux2,0, 0,1,0) # Especifica posição do observador e do alvo
    glEnable(GL_DEPTH_TEST)

    desenho()
    glFlush()

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
    tela()
    glutPostRedisplay()

def TeclasEspeciais (tecla, x, y):
    global esquerdaDireita
    global cimaBaixo
    print("*** Tratamento de teclas especiais")
    print ("tecla: ", tecla)
    if tecla == GLUT_KEY_F1:
        print(">>> Tecla F1 pressionada")
    elif tecla == GLUT_KEY_F2:
        print(">>> Tecla F2 pressionada")
    elif tecla == GLUT_KEY_F3:
        print(">>> Tecla F3 pressionada")
    elif tecla == GLUT_KEY_LEFT:
        esquerdaDireita = esquerdaDireita - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esquerdaDireita = esquerdaDireita + 0.1
    elif tecla == GLUT_KEY_UP:
        cimaBaixo = cimaBaixo + 0.1
    elif tecla == GLUT_KEY_DOWN:
        cimaBaixo = cimaBaixo - 0.1
    else:
        print ("Apertou... " , tecla)
    tela()
    glutPostRedisplay()

def ControleMouse(button, state, x, y):
    global angulo
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if (angulo >= 10):
                angulo -= 2

    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()

global distancia
global cimaBaixo

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow(b"Aula01")
distancia = 20
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()


