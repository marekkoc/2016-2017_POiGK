"""
 Lodz University of Technology 
 Institute of Electronics      
 Przetwarzanie obrazow i grafika komputerowa             
 (C) Marek Kocinski 2017                             
"""

import vtk
 
# create a rendering window and renderer
ren = vtk.vtkRenderer()
ren.SetBackground (1.0,1.0,1.0)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
 
# create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
 
# create source
source = vtk.vtkSphereSource()
source.SetCenter(0,0,0)
source.SetRadius(5.0)

 
# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(source.GetOutputPort())
 
# actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

actor.GetProperty ().SetColor (1.0, 0.8, 0.7)
actor.GetProperty ().SetDiffuse (0.7)
actor.GetProperty ().SetSpecular (0.4)
actor.GetProperty ().SetSpecularPower (250)


# assign actor to the renderer
ren.AddActor(actor)
 
# enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()


def close_window(iren):
    render_window = iren.GetRenderWindow()
    render_window.Finalize()
    iren.TerminateApp()
    
# w razie problemow z dzialaniem programu
# odkomentuj/zakomentuj ponizsze linie
# (jedną lub obydwie)  w zaleznosci
# od systemu operacyjnego
# oraz wersji zainstalowanych bibliotek 
# moga pojawic sie problemy w prawidlowym
# zakonczeniu dzialania programu.     
#close_window(iren)
