# -*- encoding: utf-8 -*

'''
Created on 13/01/2015

@author: grupoLAMP
'''
import Image
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import ctypes
from math import cos
from math import pi
from math import sin
from sys import argv
from Textura import *


# from numpy import angle
texturaTela = Image.open("images/ubuntu.png", "r")

def mesa():
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0, 0, 0)  #Transtaçao do objeto

    # OBJETO 1  mesa (parte do direito)
    glColor3f(.6, 0.3, 0.2) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.9, 0.0, 0.0)  #Transtaçao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScalef(0.06,0.6,0.9)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    # OBJETO 2  mesa (parte do esquerdo)
    glColor3f(.6, 0.3, 0.2) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( -0.9, 0.0, 0.0)  #Transtaçao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScalef(0.06,0.6,0.9)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    # OBJETO 3  mesa (parte de cima)
    glColor3f(.6, 0.3, 0.2) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.0, 0.835, -0.2)  #Transtaçao do objeto
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glScalef(0.06,0.9,0.4)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    # OBJETO 4  mesa (teclado)
    glColor3f(.6, 0.3, 0.2) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.0, 0.675, 0.3)  #Transtaçao do objeto
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glScalef(0.06,0.9,0.3)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    # OBJETO 5  mesa (parte de trás)
    glColor3f(.6, 0.3, 0.2) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.0, 0.5, -0.54)  #Transtaçao do objeto
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.06,0.9,0.3)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    glPopMatrix()

def mesaProf(eixoX, eixoY, eixoZ):
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(eixoX, eixoY, eixoZ)  #Transtaçao do objeto
    glColor3f(.8, 0.8, 0.8) # cor RGB

    # OBJETO 1  mesa (parte do direito)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.9, 0.05, 0.0)  #Transtaçao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScalef(0.06,0.6,0.75)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    # OBJETO 2  mesa (parte do esquerdo)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( -0.9, 0.05, 0.0)  #Transtaçao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScalef(0.06,0.6,0.75)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    # OBJETO 3  mesa (parte de cima)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.0, 0.835, 0.0)  #Transtaçao do objeto
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glScalef(0.06,1.5,0.8)
    glutSolidCube(2)  #1cm
    glPopMatrix()


    # OBJETO 5  mesa (parte de trás)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.0, 0.2, -0.1)  #Transtaçao do objeto
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.06,0.9,0.3)
    glutSolidCube(2)  #1cm
    glPopMatrix()

    glPopMatrix()



def cadeira():
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0, -0.22 ,1)  #Transtaçao do objeto
    #base de sustentação
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(0, 0, 0.1)
    glutSolidCylinder(0.05, 0.5, 10, 10)
    glPopMatrix()

    #assento
    glColor3f(0, 0, 1)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glutSolidCylinder(0.4, 0.1, 15, 10)
    glPopMatrix()

    #barra1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(-0.1, 0.4, -0.7)
    glutSolidCylinder(0.04, 0.8, 10, 10)
    glPopMatrix()

    #barra2
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(0.1, 0.4, -0.7)
    glutSolidCylinder(0.04, 0.8, 10, 10)
    glPopMatrix()

    #barra3
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(-0.4, 0.72, -0.15)
    glutSolidCylinder(0.04, 0.3, 10, 10)
    glPopMatrix()

    #apoio
    glColor3f(0, 0, 1)
    glPushMatrix()
    glRotatef(90, 0, 0, 0)
    glTranslate(0, 0.7, 0.28)
    glutSolidCylinder(0.35, 0.05, 15, 10)
    glPopMatrix()

    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 0, 0)
    glTranslate(0, 0.7, 0.33)
    glutSolidCylinder(0.35, 0.05, 15, 10)
    glPopMatrix()

    #braço1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(0.0, 0.21, 0.3)
    glutSolidTorus(.025, 0.3, 40, 40, 40)
    glPopMatrix()

    #braço2
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(0.0, 0.21, -0.3)
    glutSolidTorus(.025, 0.3, 40, 40, 40)
    glPopMatrix()

    #pé1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(0, -0.65, -0.5)
    glutSolidCylinder(0.05, 1, 10, 10)
    glPopMatrix()

    #pé2
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 0, 0)
    glTranslate(0, -0.65, -0.5)
    glutSolidCylinder(0.05, 1, 10, 10)
    glPopMatrix()

    glPopMatrix()

def cadeiraPreta(eixoX, eixoY, eixoZ, angulo):
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(eixoX, eixoY, eixoZ)  #Transtaçao do objeto
    glRotatef(angulo, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    #base de sustentação
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(0, 0, 0.1)
    glutSolidCylinder(0.05, 0.5, 10, 10)
    glPopMatrix()

    #assento
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(0.0, 0.0, 0.1)
    glScalef(1.8,1.5,0.2)
    glutSolidCube(0.5)
    glPopMatrix()

    #barra1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(0.0, 0.4, -0.7)
    glutSolidCylinder(0.04, 0.8, 10, 10)
    glPopMatrix()


    #apoio
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 0, 0)
    glTranslate(0, 0.7, 0.33)
    glScalef(1.5,1.4,0.15)
    glutSolidCube(0.5)
    glPopMatrix()

    #pé1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(0, -0.65, -0.5)
    glutSolidCylinder(0.05, 1, 10, 10)
    glPopMatrix()

    #pé2
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 0, 0)
    glTranslate(0, -0.65, -0.5)
    glutSolidCylinder(0.05, 1, 10, 10)
    glPopMatrix()

    glPopMatrix()

def cadeiraProfessor(eixoX, eixoY, eixoZ, angulo):
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(eixoX, eixoY, eixoZ)  #Transtaçao do objeto
    glRotatef(angulo, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    #base de sustentação
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(0, 0, 0.1)
    glutSolidCylinder(0.05, 0.5, 10, 10)
    glPopMatrix()

    #assento
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(0.0, 0.0, 0.1)
    glScalef(1.8,1.5,0.2)
    glutSolidCube(0.5)
    glPopMatrix()

    #barra1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(0.0, 0.4, -0.7)
    glutSolidCylinder(0.04, 0.8, 10, 10)
    glPopMatrix()


    #apoio
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 0, 0)
    glTranslate(0, 0.55, 0.33)
    glScalef(1.5,2.1,0.15)
    glutSolidCube(0.5)
    glPopMatrix()

    #braço1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(0.0, 0.21, 0.5)
    glutSolidTorus(.025, 0.3, 40, 40, 40)
    glPopMatrix()

    #braço2
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(0.0, 0.21, -0.5)
    glutSolidTorus(.025, 0.3, 40, 40, 40)
    glPopMatrix()

    #pé1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(0, -0.65, -0.5)
    glutSolidCylinder(0.05, 1, 10, 10)
    glPopMatrix()

    #pé2
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 0, 0)
    glTranslate(0, -0.65, -0.5)
    glutSolidCylinder(0.05, 1, 10, 10)
    glPopMatrix()

    glPopMatrix()

def computador(verifica):
    glPushMatrix()
    glPushMatrix()
    carrega_imagem(texturaTela)
    glEnable(GL_TEXTURE_2D)
    glTranslate(0, 1.42, 0.033)
    glRotate(270, 0, 1, 0)
    glScalef(0, 0.27, 0.32)
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

    glPushMatrix()
    glRotate(90, 0, 1, 0)
    glScale(0.65, 0.65, 0.65)
    glTranslate(-3, 2.17, 0)

    #monitor
    glColor3f(0, 0, 0)
    glPushMatrix()
    glTranslate(3, 0, 0)
    glScale(0.1, 1, 1.2)
    glutSolidCube(1.0)
    glPopMatrix()
    if (verifica):
        glColor3f(0.87, 0.72, 0.53)
        glPushMatrix()
        glTranslate(3.08, -0.9, 0.3)
        glScale(1.5, 0.3, 4.0)
        glutSolidCube(0.5)
        glPopMatrix()

    glColor3f(0, 0 ,0)
    glPushMatrix()
    glTranslate(3.08, -0.60, 0)
    glScale(0.2, 0.9, 0.3)
    glutSolidCube(0.5)
    glPopMatrix()

    glColor3f(0, 0 ,0)
    glPushMatrix()
    glTranslate(3.08, -0.74, 0)
    glRotate(90, 1, 0, 0)
    glScale(1, 1, 0.05)
    glutSolidCylinder(0.3, 2, 20, 2)
    glPopMatrix()

    #gabinete
    glColor3f(0, 0, 0)
    glPushMatrix()
    glTranslate(3, -0.25, 1)
    glScale(1, 3, 1)
    glutSolidCube(0.4)
    glPopMatrix()

    #teclado
    glColor3f(0, 0, 0)
    glPushMatrix()
    glTranslate(2.4, -1, 0)
    glScale(1, 0.2, 3)
    glutSolidCube(0.4)
    glPopMatrix()

    #mouse
    glColor3f(0, 0, 0)
    glPushMatrix()
    glTranslate(2.4, -1, -1.1)
    glScale(1, 0.5, 0.8)
    glutSolidSphere(0.1, 40, 40)
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()

def estacaoDeTrabalho(eixoX, eixoY, eixoZ, angulo):
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glRotatef(angulo, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScale(0.8, 0.8, 0.8)
    mesa()
    cadeira()
    computador(False)
    glPopMatrix()

def estacaoDeTrabalhoProf(eixoX, eixoY, eixoZ, angulo):
    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glRotatef(angulo, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScale(0.8, 0.8, 0.8)
    mesaProf(0,-0.15,0)
    cadeiraProfessor(0,-0.2,1,0)
    computador(True)
    glPopMatrix()