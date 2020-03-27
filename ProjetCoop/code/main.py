'''
@Author: your name
@Date: 2020-03-09 10:09:35
@LastEditTime: 2020-03-09 10:10:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /code/main.py
'''
import cv2
import numpy
from math import*
import os

apple = cv2.imread("F:/Programmation/Python/ProjetCoop/code/Polytech.png")
 
apple = cv2.resize(apple, (35,35))
apple = numpy.array(apple)
apple = numpy.resize(apple,(35*35*3, 1))
print(apple.shape)
for element in apple:
    for pixel in element:
        mon_fichier = open("polytech.txt", "a")
        mon_fichier.write(str(pixel)+"_")