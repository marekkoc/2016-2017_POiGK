

import os
import numpy as np
from numpy import r_
import nibabel as nib

#from add_path_dropbox import MK_DROPBOX_WORK


def stlAddCubeObjects(C):
   for k in range(C.shape[0]):
       
       V1 = r_[C[k,0]+0.5, C[k,1]-0.5, C[k,2]+0.5]
       V2 = r_[C[k,0]-0.5, C[k,1]-0.5, C[k,2]+0.5]
       V3 = r_[C[k,0]-0.5, C[k,1]+0.5, C[k,2]+0.5]
       V4 = r_[C[k,0]+0.5, C[k,1]+0.5, C[k,2]+0.5]
       V5 = r_[C[k,0]+0.5, C[k,1]-0.5, C[k,2]-0.5]
       V6 = r_[C[k,0]-0.5, C[k,1]-0.5, C[k,2]-0.5]
       V7 = r_[C[k,0]-0.5, C[k,1]+0.5, C[k,2]-0.5]
       V8 = r_[C[k,0]+0.5, C[k,1]+0.5, C[k,2]-0.5]
       vert = np.vstack((V1,V2,V3,V4,V5,V6,V7,V8))

       t0=r_[0,2,1]; t1=r_[0,3,2]; t2=r_[4,5,6]
       t3=r_[4,6,7]; t4=r_[0,4,3]; t5=r_[4,7,3]
       t6=r_[1,5,2]; t7=r_[5,6,2]; t8=r_[0,1,5]
       t9=r_[0,5,4]; t10=r_[3,7,6];t11=r_[3,6,2]
       F = np.vstack((t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11))  	
       	
       if k == 0:
          print "k===0"
          vC = vert
          fC = F
       else: 
           G = F + vC.shape[0]
           vC = np.vstack((vC,vert))
           fC = np.vstack((fC,G))
   return vC,fC
    
def stl_add_triangle(VOX, A, B, C, fid):
    a = B - A
    b = C - A
    n = np.cross(a, b)
    n = n / np.sqrt(sum(n*n));    
    av = A*VOX
    bv = B*VOX
    cv = C* VOX
    print >> fid,'  facet normal %.6f %.6f %.6f'%(n[0],n[1],n[2])
    print >> fid,'   outer loop'    
    print >> fid,'    vertex %.6f %.6f %.6f'%(av[0],av[1],av[2])
    print >> fid,'    vertex %.6f %.6f %.6f'%(bv[0],bv[1],bv[2])
    print >> fid,'    vertex %.6f %.6f %.6f'%(cv[0],cv[1],cv[2])   
    print >> fid,'   endloop'
    print >> fid,'  endfacet'
	   
    
if __name__ == '__main__':
    #fdir = os.path.join(MK_DROPBOX_WORK,'rozrost_drzew','am_materialy','20170202_am_stl_szkieletu')
    #os.chdir(fdir)
    
    VOX = 1
    
    fname2 = 'normal01_th-001_skel'
    #fname = 't2_nowy_lepszy'
    im = nib.load(os.path.join('lab5_dane', fname2+'.nii.gz')).get_data()
    x,y,z = np.where(im)
    C = np.vstack((x,y,z)).T
    
    fsave = os.path.join('lab5_dane', fname2+'.stl')
    if os.path.exists(fsave):
        print "\n**** Nadpisjujemy plik {} ****".format(fsave)
    fid = open(os.path.join('lab5_dane', fname2+'.stl'),'w')
    fid.write('solid Vessel branches: {}\n'.format(fname2))
    
    vc,fc = stlAddCubeObjects(C)
    
    for k in range(fc.shape[0]):        
        stl_add_triangle(VOX, vc[fc[k,0],:], vc[fc[k,1],:], vc[fc[k,2],:], fid);    
    fid.close()
    
    