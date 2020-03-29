"""
 Lodz University of Technology 
 Institute of Electronics      
 Przetwarzanie obrazow i grafika komputerowa             
 (C) Marek Kocinski 2017                             
"""

import vtk

reader = vtk.vtkPNGReader()
reader.SetFileName ("pilki1_gray.png")

iren = vtk.vtkRenderWindowInteractor()

viewer = vtk.vtkImageViewer2()
viewer.SetupInteractor(iren)
viewer.SetInputConnection(reader.GetOutputPort())
viewer.SetColorLevel(125)
viewer.SetColorWindow(255)
viewer.Render()

iren.Start()

def close_window(iren):
    render_window = iren.GetRenderWindow()
    render_window.Finalize()
    iren.TerminateApp()
    
close_window(iren)
del renWin, iren