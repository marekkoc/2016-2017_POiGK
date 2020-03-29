"""
 Lodz University of Technology 
 Institute of Electronics      
 Przetwarzanie obrazow i grafika komputerowa             
 (C) Marek Kocinski 2017                             
"""

import vtk

#setup points and vertices
Points = vtk.vtkPoints()
Points.InsertNextPoint(1.0, 0.0, 0.0)
Points.InsertNextPoint(0.0, 0.0, 0.0)
Points.InsertNextPoint(0.0, 1.0, 0.0)
 
Triangle = vtk.vtkTriangle()
Triangle.GetPointIds().SetId(0, 0)
Triangle.GetPointIds().SetId(1, 1)
Triangle.GetPointIds().SetId(2, 2)

Triangles = vtk.vtkCellArray()
Triangles.InsertNextCell(Triangle)
 
#setup colors
Colors = vtk.vtkUnsignedCharArray()
Colors.SetNumberOfComponents(3)
Colors.SetName("Colors")
Colors.InsertNextTuple3(255,0,0)
Colors.InsertNextTuple3(0,255,0)
Colors.InsertNextTuple3(0,0,255)
 
polydata = vtk.vtkPolyData()
polydata.SetPoints(Points)
polydata.SetPolys(Triangles)
 
polydata.GetPointData().SetScalars(Colors)
polydata.Modified()

# zapis do pliku dyskowego
# plik ten mozemy otworzyc w Paraview
writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName("KolorowyTrojkat.vtp")
writer.SetInputData(polydata) 
writer.Write()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(polydata)
actor = vtk.vtkActor()
actor.SetMapper(mapper)

ren = vtk.vtkRenderer()
ren.AddActor(actor)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

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
del renWin, iren