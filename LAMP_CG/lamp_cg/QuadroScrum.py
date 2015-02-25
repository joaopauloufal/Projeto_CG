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
import numpy
from sys import argv
import time
from Textura import *


texturaScrumA = Image.open("images/quadroScrumA.png", "r")
texturaScrumB = Image.open("images/quadroScrumB.png", "r")


def quadroScrum(eixoX, eixoY, eixoZ, rotacao, imagem):
    glPushMatrix()
    glRotate(rotacao, 0, 1, 0)

    glColor3f(0.87, 0.72, 0.53)
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glScale(3, 2, 0.2)
    glutSolidCube(0.5)
    glPopMatrix()

        #textura parede1
    glPushMatrix()
    if (imagem == True):
        carrega_imagem(texturaScrumA)
    else:
        carrega_imagem(texturaScrumB)
    glEnable(GL_TEXTURE_2D)
    glTranslate(eixoX, eixoY, eixoZ-0.653)
    glRotate(-90, 0, 1, 0)
    glScalef(0.71, 0.5, 0.75)
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)

    glTexCoord2f(1.0, 1.0)
    glVertex3f( 1.0,  1.0, -1.0)

    glTexCoord2f(0.0, 1.0)
    glVertex3f( 1.0,  1.0,  1.0)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0,  1.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

    glPopMatrix()





