#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 Angio 3D - Finding bifurcation points on 3D raster images.
 
 Based on geometry description of synthesizes vascular trees from VES files 
 there an attempt to overlap all bifuractions and outlets on 3D raster image 
 with depicted vascular tree.
 
 (c) MKocinski & AMaterka

Created: 2017.03.10
Modified: 2017.03.10
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import time

def copyniftiheader(data,niftioriginal):
    """
    Tworzy obraz nifti z przepisaniem informacji naglowkowych z obrazu oryginalnego.

    (C) MKocinski & AMaterka
    U:14.02.2014
    M:15.02.2014
    """
    hdr = niftioriginal.get_header()
    hdr['descrip'] = 'angio3d-nibabel-' + nib.__version__ + 'by MK ({})'.format(time.strftime("%Y-%m-%d"))

    img = nib.Nifti1Image(data, affine=niftioriginal.get_affine(), header=hdr)
    img.set_data_dtype(data.dtype.name)
    return img





if __name__ == '__main__':

    # segmentacja
    if 0:
        hdr = nib.load('normal01_4000_036_3_256.nii.gz')
        data = hdr.get_data()
        data2 = np.where(data>1,255,0)
        data2 = np.asarray(data2,np.uint8)
        hdr2 = copyniftiheader(data2,hdr)
        hdr2.to_filename('normal01_4000_036_3_256_segm.nii.gz')
    
    # iloczyn obrazu szkieletu i po segmentacji
    if 1:
        hdr = nib.load('normal01_4000_036_3_256_surf.nii.gz')
        surf = hdr.get_data()
        skel = nib.load("normal01_4000_036_3_256_skel.nii.gz").get_data()
        
        surf /= surf.max()
        skel /= skel.max()
        
        wyn = surf * skel 
        hdr2 = copyniftiheader(wyn,hdr)
        hdr2.to_filename('skel_part.nii.gz')
        
    
    pass