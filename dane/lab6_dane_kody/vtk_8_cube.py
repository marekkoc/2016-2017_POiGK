"""
 Lodz University of Technology 
 Institute of Electronics      
 Przetwarzanie obrazow i grafika komputerowa             
 (C) Wojciech Rozycki 2017                             
"""

import vtk

# CENTER OF A FIGURE
center       = ( 0.0, 0.0, 0.0 )        
# HEIGHT OF FIGURE            
height       = 2           
 
                                   
####################
## POINTS OF CUBE ##
####################
points = vtk.vtkPoints()

points.InsertNextPoint( center )
points.InsertNextPoint( center[0] + height, center[1], center[2] )
points.InsertNextPoint( center[0] + height, center[1] + height, center[2] )
points.InsertNextPoint( center[0], center[1] + height, center[2] )

points.InsertNextPoint( center[0], center[1], center[2] + height )
points.InsertNextPoint( center[0] + height, center[1], center[2] + height )
points.InsertNextPoint( center[0] + height, center[1] + height, center[2] + height )
points.InsertNextPoint( center[0], center[1] + height, center[2] + height )

####################
## POINTS OF CUBE ##
####################
triangle = vtk.vtkTriangle()
polygons = vtk.vtkCellArray()

#####################################
## CONNECTING POINTS TO EACH OTHER ##
#####################################

# triangle.GetPointIds().SetId(x, y)
# SET y index from points array as x point of triangle

# First wall
triangle.GetPointIds().SetId(0, 0)
triangle.GetPointIds().SetId(1, 1)
triangle.GetPointIds().SetId(2, 2)
polygons.InsertNextCell(triangle)

triangle.GetPointIds().SetId(0, 0)
triangle.GetPointIds().SetId(1, 3)
triangle.GetPointIds().SetId(2, 2);
polygons.InsertNextCell(triangle)
# end of the first wall

# Second wall																						
triangle.GetPointIds().SetId(0, 4)
triangle.GetPointIds().SetId(1, 5)
triangle.GetPointIds().SetId(2, 6)
polygons.InsertNextCell(triangle)

triangle.GetPointIds().SetId(0, 4)
triangle.GetPointIds().SetId(1, 7)
triangle.GetPointIds().SetId(2, 6)
polygons.InsertNextCell(triangle)
# end of  the second wall

# Third wall
triangle.GetPointIds().SetId(0, 3)
triangle.GetPointIds().SetId(1, 0)
triangle.GetPointIds().SetId(2, 4);
polygons.InsertNextCell(triangle)

triangle.GetPointIds().SetId(0, 3)
triangle.GetPointIds().SetId(1, 7)
triangle.GetPointIds().SetId(2, 4)
polygons.InsertNextCell(triangle)
# end of the third wall

# Next 3 walls
for i in range( 3 ):                                         
					
    triangle.GetPointIds().SetId(0, i); 
    triangle.GetPointIds().SetId(1, i + 1); 
    triangle.GetPointIds().SetId(2, i + 5);
    polygons.InsertNextCell(triangle)
		      
    triangle.GetPointIds().SetId(0, i); 
    triangle.GetPointIds().SetId(1, i + 4); 
    triangle.GetPointIds().SetId(2, i + 5);
    polygons.InsertNextCell(triangle)
# end of the next 3 walls


#####################################
## CONNECTING POINTS TO EACH OTHER ##
#####################################

# LOADS POINTS AND POLYGONS INTO POLYDATA
polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetPolys(polygons)
   	
# OBJECT THAT CONTROLS RENDERING PROCESS
renderer = vtk.vtkRenderer()     
                                   
# THIS VAR WILL DO THE MAPPING TO THE RENDERING PROCESS
mapper = vtk.vtkPolyDataMapper()                                    
# LOADS DATA INTO MAPPER
mapper.SetInputData( polydata )   

# LOADS DETAILS TO BE DISPLAYED BY ACTOR
actor = vtk.vtkActor()      
actor.SetMapper( mapper )  
# SETS COLOR OF FIGURE                                         
actor.GetProperty().SetColor( 1.0, 0.8, 0.7 )                             
    
# CREATES THE WINDOW AND LOADS RENDERER OBJECT - IT IS DESCRIBED LATER
renWin = vtk.vtkRenderWindow()                                       
renWin.AddRenderer( renderer )

# provides a platform-independent interaction mechanism for mouse/key/time events
iren = vtk.vtkRenderWindowInteractor()                              
iren.SetRenderWindow( renWin )

# LOADS ACTOR TO THE RENDERER OBJECT
renderer.AddActor( actor )      
# SETS COLOR OF BACKGROUND                                   
renderer.SetBackground( 1,1,1 )                                
 
# CHOOSE TYPE OF FiLE THAT YOU WANT TO SAVE RESULTS TO (stl or vtk)
# NAME OF FILE THAT YOU SAVE RESULTS TO
fileType   = "stl"                                                  
filename = "cube"                                                   
 
# CREATES OBJECT THAT WILL CREATE OUTPUT FILE
if ( fileType == "vtk" ): writer = vtk.vtkPolyDataWriter()          
elif ( fileType == "stl" ): writer = vtk.vtkSTLWriter()
else: print "[ERROR] Wrong file format. You can use vtk or stl"
    
# PROVIDES INPUT DATA
writer.SetInputData( polydata )                               
          
# SETS FILE NAME AND WRITES OUTPUT FILE
writer.SetFileName( filename+"."+fileType )                       
writer.Write()                            

# RENDERS WINDOW                       
renWin.Render()      
# SETS WINDOW TITLE                                              
renWin.SetWindowName( "Cube example" )                            
# begin mouse interaction                                                             
iren.Start()

def close_window( iren ):
    render_window = iren.GetRenderWindow()
    render_window.Finalize()
    iren.TerminateApp()
    
# w razie problemow z dzialaniem programu
# odkomentuj/zakomentuj ponizsze linie
# (jedna lub obydwie)  w zaleznosci
# od systemu operacyjnego
# oraz wersji zainstalowanych bibliotek 
# moga pojawic sie problemy w prawidlowym
# zakonczeniu dzialania programu.     
close_window(iren)
del renWin, iren