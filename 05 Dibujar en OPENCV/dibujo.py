import cv2
from cv2 import imshow
import numpy as np

#Parametros Color - Ventana (Resolucion Vertical,Horizontal,1) y el numerador
fondo = 255 * np.ones((600,600,3),dtype=np.uint8)

#Dibujar una linea o cualquier figura.
cv2.line(fondo,(10,10),(590,10),(0,0,255), 2)
cv2.rectangle(fondo,(10,20),(200,100),(0,0,255), 2)

#Circulo sin relleno
cv2.circle(fondo, (100,200),50,(0,255), 2)

#Circulo con  relleno
cv2.circle(fondo, (100,350),80,(0,255), -1)

cv2.putText(fondo,'OPENCV',(10,500), 0, 1, (0,0,0), 2)
cv2.putText(fondo,'OPENCV 2',(10,550), 0, 1, (0,0,0), 2)

cv2.imshow("Dibujos",fondo)
cv2.waitKey(0)