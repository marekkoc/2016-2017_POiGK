# -*- coding: utf-8 -*-
"""
Funkcje pomocnicze - operacje punktowe na obrazach

Created on Sun Mar 26 20:30:10 2017

@author: marek
(c) Marek Kocinski

Przetwarzanie obrazow i grafika komputerowa 2017
Laboratoium 3
"""

def thresh1(img,th,outMin=0,outMax=255):
    im = img.copy()
    wiersze,kolumny = im.shape
    for w in range(wiersze):
        for k in range(kolumny):
            if im[w,k] >= th:
                im[w,k] = outMax
            else:
                im[w,k] = outMin
    return im
                  

# mteoda 2
def thres2(img,th,outMin=0, outMax=255):
    im = img.copy()
    im[im>=th] = outMax
    im[im<th] = outMin
    return im


## ROZNE SPOSOBY POZYSTKIWANIE INFORMACJI Z MACIERZY
#a = np.array([[10,0,10],[0,10,0]])
#print np.nonzero(a)
#print a[np.nonzero(a)]
#print a==10
#print a[a==10]
#print np.where(a==10)
#print a[np.where(a==10)]