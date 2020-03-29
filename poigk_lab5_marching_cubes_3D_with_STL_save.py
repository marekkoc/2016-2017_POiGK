# %load poigk_lab5_marching_cubes_3D.py
#####################################
### Lodz University of Technology ###
### Institute of Electronics      ###
### Image Processing and          ###
### Computer Graphics             ###
### Marek Kocinski                ###
### 2014                          ###
#####################################
import os
import nibabel as nib

import vtk
print(vtk.vtkVersion.GetVTKSourceVersion())

print os.getcwd()

imageArray = nib.load(os.path.join('lab5_dane','normal01.nii.gz')).get_data()

# aby moc wyswietlic obraz trzeba go zamienic na format vtk-owy
dataImporter = vtk.vtkImageImport()                               
# obraz jest zamieniany na string zbudowany z charow...
data_string = imageArray.tostring()                               
# ... i wrzucany do dataImportera     
dataImporter.CopyImportVoidPointer(data_string, len(data_string)) 
# informujemy VTK ze dane sa charami...
dataImporter.SetDataScalarTypeToUnsignedChar()                    
# ... ze jasnosci sa kodowane przy pomocy jednej tablicy (nie jak w rgb 3)
dataImporter.SetNumberOfScalarComponents(1)                       
 # podajemy rozmiar danych (cos jak wczytywanie raw)...
dataImporter.SetDataExtent(0,(imageArray.shape[2]-1),0,(imageArray.shape[1]-1), 0,(imageArray.shape[0]-1))
# ...mmusimy to zrobic bo podalismy przeciez stringa a nie tablice
dataImporter.SetWholeExtent(0,(imageArray.shape[2]-1),0,(imageArray.shape[1]-1),0,(imageArray.shape[0]-1)) 

shrinker = vtk.vtkImageShrink3D()
shrinker.SetInputConnection(dataImporter.GetOutputPort())
shrinker.SetShrinkFactors(1,1,1)
shrinker.AveragingOn()

gaussian = vtk.vtkImageGaussianSmooth()
gaussian.SetDimensionality(3)
gaussian.SetStandardDeviations(1.0, 1.0, 1.0)
gaussian.SetRadiusFactor(1.0)
gaussian.SetInputConnection(shrinker.GetOutputPort())

marching = vtk.vtkMarchingCubes()
marching.SetInputConnection(gaussian.GetOutputPort())
marching.SetValue(1,50)
marching.ComputeScalarsOff()
marching.ComputeGradientsOff()
marching.ComputeNormalsOff()

decimator = vtk.vtkDecimatePro()
decimator.SetInputConnection(marching.GetOutputPort())
decimator.SetTargetReduction(0.1)
decimator.SetFeatureAngle(60)

smoother = vtk.vtkSmoothPolyDataFilter()
smoother.SetInputConnection(decimator.GetOutputPort())
smoother.BoundarySmoothingOn()
smoother.FeatureEdgeSmoothingOn()

normals = vtk.vtkPolyDataNormals()
normals.SetInputConnection(smoother.GetOutputPort())
normals.SetFeatureAngle(60)

stripper = vtk.vtkStripper()
stripper.SetInputConnection(normals.GetOutputPort())

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(stripper.GetOutputPort())
mapper.ScalarVisibilityOff()

surf = vtk.vtkProperty()
surf.SetColor(0.8,0.1,0.1)

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetProperty(surf)

ren1 = vtk.vtkRenderer()
ren1.AddActor(actor)

fileType   = "stl"                                                  
filename = "systemKrwionosny"                       
 
if ( fileType == "vtk" ): writer = vtk.vtkPolyDataWriter()  
elif ( fileType == "stl" ): writer = vtk.vtkSTLWriter()
else: print "[ERROR] Wrong file format. You can use vtk or stl"
    
if vtk.VTK_MAJOR_VERSION <= 5:
    writer.SetInputConnection( normals.GetOutput() ) 
else:
    writer.SetInputConnection( normals.GetOutputPort() )                             
                    
writer.SetFileName( filename+"."+fileType ) 
writer.Write()       

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

renWin.Render()
iren.Start()

def close_window(iren):
    render_window = iren.GetRenderWindow()
    render_window.Finalize()
    iren.TerminateApp()
# w razie problemow z dzialaniem programu
# odkomentuj/zakomentuj ponizsze linie
# w zaleznosci od systemu operacyjnego
# lub wersji zainstalowanych bibliotek 
# moga pojawic sie problemu w prawidlowym
# zakonczeniu dzialania programu    
#close_window(iren)
#del renWin, iren