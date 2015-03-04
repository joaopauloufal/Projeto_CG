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

from Porta import *
from Textura import *


textura1 = None
texturaPiso = Image.open("images/piso.jpg", "r")
texturaParedes = Image.open("images/parede_branca.jpg", "r")
texturaPonto = Image.open("images/pontoEletronico.png", "r")



def ambiente():
    global textura1
    #piso
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate(-2.00, -0.82, 0.0)  #Transtaçao do objeto
    glScale(16.5, 0.2, 9.0)
    glutSolidCube(0.9)
    glPopMatrix()

    #parede1
    #carrega_imagem()
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    #glEnable(GL_TEXTURE_2D)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate(-2.0, 3.975, -1.9)  #Transtaçao do objeto
    glScale(16.4, 0.2, 5.9)
    glutSolidCube(0.9)
    glPopMatrix()
    #glDisable(GL_TEXTURE_2D)


    #parede2
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate(-2.0, -3.975, -1.9)  #Transtaçao do objeto
    glScale(16.4, 0.2, 5.9)
    glutSolidCube(0.9)
    glPopMatrix()

    #parede3
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glTranslate(1.9, 9.28, 0.0)  #Transtaçao do objeto
    glScale(5.9, 0.2, 9.0)
    glutSolidCube(0.9)
    glPopMatrix()

    #parede4 parte grande
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glTranslate(1.9, -5.50, -0.9)  #Transtaçao do objeto
    glScale(5.9, 0.2, 6.8)
    glutSolidCube(0.9)
    glPopMatrix()

    #parede4 parte pequena
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glTranslate(3.7, -5.50, 3.0)  #Transtaçao do objeto
    glScale(1.8, 0.2, 2.2)
    glutSolidCube(0.9)
    glPopMatrix()

#     Ar
    glColor3f(1, 1, 1) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glTranslate(3.9, 9.0, 0.0)  #Transtaçao do objeto
    glScale(0.6, 0.55, 2.5)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(0.01, 0.01, 0.01) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glTranslate(3.9, 8.75, 0.0)  #Transtaçao do objeto
    glScale(0.05, 0.02, 2.5)
    glutSolidCube(0.9)
    glPopMatrix()

    porta(5.35,1.09,3.0,90)

    #textura parede1
    glPushMatrix()

    carrega_imagem(texturaParedes)
    glEnable(GL_TEXTURE_2D)
    glTranslate(-1.9, 2.0, 3.88)
    glRotate(90, 0, 1, 0)
    glScalef(0, 2.8, 7.28)
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

    #textura parede2
    glPushMatrix()
    carrega_imagem(texturaParedes)
    glEnable(GL_TEXTURE_2D)
    glTranslate(-1.9, 2.0, -3.88)
    glRotate(90, 0, 1, 0)
    glScalef(0, 2.8, 7.28)
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

    #textura parede3
    glPushMatrix()
    carrega_imagem(texturaParedes)
    glEnable(GL_TEXTURE_2D)
    glTranslate(-9.18, 2.0, 0)
    #glRotate(90, 0, 1, 0)
    glScalef(0, 2.8, 4)
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

    #textura parede4 parte grande
    glPushMatrix()
    carrega_imagem(texturaParedes)
    glEnable(GL_TEXTURE_2D)
    glTranslate(5.35, 1.9, -0.95)  #Transtaçao do objeto
    #glRotate(90, 0, 1, 0)
    glScalef(0, 2.55, 3.1)
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

    #textura parede4 parte pequena
    glPushMatrix()
    carrega_imagem(texturaParedes)
    glEnable(GL_TEXTURE_2D)
    glTranslate(5.35, 3.7, 2.9)  #Transtaçao do objeto
    #glRotate(90, 0, 1, 0)
    glScalef(0, 0.8, 1.1)
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


    #textura piso
    glPushMatrix()
    carrega_imagem(texturaPiso)
    glEnable(GL_TEXTURE_2D)
    glTranslate(-1.9, -0.72, 0)
    glRotate(90, 0, 0, 1)
    glScalef(0, 7.35, 4)
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

    #teto
    glColor3f(1, 1, 1) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate(-2.00, 4.5, 0.0)  #Transtaçao do objeto
    glScale(16.5, 0.2, 9.0)
    glutSolidCube(0.9)
    glPopMatrix()


def quadroBranco(eixoX, eixoY, eixoZ, angulo):
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glRotatef(angulo, 0.0, 1.0, 0.0)     #Rotaçao do objeto

    glColor3f(1, 1, 1) # cor RGB  eixo X
    glPushMatrix()
    glScale(0.08, 2.1, 4.5)
    glutSolidCube(0.9)
    glPopMatrix()

    glPopMatrix()

def ponto(eixoX, eixoY, eixoZ, angulo):
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glRotatef(angulo, 0.0, 1.0, 0.0)     #Rotaçao do objeto

    glColor3f(0.01, 0.01, 0.01) # cor RGB  eixo X
    glPushMatrix()
    glScale(0.08, 0.35, 0.35)
    glutSolidCube(0.9)
    glPopMatrix()

    #textura piso
    glPushMatrix()
    carrega_imagem(texturaPonto)
    glEnable(GL_TEXTURE_2D)
    glTranslate(-0.06, 0, 0)
#     glRotate(90, 0, 0, 1)
    glScalef(0, 0.15, 0.15)
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