"""
 Lodz University of Technology 
 Institute of Electronics      
 Przetwarzanie obrazow i grafika komputerowa             
 (C) Wojciech Rozycki 2017                             
"""

import vtk
import numpy as np
	
center           = ( 0.0, 0.0, 0.0 )                                          # DETERMINE CENTER OF A FIGURE
radius           = 5.0                                                        # DETERMINE RADIUS OF FIGURE
numberOfPoints   = 60                                                        # DETERMINE RESOLUTION OF FIGURE - IT DESCRIPES "FREQUENCY OF POINTS"
height           = 15.5                                                       # DETERMINE HEIGHT OF FIGURE


math = vtk.vtkMath()
pi   = math.Pi()

####################################################################################
##################### DETERMINES POINTS OF BOTTOM CIRCLE ###########################
####################################################################################

circleCenter = [ 0, 0, 0 ]
points = vtk.vtkPoints()

points.InsertNextPoint( circleCenter )
points.InsertNextPoint( 0, 0, height )

for j in range(0, numberOfPoints):

    alpha = 2.0*pi*float(j)/numberOfPoints           # Convert j degrees into radians
    x = np.cos(alpha)
    y = np.sin(alpha)
    
    circleCenter[0] = center[0] + radius * x;
    circleCenter[1] = center[1] + radius * y;
    
    points.InsertNextPoint( circleCenter )           # INSERTS X, Y, Z COORDINATES OF POINT

####################################################################################
##################### DETERMINES POINTS OF BOTTOM CIRCLE ###########################
####################################################################################

####################################################################################
##################### DETERMINES POINTS OF TOP CIRCLE ##############################
####################################################################################

circleCenter = [ 0,0,height ]

for j in range(0, numberOfPoints):

    alpha = 2.0*pi*float(j)/numberOfPoints           # Convert j degrees into radians
    x = np.cos(alpha)
    y = np.sin(alpha)
    
    circleCenter[0] = center[0] + radius * x;
    circleCenter[1] = center[1] + radius * y;
    
    points.InsertNextPoint( circleCenter )

####################################################################################
##################### DETERMINES POINTS OF TOP CIRCLE ##############################
####################################################################################

triangle = vtk.vtkTriangle()
polygons = vtk.vtkCellArray()

####################################################################################
##################### CONNECTING WALL POINTS #######################################
####################################################################################

# triangle.GetPointIds().SetId(x, y)
# SET y index from points array as x point of triangle

for i in range( 2, numberOfPoints + 2 ):                                         
					
    triangle.GetPointIds().SetId(0, i ); 
    index = i + 1
    if ( index >= numberOfPoints + 2 ): index -= numberOfPoints
    triangle.GetPointIds().SetId(1, index ); 
    triangle.GetPointIds().SetId(2, numberOfPoints + i );
    polygons.InsertNextCell(triangle)
      
    triangle.GetPointIds().SetId(0, numberOfPoints + i );
     
    index = numberOfPoints + i + 1
    if ( index >= 2 * numberOfPoints + 2 ): index -= numberOfPoints
    triangle.GetPointIds().SetId(1, index ); 
    
    index = i + 1
    if ( index >= numberOfPoints + 2 ): index -= numberOfPoints
    triangle.GetPointIds().SetId(2, index ); 
    polygons.InsertNextCell(triangle)

####################################################################################
##################### CONNECTING WALL POINTS #######################################
####################################################################################

####################################################################################
##################### CONNECTING BASE POINTS #######################################
####################################################################################

for i in range( 2, numberOfPoints + 2 ):                                         
    
    triangle.GetPointIds().SetId( 0, 0 ); 
    triangle.GetPointIds().SetId( 1, i );
     
    index = i + 1
    if ( index >= numberOfPoints + 2 ): index -= numberOfPoints
    triangle.GetPointIds().SetId( 2, index ); 
   
    polygons.InsertNextCell(triangle)
      
    triangle.GetPointIds().SetId( 0, 1 );
    triangle.GetPointIds().SetId( 1, numberOfPoints + i );
     
    index = numberOfPoints + i + 1
    if ( index >= 2 * numberOfPoints + 2 ): index -= numberOfPoints
    triangle.GetPointIds().SetId( 2, index ); 

    polygons.InsertNextCell(triangle)

####################################################################################
##################### CONNECTING BASE POINTS #######################################
####################################################################################

# LOADS POINTS AND POLYGONS INTO POLYDATA
polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetPolys(polygons)
   	
renderer = vtk.vtkRenderer()                                        # CREATES OBJECT THAT CONTROLS RENDERING PROCESS

mapper = vtk.vtkPolyDataMapper()                                    # THIS VAR WILL DO THE MAPPING TO THE RENDERING PROCESS

if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput( polydata )
else:
    mapper.SetInputData( polydata )                                 # LOADS DATA INTO MAPPER

actor = vtk.vtkActor()      
actor.SetMapper( mapper )                                           # LOADS DETAILS TO BE DISPLAYED BY ACTOR
actor.GetProperty().SetColor( 1.0, 0.8, 0.7 )                             # SETS COLOR OF FIGURE
    
renWin = vtk.vtkRenderWindow()                                      # CREATES THE WINDOW AND LOADS RENDERER OBJECT - IT IS DESCIBED LATER
renWin.AddRenderer( renderer )

iren = vtk.vtkRenderWindowInteractor()                              # provides a platform-independent interaction mechanism for mouse/key/time events
iren.SetRenderWindow( renWin )
    
renderer.AddActor( actor )                                          # LOADS ACTOR TO THE RENDERER OBJECT
renderer.SetBackground( 1,1,1)                                # SETS COLOR OF BACKGROUND
 
fileType   = "stl"                                                  # CHOOSE TYPE OF FiLE THAT YOU WANT TO SAVE RESULTS TO (stl or vtk)
filename = "cyllinder"                                                 # NAME OF FILE THAT YOU SAVE RESULTS TO
 
if ( fileType == "vtk" ): writer = vtk.vtkPolyDataWriter()          # CREATES OBJECT THAT WILL CREATE OUTPUT FILE
elif ( fileType == "stl" ): writer = vtk.vtkSTLWriter()
else: print "[ERROR] Wrong file format. You can use vtk or stl"
    
if vtk.VTK_MAJOR_VERSION <= 5:
    writer.SetInput( polydata )
else:
    writer.SetInputData( polydata )                               # PROVIDES INPUT DATA
                    
writer.SetFileName( filename+"."+fileType )                       # SETS FILE NAME
writer.Write()                                                    # WRITES OUTPUT FILE

renWin.Render()                                                   # RENDERS WINDOW 
renWin.SetWindowName( "Cylinder example" )                            # SETS WINDOW TITLE
                                                                  # begin mouse interaction
iren.Start()

def close_window( iren ):
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