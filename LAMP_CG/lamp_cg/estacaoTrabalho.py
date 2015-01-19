# -*- encoding: utf-8 -*

'''
Created on 13/01/2015

@author: grupoLAMP
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import ctypes
from math import cos
from math import pi
from math import sin
# from numpy import angle
from sys import argv

def mesa(eixoX, eixoY, eixoZ):
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(eixoX, eixoY, eixoZ)  #Transtaçao do objeto
    
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

    
def cadeira(eixoX, eixoY, eixoZ):    
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(eixoX, eixoY, eixoZ)  #Transtaçao do objeto
    
    #base de sustentação
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(0, 0, 0.1)
    glutSolidCylinder(0.1, 0.5, 10, 10)
    glPopMatrix()
    
    #assento
    glColor3f(0, 0, 1)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glutSolidCylinder(0.5, 0.2, 15, 10)
    glPopMatrix()
    
    #barra1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(-0.1, 0.53, -0.6)
    glutSolidCylinder(0.05, 0.8, 10, 10)
    glPopMatrix()
    
    #barra2
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslate(0.1, 0.53, -0.6)
    glutSolidCylinder(0.05, 0.8, 10, 10)
    glPopMatrix()
    
    #barra3
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(-0.53, 0.62, -0.15)
    glutSolidCylinder(0.05, 0.3, 10, 10)
    glPopMatrix()
    
    #apoio
    glColor3f(0, 0, 1)
    glPushMatrix()
    glRotatef(90, 0, 0, 0)
    glTranslate(0, 0.6, 0.3)
    glutSolidCylinder(0.35, 0.1, 15, 10)
    glPopMatrix()
    
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 0, 0)
    glTranslate(0, 0.6, 0.4)
    glutSolidCylinder(0.35, 0.1, 15, 10)
    glPopMatrix()   
    
    #braço1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(0.0, 0.15, 0.4)
    glutSolidTorus(.05, 0.3, 40, 40, 40)
    glPopMatrix()
    
    #braço2
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(0.0, 0.15, -0.4)
    glutSolidTorus(.05, 0.3, 40, 40, 40)
    glPopMatrix()
    
    #pé1
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslate(0, -0.65, -0.5)
    glutSolidCylinder(0.08, 1, 10, 10)
    glPopMatrix()
    
    #pé2
    glColor3f(0, 0, 0)
    glPushMatrix()
    glRotatef(90, 0, 0, 0)
    glTranslate(0, -0.65, -0.5)
    glutSolidCylinder(0.08, 1, 10, 10)
    glPopMatrix()
    
    glPopMatrix()
    
def computador(eixoX, eixoY, eixoZ):
    
    glPushMatrix()
    glRotate(90, 0, 1, 0)
    glScale(0.65, 0.65, 0.65)
    glTranslate(eixoX, eixoY, eixoZ)
    
    #monitor
    glColor3f(0, 0, 0)
    glPushMatrix()
    glTranslate(3, 0, 0)
    glScale(0.1, 1, 1.2)
    glutSolidCube(1.0)    
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
    