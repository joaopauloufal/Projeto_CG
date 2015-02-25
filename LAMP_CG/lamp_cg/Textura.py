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



def testa_imagem():

    diretorioatual = sys.path[0]
    print(diretorioatual)

    img_filename = diretorioatual + "images/parede_branca.jpg"
    print(img_filename)
    im = Image.open(img_filename)
    im.show()

def carrega_imagem(im):
    global textura1
    try:
        ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
    except SystemError:
        ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)

    textura1 = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura1)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)  #repetir textura na horiz
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) #repetir textura na vertical
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_R, GL_REPEAT)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL) # somente textura
    #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE) # textura + cor

    glTexImage2D(
      GL_TEXTURE_2D, 0, 3, ix, iy, 0,
      GL_RGBA, GL_UNSIGNED_BYTE, image
    )