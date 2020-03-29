# -*- coding: utf-8 -*-
# Lab 9 - 2015
# Matplotlib - Graficzny interfejs użytkownika 2- biblioteka Matplotlib
# (c) Marek Kocinski & Anna Borowska-Terka

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

img = plt.imread(os.path.join('lab3_dane','krynica_gray.png'))


fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

im = ax.imshow(img,cmap='gray')
fig.colorbar(im)

slidercolor = 'lightgoldenrodyellow'
slideraxes = fig.add_axes([0.25, 0.1, 0.65, 0.05], axisbg=slidercolor)

slider = Slider(slideraxes, 'Prog.', 0, 255, valinit=img.max()/2, valfmt='%d')

def update(val):
    im.set_array(np.where(img>slider.val,255,0))
    fig.canvas.draw()

slider.on_changed(update)
plt.show()