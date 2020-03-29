"""
 Lodz University of Technology 
 Institute of Electronics      
 Przetwarzanie obrazow i grafika komputerowa             
 (C) Marek Kocinski 2017                             
"""

import vtk
print "Wersja VTK: %s"%str(vtk.vtkVersion.GetVTKVersion())
 
# Cel: "narysowac" trojkat w scenie 3D

# Definiiujemy wierzcholki trojkata
points = vtk.vtkPoints()
points.InsertNextPoint(1.0,0.0,0.0)
points.InsertNextPoint(0.0,0.0,0.0)
points.InsertNextPoint(0.0,1.0,0.0)
 
# element graficzny ("prymityw") 
# ktory reprezentuje trojkat (ang. cell)
triangle = vtk.vtkTriangle()
triangle.GetPointIds().SetId(0,0)
triangle.GetPointIds().SetId(1,1)
triangle.GetPointIds().SetId(2,2)
 
# mozemy narysowac wiele trojkatow
triangles = vtk.vtkCellArray()
triangles.InsertNextCell(triangle)
 
# obiekt reprezentujacy wierzcholki 
# oraz elementy graficzne (prymitywy)
# takie jak: punkut, linie, wielokaty
# w tym trojkaty, paski trojkatow,...
trianglePolyData = vtk.vtkPolyData()
trianglePolyData.SetPoints( points )
trianglePolyData.SetPolys( triangles )
 
# klasa - interfejs do mapowania
# danych (vtkPolyData) na podstawowe
# elementy graficzne
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(trianglePolyData)
 
# actor - reprezentuje renderowany obiekt
# wraz z jego geometria i wlasciwosciami
# powierzchni (properties)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
 
# obiekt odpowiedzialny za 
# proces renderowania wszysktkich
# obiektow w scenie
ren = vtk.vtkRenderer()
ren.AddActor(actor)

# Okno na ekranie monitora
# tutaj bedzie odbywal sie proces renderowania
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
 
# create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
 
 
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
close_window(iren)
#del renWin, iren