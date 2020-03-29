# -*- coding: utf-8 -*-
# Lab 9 - 2015
# Matplotlib - Graficzny interfejs użytkownika 2- biblioteka Matplotlib
# (c) Marek Kocinski & Anna Borowska-Terka

import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

img = nib.load(os.path.join('lab5_dane','normal01.nii.gz')).get_data()

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
fig.subplots_adjust(left=0.2,bottom=0.2)

im = ax.imshow(img[:,:,127],cmap='gray')
fig.colorbar(im)

slidercolor = 'lightgoldenrodyellow'
slideraxes = fig.add_axes([0.25, 0.1, 0.65, 0.05], axisbg=slidercolor)

slider = Slider(slideraxes, 'Prog.', 0, 255, valinit=127, valfmt='%d')

def update(val):
    im.set_array(img[:,:,val])
    #fig.canvas.draw()

slider.on_changed(update)

plt.show()