#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Filtracja

Created on Fri Mar 17 15:55:45 2017

@author: marek
(c) Marek Kocinski

Przetwarzanie obrazow i grafika komputerowa 2017
Laboratoium 4
"""
import numpy as np
import matplotlib.pyplot as plt


def saltandpepper(im):
    """
    """
    img = im.copy() # zeby nie pracowac na oryginale
    noise = np.random.random_integers(0,255,size=img.shape)
    img[noise==0] = img.min()
    img[noise==255] = img.max()
    return img

def mse(im1,im2):    
    return ((im1-im2)**2).sum()/im1.size

def psnr(im1,im2,maxx=255):
    return 20*np.log10(maxx) - 10*np.log10(mse(im1,im2))