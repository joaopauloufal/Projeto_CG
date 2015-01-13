# -*- encoding: utf-8 -*

# Autor: João Paulo Ferreira da Silva

'''
 ====== LAMP ===
 Projeto de Computação Gráfica
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
from estacaoTrabalho import *

esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 45

def eixos():
    
    #desenha os eixos x e y do plano cartesiano.
    glColor3f(.9, .1, .1) # cor RGB  eixo X
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .1, .9) # cor RGB  eixo Y
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .9, .1) # cor RGB  eixo z
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    #glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()    
    
    
def piso():   
    glColor3f(.5, .5, .5) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate(0.04, -0.82, 0.0)  #Transtaçao do objeto
    glScale(4.0, 0.2, 4.0)    
    glutSolidCube(0.9) 
    glPopMatrix()
    
# def cadeira(eixoX, eixoY, eixoZ):    
#     
#     #base de sustentação
#     glColor3f(0, 0, 0)
#     glPushMatrix()
#     glRotatef(90, 1, 0, 0)
#     glTranslate(0, 0, 0.1)
#     glutSolidCylinder(0.1, 0.5, 10, 10)
#     glPopMatrix()
#     
#     #assento
#     glColor3f(0, 0, 1)
#     glPushMatrix()
#     glRotatef(90, 1, 0, 0)
#     glutSolidCylinder(0.5, 0.2, 15, 10)
#     glPopMatrix()
#     
#     #barra1
#     glColor3f(0, 0, 0)
#     glPushMatrix()
#     glRotatef(90, 1, 0, 0)
#     glTranslate(-0.1, 0.53, -0.6)
#     glutSolidCylinder(0.05, 0.8, 10, 10)
#     glPopMatrix()
#     
#     #barra2
#     glColor3f(0, 0, 0)
#     glPushMatrix()
#     glRotatef(90, 1, 0, 0)
#     glTranslate(0.1, 0.53, -0.6)
#     glutSolidCylinder(0.05, 0.8, 10, 10)
#     glPopMatrix()
#     
#     #barra3
#     glColor3f(0, 0, 0)
#     glPushMatrix()
#     glRotatef(90, 0, 1, 0)
#     glTranslate(-0.53, 0.62, -0.15)
#     glutSolidCylinder(0.05, 0.3, 10, 10)
#     glPopMatrix()
#     
#     #apoio
#     glColor3f(0, 0, 1)
#     glPushMatrix()
#     glRotatef(90, 0, 0, 0)
#     glTranslate(0, 0.6, 0.3)
#     glutSolidCylinder(0.35, 0.1, 15, 10)
#     glPopMatrix()
#     
#     glColor3f(0, 0, 0)
#     glPushMatrix()
#     glRotatef(90, 0, 0, 0)
#     glTranslate(0, 0.6, 0.4)
#     glutSolidCylinder(0.35, 0.1, 15, 10)
#     glPopMatrix()   
#     
#     #braço1
#     glColor3f(0, 0, 0)
#     glPushMatrix()
#     glRotatef(90, 0, 1, 0)
#     glTranslate(0.0, 0.15, 0.4)
#     glutSolidTorus(.05, 0.3, 40, 40, 40)
#     glPopMatrix()
#     
#     #braço2
#     glColor3f(0, 0, 0)
#     glPushMatrix()
#     glRotatef(90, 0, 1, 0)
#     glTranslate(0.0, 0.15, -0.4)
#     glutSolidTorus(.05, 0.3, 40, 40, 40)
#     glPopMatrix()
#     
#     #pé1
#     glColor3f(0, 0, 0)
#     glPushMatrix()
#     glRotatef(90, 0, 1, 0)
#     glTranslate(0, -0.65, -0.5)
#     glutSolidCylinder(0.08, 1, 10, 10)
#     glPopMatrix()
#     
#     #pé2
#     glColor3f(0, 0, 0)
#     glPushMatrix()
#     glRotatef(90, 0, 0, 0)
#     glTranslate(0, -0.65, -0.5)
#     glutSolidCylinder(0.08, 1, 10, 10)
#     glPopMatrix()         
    
    
def desenho():
    eixos()
    mesa(0,0,0)
    cadeira(0, 0, 1)
    piso()
    
def iluminacao_da_cena1():

    ambiente = [0.2, 0.2, 0.2, 1.0]
    difusa = [0.7, 0.7, 0.7, 1.0]
    especular = [1.0, 1.0, 1.0, 1.0]
    posicao = [0.0, 3.0, 2.0, 0.0]
    lmodelo_ambiente = [0.2, 0.2, 0.2, 1.0]
    
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
     
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, difusa)
    glLightfv(GL_LIGHT0, GL_POSITION, posicao)
    glLightfv(GL_LIGHT0, GL_SPECULAR, especular)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodelo_ambiente)
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    
def iluminacao_da_cena2():

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 90;

    # Especifica que a cor de fundo da janela será branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH)

    #  Define a refletância do material
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    #  Define a concentração do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    

    # Define os parâmetros da luz de número 0
    glEnable(GL_LIGHT0)
    
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    
    
    # Habilita a luz de número 0
    
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)
    
    glEnable(GL_COLOR_MATERIAL)

    # Habilita a definição da cor do material a partir da cor corrente
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    
def tela():
    global angulo

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(0, 0, 0, 0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade
    
    gluPerspective(angulo,1,0.1,500) # Especifica a projeção perspectiva    

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posição do observador e do alvo
    iluminacao_da_cena1()
#    iluminacao_da_cena2()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()
    glFlush()        
    
def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo
    print("*** Tratamento de teclas especiais")
    print ("tecla: ", tecla)
    if tecla == GLUT_KEY_F1:
        print(">>> Tecla F1 pressionada")
    elif tecla == GLUT_KEY_F2:
        print(">>> Tecla F2 pressionada")
    elif tecla == GLUT_KEY_F3:
        print(">>> Tecla F3 pressionada")
    elif tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.05
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.05
    else:
        print ("Apertou... " , tecla)
    tela()
    glutPostRedisplay()
    
def Teclado(tecla, x ,y):
    
            
    tela()
    glutPostRedisplay()
    
    
    
def ControleMouse(button, state, x, y):
    global angulo
    print ("Apertou... " , button)
    if (button == 3):
        if (state == GLUT_DOWN):
            if (angulo >= 10):
                angulo -= 2


    if (button == 4):
        if (state == GLUT_DOWN):
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()
    
    
global distancia


glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow(b"LAMP")
distancia = 20
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc(Teclado)
glutSpecialFunc(TeclasEspeciais)
glutMainLoop()