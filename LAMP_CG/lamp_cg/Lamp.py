# -*- encoding: utf-8 -*-
# Autor: João Paulo Ferreira da Silva
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

from ArmarioGrande import *
from ArmarioPequeno import *
from EstacaoTrabalho import *
from Janela import *
from QuadroScrum import *
from Ventilador import *


esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 45
textura1 = None

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
    
def testa_imagem():

    diretorioatual = sys.path[0]
    print(diretorioatual)
    
    img_filename = diretorioatual + "images/parede_branca.jpg"
    print(img_filename)
    im = Image.open(img_filename)
    im.show()
    
def carrega_imagem():
    global textura1

    im = Image.open("images/parede_branca.jpg", "r")
    try:
        ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
    except SystemError:
        ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)
    
    textura1 = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura1)
    
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)  #repetir textura na horiz
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) #repetir textura na vertical
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_R, GL_REPEAT)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL) # somente textura
    #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE) # textura + cor
    
    glTexImage2D(
      GL_TEXTURE_2D, 0, 3, ix, iy, 0,
      GL_RGBA, GL_UNSIGNED_BYTE, image
    )



def ambiente():
    global textura1
    #piso
    
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate(0.04, -0.82, 0.0)  #Transtaçao do objeto
    glScale(12.0, 0.2, 9.0)
    glutSolidCube(0.9)
    glPopMatrix()

    #parede1
    #carrega_imagem()    
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    #glEnable(GL_TEXTURE_2D)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate(0.04, 3.975, -1.35)  #Transtaçao do objeto
    glScale(12.0, 0.2, 5.0)
    glutSolidCube(0.9)
    glPopMatrix()
    #glDisable(GL_TEXTURE_2D)
    

    #parede2
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate(0.04, -3.975, -1.35)  #Transtaçao do objeto
    glScale(12.0, 0.2, 5.0)  
    glutSolidCube(0.9)
    glPopMatrix()
    
    #parede3
    glColor3f(0.98, 0.98, 0.98) # cor RGB  eixo X
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glTranslate(1.35, 5.28, 0.0)  #Transtaçao do objeto
    glScale(5.0, 0.2, 9.0)
    glutSolidCube(0.9)
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
    estacaoDeTrabalho(4, 0, -3.3)
    ambiente()
    
    armarioGrande(3, 1.05, 3)
    #armarioPequeno(2, 0.5, 0)
    #quadroScrum(3, 2, 3)
    #janela(-3,2,3)
    #ventilador(0,0,0)

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
    global angulo

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(0, 0, 0, 0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade

    gluPerspective(angulo,1,0.1,500) # Especifica a projeção perspectiva

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo, cos(esqdir) * 10, 0, 0, 0, 0, 1,0) # Especifica posição do observador e do alvo
    iluminacao_da_cena1()
    #iluminacao_da_cena2()
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
    global aux1
    global aux2   
    global cam

    if tecla == b'a':  # tecla A
        aux1 = aux1 + 0.1
       
    
    if tecla == b'd': # tecla D
        aux1 = aux1 - 0.1
        
        
    if tecla == b'w': # tecla W
        aux2 = aux2 - 0.1
        

    if tecla == b's': # tecla S
        aux2 = aux2 + 0.1
        
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
