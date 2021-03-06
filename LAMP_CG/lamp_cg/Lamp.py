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

from ArmarioGrande import *
from ArmarioPequeno import *
from EstacaoTrabalho import *
from Janela import *
from QuadroScrum import *
from Ventilador import *
from ArmarioImpressora import *
from Porta import *
from Mesa import *
from Textura import *
from Ambiente import *


#CameraInicio
angleX = 0.0
angleY = -1.65
directionX = 0.0
directionZ = -5.0
directionY = 0.0
xPos = 8.0
zPos = 2.2
yPos = 2.0
#CameraFim


esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 45

#Melhorar cena
global objCompilado
global tempo,quadro,var
tempo = 0
quadro = 0
var = 0


#Animação Ventilador
ventAnimadoCompil=0
global ventLigDesl
global ventAnimado
ventAnimado = 90
ventLigDesl = False


#Animação Ventilador
portaAnimadoCompil=0
global portaLigDesl
global portaAnimado
portaAnimado = 0
portaLigDesl = False

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




def desenho():
    ambiente()
#     Lado direito
    estacaoDeTrabalho(4, 0, -3.5, 0)
    estacaoDeTrabalho(2.7, 0, -3.5, 0)
    estacaoDeTrabalho(1.1, 0, -3.5, 0)
    estacaoDeTrabalho(-0.5, 0, -3.5, 0)
    estacaoDeTrabalho(-2.1, 0, -3.5, 0)
    estacaoDeTrabalho(-3.7, 0, -3.5, 0)
    estacaoDeTrabalho(-6.3, 0, -3.5, 0)
    estacaoDeTrabalho(-7.9, 0, -3.5, 0)
    quadroScrum(3, 2, -3.8,0, True)
    quadroScrum(-2, 2, -3.8,0, False)
    armarioImpressora(-5,0,-3.5)


#     Lado esquerdo
    estacaoDeTrabalho(1.1, 0, 3.5, 180)
    estacaoDeTrabalho(-0.5, 0, 3.5, 180)
    estacaoDeTrabalho(-2.1, 0, 3.5, 180)
    estacaoDeTrabalho(-3.7, 0, 3.5, 180)
    quadroScrum(1, 2, -3.8,180, True)

#     Armários
    armarioGrande(3, 1.05, 3)
    armarioPequeno(4.5, 0.0, -1.5, True, 270)
    armarioPequeno(-5.2, 0.0, -1.5, False, 180)

#     Janelas
    janela(-9.0,2,1.8,90)
    janela(-9.0,2,-1.8,90)

#     Estação de trabalho do professores
    estacaoDeTrabalhoProf(-5.2,0,2.62,-90)
    estacaoDeTrabalhoProf(-5.2,0,0.2,-90)

#     Mesa e cadeiras pretas
    mesa(0,0,0,0)
    cadeiraPreta(-2.5,0,0,-90)
    cadeiraPreta(2.5,0,0,90)

    cadeiraPreta(1.8,0,1.0,15)
    cadeiraPreta(0.7,0,1.4,15)
    cadeiraPreta(-1.8,0,1.0,-15)
    cadeiraPreta(-0.7,0,1.4,-15)

    cadeiraPreta(1.8,0,-1.0,165)
    cadeiraPreta(0.7,0,-1.4,165)
    cadeiraPreta(-1.8,0,-1.0,-165)
    cadeiraPreta(-0.7,0,-1.4,-165)

    quadroBranco(5.2, 2.5, -1.0, 0)
    ponto(5.2, 2.5, 1.5, 0)

def ventiladorAnimacao():
    #todas as animacoes
    global ventAnimado
    global ventAnimadoCompil

    glNewList(ventAnimadoCompil, GL_COMPILE)
    if (ventAnimado == 90):
        ventAnimado = 0
    ventilador(3.0,3.5,0.0, ventAnimado)
    ventilador(-3.0,3.5,0.0, ventAnimado)
    ventAnimado = ventAnimado + 5
    glEndList()

def portaAnimacao(verifica):
    #todas as animacoes
    global portaAnimado
    global portaAnimadoCompil

    glNewList(portaAnimadoCompil, GL_COMPILE)
    if (verifica == False):
        porta(5.35,1.09,3.0,90)
    else:
        porta(4.8,1.09,3.5,150)
    glEndList()


def iluminacao_da_cena1():

    ambiente = [0.2, 0.2, 0.2, 1.0]
    difusa = [0.7, 0.7, 0.7, 1.0]
    especular = [1.0, 1.0, 1.0, 1.0]
    posicao = [0.0, 20.0, 2.0, 0.0]
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

    luzAmbiente=[0.2,0.2,0.2,1.0]
    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    luzDifusa = [0.7,0.7,0.7,1.0] #cor
    luzEspecular = [1.0, 1.0, 1.0, 1.0] #brilho
    posicaoLuz =[20.0, 50.0,50.0, 50.0]
    especMaterial = 60;

    # Especifica que a cor de fundo da janela será branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH)

    #  Define a refletância do material
    glMaterialfv(GL_FRONT,GL_AMBIENT_AND_DIFFUSE, especularidade)
    #  Define a concentração do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    # Define os parâmetros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular)
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz)

    # Habilita o depth-buffering
    glEnable(GL_COLOR_MATERIAL);
    #Habilita o uso de iluminação
    glEnable(GL_LIGHTING);
    #Habilita a luz de número 0
    glEnable(GL_LIGHT0);
    #Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST);



def tela():
    global tempo,quadro,var
    tempo=int(time.clock())
    quadro+=1
    if tempo==var:
        print "fps:",quadro
        quadro=0
        var+=1


    global angulo
    #CameraInicio
    global angleX
    global angleY
    global directionX
    global directionZ
    global directionY
    global xPos
    global zPos
    global yPos
    #CameraFim

    global objCompilado

    #Ventilador animado
    global ventLigDesl
    global ventAnimadoCompil

    #Porta
    global portaLigDesl
    global portaAnimadoCompil

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(0, 0, 0, 0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade

    gluPerspective(angulo,1,0.1,500) # Especifica a projeção perspectiva

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

#     gluLookAt(sin(esqdir) * 10, 0 + cimabaixo, cos(esqdir) * 10, 0, 0, 0, 0, 1,0) # Especifica posição do observador e do alvo
    gluLookAt(xPos, yPos, zPos, xPos+directionX, yPos+directionY, zPos+directionZ, 0, 1, 0); #Para andar
#    iluminacao_da_cena1()
    iluminacao_da_cena2()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d
    glEnable(GL_NORMALIZE)

    glCallList(objCompilado)
    glCallList(ventAnimadoCompil)
    glCallList(portaAnimadoCompil)
    if (ventLigDesl == True):
        ventiladorAnimacao()
    if (portaLigDesl == True):
        portaAnimacao(portaLigDesl)
    else:
        portaAnimacao(portaLigDesl)
#     desenho()
    glutSwapBuffers()
#     glFlush()

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
    global aux1
    global aux2
    global cam
    #CameraInicio
    global angleX
    global angleY
    global directionX
    global directionZ
    global directionY
    global xPos
    global zPos
    global yPos
    fraction = 0.3
    #CameraFim

    #Ventilador animado
    global ventLigDesl
    
    #Ventilador animado
    global portaLigDesl

    if tecla == b'a':  # tecla A
        angleY = angleY - 0.05
        directionX = sin(angleY)
        directionZ = -cos(angleY)

    if tecla == b'd': # tecla D
        angleY = angleY + 0.05
        directionX = sin(angleY);
        directionZ = -cos(angleY);

    if tecla == b'w': # tecla W
        xPos = xPos + (directionX * fraction)
        zPos = zPos + (directionZ * fraction)
        yPos = yPos + (directionY * fraction)


    if tecla == b's': # tecla S
        xPos = xPos - (directionX * fraction)
        zPos = zPos - (directionZ * fraction)
        yPos = yPos - (directionY * fraction)

    if tecla == b'v': # tecla S
        if (ventLigDesl == False):
            ventLigDesl = True
        else:
            ventLigDesl = False
            
    if tecla == b'p': # tecla S
        print portaLigDesl
        if (portaLigDesl == False):
            portaLigDesl = True
        else:
            portaLigDesl = False

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


def init():
    global objCompilado,ventAnimadoCompil, portaAnimadoCompil,  portaLigDesl

    objCompilado = glGenLists(1)

    glNewList(objCompilado, GL_COMPILE)
    desenho()
    glEndList()
    ventAnimadoCompil = glGenLists(2)
    ventiladorAnimacao()
    portaAnimadoCompil = glGenLists(3)
    portaAnimacao(portaLigDesl)

def animar():
    glutPostRedisplay()

global distancia


glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(600,600)
glutCreateWindow(b"LAMP")
distancia = 20
glutDisplayFunc(tela)
glutIdleFunc(animar)
glutMouseFunc(ControleMouse)
glutKeyboardFunc(Teclado)
glutSpecialFunc(TeclasEspeciais)
init()
glutMainLoop()
