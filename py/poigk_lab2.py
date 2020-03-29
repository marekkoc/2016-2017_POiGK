#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Funkcje pomocnicze - Jasność, kontrast obrazu. Histogram. Konwersja między typami danych

Created on Fri Mar 17 15:55:45 2017

@author: marek
(c) Marek Kocinski

Przetwarzanie obrazow i grafika komputerowa 2017
Laboratoium 2
"""
import numpy as np
import matplotlib.pyplot as plt


def brigh_cont_for_loops(img,name='obrazek'):
    wiersze, kolumny = img.shape
    jasn = 0.0
    for w in range(wiersze):
        for k in range(kolumny):
            jasn += img[w,k]
    jasn = jasn / img.size
    kont = 0.0
    for w in range(wiersze):
        for k in range(kolumny):
            kont += (img[w,k]-jasn)**2
    kont = kont/img.size
    kont = np.sqrt(kont)
    print 'info o {}: brightness={:.3f}, contrast={:.3f}'.format(name.upper(),jasn,kont)

    
def imginfo2(img,name='obrazek'):
    print 'info o {}: min={:.2f}, max={:.2f}, br.={:.3f}, con.={:.3f} shape={}, dtype={}'.format(name.upper(), img.min(), img.max(), img.mean(), img.std(),img.shape, img.dtype)

  
def img_hist(img,**kw):
    """
    Funkcja wyswietla dwa obrazy.
    imgs - lista z obrazami
    """
    cmap1 = kw.get('cmap','gray')
    show_axis = kw.get('show_axis','on')
    tit = kw.get('title','A')
    bins = kw.get('bins',64)
    
    f,ax = plt.subplots(1,2,figsize=(12,8))
    ax[0].imshow(img,cmap=cmap1)
    ax[1].hist(img.ravel(),bins=bins)
    
    ax[0].set_title(tit)
    ax[1].set_title('bins={}'.format(str(bins)))
    
    ax[0].axis(show_axis)
    #ax[1].axis(show_axis)
    plt.show()
    
    
def hist2(imgs,**kw):
    """
    Funkcja wyswietla dwa obrazy.
    imgs - lista z obrazami
    """
    tit = kw.get('titles',['A','B'])
    bins = kw.get('bins',[64,128])
    
    f,ax = plt.subplots(1,2,figsize=(10,8))
    ax[0].hist(imgs[0].ravel(),bins=bins[0])
    ax[1].hist(imgs[1].ravel(),bins=bins[1])
    
    ax[0].set_title('{}, bins={}'.format(tit[0], str(bins[0])))
    ax[1].set_title('{}, bins={}'.format(tit[1], str(bins[1])))
    
    plt.show()
    
def hist3(imgs,**kw):
    """
    Funkcja wyswietla trzy obrazy.
    imgs - lista z obrazami
    """
    tit = kw.get('titles',['A','B','C'])
    bins = kw.get('bins',[64,128,256])
    
    f,ax = plt.subplots(1,3,figsize=(12,8))    
    ax[0].hist(imgs[0].ravel(),bins=bins[0])
    ax[1].hist(imgs[1].ravel(),bins=bins[1])
    ax[2].hist(imgs[2].ravel(),bins=bins[2])
    
    ax[0].set_title('{}, bins={}'.format(tit[0], str(bins[0])))
    ax[1].set_title('{}, bins={}'.format(tit[1], str(bins[1])))
    ax[2].set_title('{}, bins={}'.format(tit[2], str(bins[2])))
    plt.show()
    
def hist4(imgs,**kw):
    """
    Funkcja wyswietla cztery obrazy.
    imgs - lista z obrazami
    """
    tit = kw.get('titles',['A','B','C','D'])
    bins = kw.get('bins',[32,64,128,256])
    share_axes=kw.get('share_axes',False)
       
    if share_axes:
        f,ax = plt.subplots(2,2, sharex=True, sharey=True, figsize=(12,8))
    else:
        f,ax = plt.subplots(2,2,figsize=(12,8))
        print share_axes
    ax[0,0].hist(imgs[0].ravel(),bins=bins[0])
    ax[0,1].hist(imgs[1].ravel(),bins=bins[1])
    ax[1,0].hist(imgs[2].ravel(),bins=bins[2])
    ax[1,1].hist(imgs[3].ravel(),bins=bins[3])
    
    ax[0,0].set_title('{}, bins={}'.format(tit[0], str(bins[0])))
    ax[0,1].set_title('{}, bins={}'.format(tit[1], str(bins[1])))
    ax[1,0].set_title('{}, bins={}'.format(tit[2], str(bins[2])))
    ax[1,1].set_title('{}, bins={}'.format(tit[3], str(bins[3])))
    plt.show()


def rescaleFor(img,outMin=0,outMax=255):
    mx = img.max()
    mn = img.min()
    wiersze, kolumny = img.shape
    for w in range(wiersze):
        for k in range(kolumny):
            img[w,k] = (img[w,k]-mn)*(outMax-outMin)/(mx-mn) + outMin
               
            
               
def rescale(img,outMin=0,outMax=255,dtype='uint8'):
    mx = img.max()
    mn = img.min()    
    img = np.asarray(img,dtype=np.float32)
    out = (img-mn)*(outMax-outMin)/(mx-mn) + outMin
    out = np.asarray(out,dtype=dtype)
    return out

