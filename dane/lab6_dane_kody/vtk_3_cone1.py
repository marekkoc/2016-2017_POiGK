"""
 Lodz University of Technology 
 Institute of Electronics      
 Przetwarzanie obrazow i grafika komputerowa             
 (C) Marek Kocinski 2017                             
"""

import vtk
#from colorsys import rgb_to_hsv
 
# create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
WIDTH=640
HEIGHT=480
renWin.SetSize(WIDTH,HEIGHT)
 
# create cone
cone = vtk.vtkConeSource()
cone.SetResolution(1200)
cone.SetCenter(-2,0,0)
 
# mapper
coneMapper = vtk.vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())
 
# actor
coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)

lSource = vtk.vtkLight() 
lSource.SetLightTypeToCameraLight()
lSource.SetColor(100, 1, 1)

# assign actor to the renderer
ren.AddActor(coneActor)
ren.AddLight(lSource) 

# enable user interface interactor
ren.LightFollowCameraOn()
renWin.Start()

for i in range (360*2):
    renWin.Render()
    ren.GetActiveCamera().Azimuth(0.5)

del renWin