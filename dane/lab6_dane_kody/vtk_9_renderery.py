"""
 Lodz University of Technology 
 Institute of Electronics      
 Przetwarzanie obrazow i grafika komputerowa             
 (C) Marek Kocinski 2017                             
"""
import vtk

# create source - CONE
cone = vtk.vtkConeSource ()
cone.SetHeight (6.0)
cone.SetRadius (1.0)
cone.SetResolution(20)
cone.SetAngle(46)

coneMapper = vtk.vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())

coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)

coneActor. GetProperty ().SetColor (1.0, 0.8, 0.7)
coneActor. GetProperty ().SetDiffuse (0.7)
coneActor .GetProperty ().SetSpecular (0.4)
coneActor .GetProperty ().SetSpecularPower (250)

# create source - CUBE
cube = vtk.vtkCubeSource()
cube. SetXLength(5)
cube. SetYLength(3)
cube. SetZLength(2)
cube. SetCenter(0,0,0)

cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper. SetInputConnection( cube.GetOutputPort() )

cubeActor = vtk.vtkActor()
cubeActor. GetProperty().SetColor(0.9, 0.5, 0.3)
cubeActor. SetMapper ( cubeMapper )

# create source - ARROW
arrow = vtk.vtkArrowSource()

#arrow.SetTipLength( 0.4);
#arrow.SetTipRadius( 0.6 );
#arrow.SetTipResolution( 12 );
#arrow.SetShaftRadius( 0.2 );
#arrow.SetShaftResolution( 20 );


arrowMapper = vtk.vtkPolyDataMapper()
arrowMapper.SetInputConnection( arrow.GetOutputPort() )

arrowActor = vtk.vtkActor()
arrowActor.SetMapper( arrowMapper)
arrowActor.GetProperty().SetColor(0.2, 0.3, 0.8)

#create source - TEXT
text = vtk.vtkTextSource()
text.SetText("Hello VTK!")

textMapper = vtk.vtkPolyDataMapper()
textMapper.SetInputConnection( text.GetOutputPort())

textActor = vtk.vtkActor()
textActor.SetMapper( textMapper )
textActor.GetProperty().SetColor( 0.9,0.0,0.0)


#renderer1
ren1 = vtk.vtkRenderer()
ren1.SetBackground (0.1,0.2,0.4)
ren1.SetViewport(0.0,0.0,0.5,0.5)
ren1.AddActor(coneActor)
ren1.ResetCamera ()
ren1.GetActiveCamera ().Elevation (30)


#renderer2
ren2 = vtk.vtkRenderer()
ren2.SetBackground (0.3,0.3,0.6)
ren2.SetViewport(0.5,0.0,1.0,0.5)
ren2.AddActor(cubeActor)
ren2.ResetCamera ()
ren2.GetActiveCamera ().Azimuth(30)


#renderer3
ren3 = vtk.vtkRenderer()
ren3.SetBackground (0.6,0.7,0.9)
ren3.SetViewport(0.0,0.5,0.5,1.0)
ren3.AddActor( arrowActor )
ren3.ResetCamera ()
ren3.GetActiveCamera ().Roll(30)

#renderer4
ren4 = vtk.vtkRenderer()
ren4.SetBackground (0.8,0.9,1.0)
ren4.SetViewport(0.5,0.5,1.0,1.0)
ren4.AddActor(textActor )
ren4.ResetCamera()

# create a rendering window and renderers
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.AddRenderer(ren2)
renWin.AddRenderer(ren3)
renWin.AddRenderer(ren4)
renWin.SetSize(300,300)
 
# create a renderwindowinteractor

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
 
renWin.Render()
 
# enable user interface interactor
iren.Initialize()
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
del renWin, iren