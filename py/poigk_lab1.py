#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Funkcje pomocnicze - obrazy RGB

Created on Tue Mar 14 17:42:31 2017

@author: marek
(c) Marek Kocinski

Przetwarzanie obrazow i grafika komputerowa 2017
Laboratoium 2
"""


import numpy as np
import matplotlib.pyplot as plt


def imshow2(imgs,**kw):
    """
    Funkcja wyswietla dwa obrazy.
    imgs - lista z obrazami
    """
    cmap1 = kw.get('cmap','gray')
    show_axis = kw.get('show_axis','on')
    tit = kw.get('titles',['A','B'])
    
    f,ax = plt.subplots(1,2,figsize=(12,8))
    ax[0].imshow(imgs[0],cmap=cmap1)
    ax[1].imshow(imgs[1],cmap=cmap1)
    
    ax[0].set_title(tit[0])
    ax[1].set_title(tit[1])
    
    ax[0].axis(show_axis)
    ax[1].axis(show_axis)
    plt.show()
    
def imshow3(imgs,**kw):
    """
    Funkcja wyswietla trzy obrazy.
    imgs - lista z obrazami
    """
    cmap1 = kw.get('cmap','gray')
    show_axis = kw.get('show_axis','on')
    tit = kw.get('titles',['A','B','C'])
    
    f,ax = plt.subplots(1,3,figsize=(16,8))
    
    ax[0].imshow(imgs[0],cmap=cmap1)
    ax[1].imshow(imgs[1],cmap=cmap1)
    ax[2].imshow(imgs[2],cmap=cmap1)
    
    ax[0].set_title(tit[0])
    ax[1].set_title(tit[1])
    ax[2].set_title(tit[2])
    
    ax[0].axis(show_axis)
    ax[1].axis(show_axis)
    ax[2].axis(show_axis)
    plt.show()
    
def imshow4(imgs,**kw):
    """
    Funkcja wyswietla cztery obrazy.
    imgs - lista z obrazami
    """
    cmap1 = kw.get('cmap','gray')
    show_axis = kw.get('show_axis','on')
    tit = kw.get('titles',['A','B','C','D'])
    interp = kw.get('interpolation', 'None')
    
   
    f,ax = plt.subplots(2,2, sharex=True, sharey=True, figsize=(12,8))
    ax[0,0].imshow(imgs[0],cmap=cmap1,interpolation=interp)
    ax[0,1].imshow(imgs[1],cmap=cmap1,interpolation=interp)
    ax[1,0].imshow(imgs[2],cmap=cmap1,interpolation=interp)
    ax[1,1].imshow(imgs[3],cmap=cmap1,interpolation=interp)
    
    ax[0,0].set_title(tit[0])
    ax[0,1].set_title(tit[1])
    ax[1,0].set_title(tit[2])
    ax[1,1].set_title(tit[3])
    
    ax[0,0].axis(show_axis)
    ax[0,1].axis(show_axis)
    ax[1,0].axis(show_axis)
    ax[1,1].axis(show_axis)

    plt.tight_layout()
    plt.show()
    
    
def imshow4_raw(imgs,**kw):
    """
    Funkcja wyswietla cztery obrazy.
    imgs - lista z obrazami
    """
    cmap0 = kw.get('cmap','gray')
    show_axis = kw.get('show_axis','on')
    tit = kw.get('titles',['A','B','C','D'])
    interp = kw.get('interpolation', 'None')
    
    if not isinstance(cmap0, list):
        cmap1 = [cmap0,cmap0,cmap0,cmap0]
    else:
        cmap1 = cmap0    

    f,ax = plt.subplots(1,4, sharex=True, sharey=True,figsize=(10,8))
    ax[0].imshow(imgs[0],cmap=cmap1[0],interpolation=interp,aspect='auto')
    ax[1].imshow(imgs[1],cmap=cmap1[1],interpolation=interp)
    ax[2].imshow(imgs[2],cmap=cmap1[2],interpolation=interp)
    ax[3].imshow(imgs[3],cmap=cmap1[3],interpolation=interp)
    
    ax[0].set_title(tit[0])
    ax[1].set_title(tit[1])
    ax[2].set_title(tit[2])
    ax[3].set_title(tit[3])
    
    ax[0].axis(show_axis)
    ax[1].axis(show_axis)
    ax[2].axis(show_axis)
    ax[3].axis(show_axis)
    
    plt.show()
    
def imginfo(img,name='obrazek'):
    print 'info o {}: min={:.2f}, aver={:.2f},  max={:.2f}, shape={}, dtype={}'.format(name.upper(), img.min(), img.mean(), img.max(), img.shape, img.dtype)
    
    
def rgb2mono(rgb):
    """
    Funkcja zamienia obraz kolorowy ze skladowymi RGB na obraz monochromatyczny.
    
    W funkcji zastosowano dwie petle for do przegladania wierszow i kolumn obrazu
    """
    wiersze,kolumny,kolory = rgb.shape
    mono = np.zeros((wiersze,kolumny),dtype=rgb.dtype)
    r,g,b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]    
    
    for w in range(wiersze):
        for k in range(kolumny):
            mono[w,k] =  0.2126*r[w,k] + 0.7152*g[w,k] + 0.0722*b[w,k]
    return mono
    
def separateChannels(rgb):
    """
    Funkcja wydziela poszczegolne skladowe kolorow i wyswietla w naturalnyeh przestrzeni barw.
    """  
    
    ro = np.zeros_like(rgb)
    go = np.zeros_like(rgb)
    bo = np.zeros_like(rgb)
    ro[:,:,0] = rgb[:,:,0]
    bo[:,:,1] = rgb[:,:,1]
    go[:,:,2] = rgb[:,:,2]    
    return ro,bo,go