#/usr/bin/env python
# -*- coding: utf-8 -*


from math import cos
from math import pi
from math import sin
import timeit
#import numpy
import ctypes
import random
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global esqdir
global cimabaixo
global aux1
global aux2


esqdir = 0.0
cimabaixo =3
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 10


def porta(eixoX, eixoY, eixoZ, angulo):
    global aux1
    global aux2

    global cor1

    glPushMatrix()
    glTranslate(eixoX, eixoY, eixoZ)
    glRotatef(angulo, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(2.0,2.0,2.0)

    # OBJETO 1 porta

    glColor3f(1.0 , 0.96, 0.93) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.0, 0.0, 0.0)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(1.0,2.0,0.1)
    glutSolidCube(0.9)  #1cm
    glPopMatrix()

    # OBJETO 2 maçanetas

    glColor3f(0.47 , 0.53, 0.6) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.3, 0.0, 0.0)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.2,0.2,0.1)
    glutSolidSphere(0.5,100,100)  #1cm
    glPopMatrix()


    glColor3f(0.47 , 0.53, 0.6) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.3, 0.0, -0.07)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.04,0.04,1.4)
    glutSolidCylinder(0.5, 0.1, 30, 30)  #1cm
    glPopMatrix()


    glColor3f(0. , 0., 0.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.25, 0.0, 0.07)  #Transtaçao do objeto
    #glRotatef(0, 0.0, 0.0, 0.0)     #Rotaçao do objeto
    glScalef(0.4,0.04,0.4)
    glutSolidCylinder(0.2, 0.1, 30, 30)  #1cm
    glPopMatrix()

    glColor3f(0. , 0., 0.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.25, 0.0, -0.1)  #Transtaçao do objeto
    #glRotatef(0, 0.0, 0.0, 0.0)     #Rotaçao do objeto
    glScalef(0.4,0.04,0.4)
    glutSolidCylinder(0.2, 0.1, 30, 30)  #1cm
    glPopMatrix()

    # OBJETO 3 faixa azul

    glColor3f(0. , 0., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.0, 0.0, 0.046)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(1.0,0.3,0.0)
    glutSolidCube(0.9)  #1cm
    glPopMatrix()

    glColor3f(0. , 0., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.0, 0.0, -0.046)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(1.0,0.3,0.0)
    glutSolidCube(0.9)  #1cm
    glPopMatrix()

    # OBJETO 4 circulos

    glColor3f(0.12 , 0.56, 1.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( -0.2, 0.6, 0.04)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.15,0.15,0.098)
    glutSolidCylinder(0.5, 0.1, 30, 30)
    glPopMatrix()

    glColor3f( 0.0 , 0.66, 0.42) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( -0.04, 0.6, 0.04)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.15,0.15,0.098)
    glutSolidCylinder(0.5, 0.1, 30, 30)
    glPopMatrix()

    glColor3f(1. , 0., 0.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.12, 0.6, 0.04)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.15,0.15,0.098)
    glutSolidCylinder(0.5, 0.1, 30, 30)
    glPopMatrix()

    glColor3f(1.0 , 1.0, 0.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.28, 0.6, 0.04)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.15,0.15,0.098)
    glutSolidCylinder(0.5, 0.1, 30, 30)
    glPopMatrix()

    # OBJETO 5 nome

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( -0.22, 0.6, 0.04)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.025,0.09,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( -0.20, 0.57, 0.04)  #Transtaçao do objeto
    glRotatef(90, 0.0, 0.0,1.0)     #Rotaçao do objeto
    glScalef(0.025,0.07,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( -0.055, 0.6, 0.04)  #Transtaçao do objeto
    glRotatef(20, 0.0, 0.0, -1.0)     #Rotaçao do objeto
    glScalef(0.025,0.09,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( -0.028, 0.6, 0.04)  #Transtaçao do objeto
    glRotatef(20, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glScalef(0.02,0.09,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( -0.040, 0.58, 0.04)  #Transtaçao do objeto
    glRotatef(90, 0.0, 0.0,1.0)     #Rotaçao do objeto
    glScalef(0.02,0.05,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.08, 0.6, 0.04)  #Transtaçao do objeto
    glRotatef(10, 0.0, 0.0, -1.0)     #Rotaçao do objeto
    glScalef(0.025,0.09,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.11, 0.6, 0.04)  #Transtaçao do objeto
    glRotatef(10, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glScalef(0.025,0.09,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.13, 0.6, 0.04)  #Transtaçao do objeto
    glRotatef(10, 0.0, 0.0, -1.0)     #Rotaçao do objeto
    glScalef(0.025,0.09,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.16, 0.6, 0.04)  #Transtaçao do objeto
    glRotatef(10, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glScalef(0.025,0.09,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.28, 0.6, 0.04)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.025,0.09,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glColor3f(1., 1., 1.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.29, 0.62, 0.042)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.06,0.06,0.098)
    glutSolidCylinder(0.5, 0.1, 30, 30)
    glPopMatrix()

    glColor3f(1.0 , 1.0, 0.) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate( 0.26, 0.61, 0.042)  #Transtaçao do objeto
    #glRotatef(30, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glScalef(0.025,0.09,0.03)
    glutSolidCube(0.9)
    glPopMatrix()

    glPopMatrix()


