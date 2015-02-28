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
textura1 = None
texturaPiso = Image.open("images/piso.jpg", "r")
texturaParedes = Image.open("images/parede_branca.jpg", "r")

objAnimadoCompil=0
#Melhorar cena
global objCompilado
global tempo,quadro,var
tempo = 0
quadro = 0
var = 0


#Animação
global ventLigDesl
global ventAnimado
ventAnimado = 0
ventLigDesl = False

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
    glTranslate(-2.0, 3.975, -1.35)  #Transtaçao do objeto
    glScale(16.4, 0.2, 5.0)
    glutSolidCube(0.9)
    glPopMatrix()
    #glDisable(GL_TEXTURE_2D)


    #parede2
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate(-2.0, -3.975, -1.35)  #Transtaçao do objeto
    glScale(16.4, 0.2, 5.0)
    glutSolidCube(0.9)
    glPopMatrix()

    #parede3
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glTranslate(1.35, 9.28, 0.0)  #Transtaçao do objeto
    glScale(5.0, 0.2, 9.0)
    glutSolidCube(0.9)
    glPopMatrix()

    porta(5.35,1.09,2.5,90)

    #textura parede1
    glPushMatrix()

    carrega_imagem(texturaParedes)
    glEnable(GL_TEXTURE_2D)
    glTranslate(-1.9, 1.44, 3.88)
    glRotate(90, 0, 1, 0)
    glScalef(0, 2.19, 7.28)
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
    glTranslate(-1.9, 1.44, -3.88)
    glRotate(90, 0, 1, 0)
    glScalef(0, 2.19, 7.28)
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
    glTranslate(-9.18, 1.44, 0)
    #glRotate(90, 0, 1, 0)
    glScalef(0, 2.19, 4)
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
    '''
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate(0.04, 3.6, 0.0)  #Transtaçao do objeto
    glScale(12.0, 0.2, 9.05)
    glutSolidCube(0.9)
    glPopMatrix()
    '''




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

#    Ventiladores
#     ventilador(3.0,3.0,0.0, 0)
#     ventilador(-3.0,3.0,0.0, 0)

    #Estação de trabalho do professores
    estacaoDeTrabalhoProf(-5.2,0,2.62,-90)
    estacaoDeTrabalhoProf(-5.2,0,0.2,-90)
    mesa(0,0,0,0)

def ventiladorAnimado():
    #todas as animacoes
    global ventAnimado
    global objAnimadoCompil

    glNewList(objAnimadoCompil, GL_COMPILE)
    if (ventAnimado == 90):
        ventAnimado = 0
    ventilador(3.0,3.0,0.0, ventAnimado)
    ventilador(-3.0,3.0,0.0, ventAnimado)
    ventAnimado = ventAnimado + 5
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
    global objAnimadoCompil


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
    glCallList(objAnimadoCompil)
    if (ventLigDesl == True):
        ventiladorAnimado()
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
    global objCompilado,objAnimadoCompil
    objCompilado = glGenLists(1)

    glNewList(objCompilado, GL_COMPILE)
    desenho()
    glEndList()
    objAnimadoCompil = glGenLists(2)
    ventiladorAnimado()

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
