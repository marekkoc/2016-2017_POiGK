"""
 Lodz University of Technology 
 Institute of Electronics      
 Przetwarzanie obrazow i grafika komputerowa             
 (C) Marek Kocinski 2017                             
"""

import vtk

reader = vtk.vtkPNGReader()
reader.SetFileName("c1.png")

imgGeometry = vtk.vtkImageDataGeometryFilter()
imgGeometry.SetInputConnection(reader.GetOutputPort())

warp = vtk.vtkWarpScalar()
warp.SetInputConnection(imgGeometry.GetOutputPort())
warp.SetScaleFactor(0.7)

wl = vtk.vtkWindowLevelLookupTable()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(warp.GetOutputPort())
mapper.SetScalarRange(0,2000)
mapper.ImmediateModeRenderingOff()
mapper.SetLookupTable(wl)

imageActor = vtk.vtkImageActor()
imageActor.SetInputData(reader.GetOutput())

warpActor = vtk.vtkActor()
warpActor.SetMapper(mapper)

ren1 = vtk.vtkRenderer()
ren1.SetBackground(0.2,0.2,0.4)
ren1.AddActor(imageActor )
ren1.SetViewport(0.0, 0.0, 0.5, 1.0)

ren2 = vtk.vtkRenderer()
ren2.SetBackground(0.6, 0.7, 0.9)
ren2.SetViewport(0.5, 0.0, 1.0, 1.0)
ren2.AddActor(warpActor)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renWin =vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.AddRenderer(ren2)
renWin.SetInteractor(renderWindowInteractor)
renWin.SetSize(900,450)
renWin.Render()

renderWindowInteractor.Start()

def close_window(iren):
    render_window = iren.GetRenderWindow()
    render_window.Finalize()
    iren.TerminateApp()
    
close_window(renderWindowInteractor)
del renWin, renderWindowInteractor