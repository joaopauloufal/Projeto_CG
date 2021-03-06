# -*- encoding: utf-8 -*-
# Autor: João Paulo Ferreira da Silva
#        Danilo Victor Barbosa da Costa
#        Roberto Bartolomeu
'''
 ====== LAMP ===
 Projeto de Computação Gráfica
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image, ImageFilter
import PIL
import ctypes
from math import cos
from math import pi
from math import sin
# import numpy
from sys import argv
import time
from Textura import *

global aux1
global aux2
global angulo


aux1 = 0
aux2 = 0
angulo = 30
girarPorta = 0


def armarioGrande(eixoX, eixoY, eixoZ):
    global aux1
    global aux2
    global tec
    global girarPorta

    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glScale(0.8, 0.8, 0.8)
    glRotate(180, 1, 0, 0)
    glColor3f(0.86, 0.86, 0.86)
    #parte de tras
    glPushMatrix()
    glRotate(90,0,1,0)

    glTranslate(1,0.3,0.0)
    glScale(1, 1.06, 1)
    prancha()
    glPopMatrix()

    #Lado direito
    glPushMatrix()

    glTranslate(1.1,0.3,-0.5)
    glScale(0.5, 1.06, 0.5)
    prancha()
    glPopMatrix()

    #Lado esquerdo
    glPushMatrix()

    glTranslate(-1.1,0.3,-0.5)
    glScale(0.5, 1.06, 0.5)
    prancha()
    glPopMatrix()

    #pranchas
    glPushMatrix()
    glTranslate(0,-1.1,0)
    for i in range(0, 5):
        glPushMatrix()

        glRotate(90,0,0,1)
        glTranslate((i-0.6),0.0,-0.5)
        glScale(0.5, 0.58, 0.5)
        prancha()
        glPopMatrix()
    glPopMatrix()

    #portas
    glPushMatrix()
    glTranslate(-0.75,-1.2,0)
    for i in range(0, 4):
        for j in range(0, 3):
            glPushMatrix()

            glRotate(90,0,1,0)
            glTranslate(-0.089,(i),(j*0.75))
            glScale(0.27, 0.27, 0.33)
            portaEsquerda()
            glPopMatrix()
    glPopMatrix()


    #Coluna entre portas esquerda
    glPushMatrix()

    glTranslate(-0.376,0.29,0.06)
    glScale(0.02, 0.97, 0.01)
    glutSolidCube(4)
    glPopMatrix()

    #Coluna entre portas direita
    glPushMatrix()

    glTranslate(0.376,0.29,0.06)
    glScale(0.02, 0.97, 0.01)
    glutSolidCube(4)
    glPopMatrix()
    glPopMatrix()

def portaEsquerda():
    #porta esquerda
    glPushMatrix()
    glColor3f(0.86, 0.86, 0.86)
    glPushMatrix()
    glScale(0.04, 1.8, 1)
    glutSolidCube(2)
    glPopMatrix()

    #maçaneta
    glColor(1,1,1)
    glRotate(90,0,0,1)
    glTranslate(-0.3,0.1,0.7)
    glutWireTorus(0.04,0.045,30,30)   # rosquinha
    glPopMatrix()


def prancha():
    glPushMatrix()
    glScale(0.04, 1, 0.6)
    glutSolidCube(3.8)
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
