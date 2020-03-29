# (c) MK
# C: 2016.03.25
# M: 2016.03.25

import os
import numpy as np
import scipy.misc as misc
import matplotlib.pyplot as plt


def seedGrowing(im,seed,upper=150, lower=50):
    """Funkcja do rozrostu obszaru w obrazie
   
    s,r,c - wspolrzedne zarodka (slice,row,column)
    upper - wartosc gorna progu
    lower  - wartosc dolna progu"""
       
    w,k = im.shape
    r,c = seed[0], seed[1]

    if r >= w-1 : r = w-1
    if c >= k-1 : c = k-1

    mask = np.zeros_like(im)
    val = im[r,c]
    seeds = []
    seeds.append((r,c))
    mx = im.max()

    while len(seeds)>0:
        r,c = seeds.pop()
        if r == 0 : r = 1
        if c == 0 : c = 1
        if r == im.shape[0]-1 : r = im.shape[0]-2
        if c == im.shape[1]-1 : c = im.shape[1]-2

        top = (r-1,c)
        bottom = (r+1,c)
        left = (r,c-1)
        right = (r,c+1)
        topleft = (r-1,c-1)
        topright =(r-1,c+1)
        bottomleft=(r+1,c-1)
        bottomright = (r+1,c+1)

        for cell in [top, bottom, left, right, topleft, topright, bottomleft, bottomright]:
            if im[cell] <= val+upper and im[cell] >= val-lower and mask[cell]== 0:
                seeds.append(cell)
                mask[cell]=mx
    return mask

if __name__ == '__main__':
    
    plt.close('all')
    
    

    imgl = misc.ascent()
    rows,cosl = imgl.shape
    
    imgr = np.random.rand(*imgl.shape)
    
    fig = plt.figure()
    fig.subplots_adjust(bottom=0.25)
    
    ax1 = fig.add_subplot(121)
    ax1.axis('off')
    canv1 = ax1.imshow(imgl,cmap='gray', interpolation='None')
    
    ax2 = fig.add_subplot(122)
    ax2.axis('off')
    canv2 = ax2.imshow(imgr,cmap='gray', interpolation='None')
    
    # Mouse click
    def onclick(event):    
        if event.inaxes == ax1.axes:
            seed = (int(event.ydata),int(event.xdata))
            print 'seed val.={}'.format(imgl[event.ydata,event.xdata])
            #global imgr     
            imgr = seedGrowing(imgl,seed,upper=15, lower=15)        
            canv1.set_array(imgl)
            canv2.set_array(imgr)
            fig.canvas.draw()
            
        
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()