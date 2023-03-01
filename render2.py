# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import time
from pathlib import Path
import argparse
#### disable automatic camera reset on 'Show'
#paraview.simple._DisableFirstRenderCameraReset()

parser = argparse.ArgumentParser(description="A program for render shuttle.")
parser.add_argument('-p', '--path', metavar='', type=str, default='', required=True, help="A path to file's directory.")
args = parser.parse_args()

path = args.path

path1=str(Path(path, 'top.stl'))
path2=str(Path(path, 'left.stl'))
path3=str(Path(path, 'right.stl'))
path4=str(Path(path, 'shuttle_edit.stl'))

# create a new 'STL Reader'
leftstl = STLReader(registrationName='left.stl', FileNames=[path2])

# create a new 'STL Reader'
rightstl = STLReader(registrationName='right.stl', FileNames=[path3])

# create a new 'STL Reader'
shuttle_editstl = STLReader(registrationName='shuttle_edit.stl', FileNames=[path4])

# create a new 'STL Reader'
topstl = STLReader(registrationName='top.stl', FileNames=[path1])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
leftstlDisplay = Show(leftstl, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
leftstlDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show data in view
rightstlDisplay = Show(rightstl, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
rightstlDisplay.Representation = 'Surface'

# show data in view
shuttle_editstlDisplay = Show(shuttle_editstl, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
shuttle_editstlDisplay.Representation = 'Surface'

# show data in view
topstlDisplay = Show(topstl, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
topstlDisplay.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data bounds
renderView1.ResetCamera(0.14673453569412231, 0.1946321576833725, -0.003738319966942072, 0.003738319966942072, 0.06577153503894806, 0.12541364133358002, False)

# reset view to fit data
renderView1.ResetCamera(False)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2400, 1300)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.7518168037533106, 0.40176619191526913, 0.5340122580930196]
renderView1.CameraFocalPoint = [-0.0057594776153564444, -5.45300320681359e-20, 0.05757633596658707]
renderView1.CameraViewUp = [0.45176060764356724, -0.19379126363688445, 0.8708371257126872]
renderView1.CameraParallelScale = 0.2516020386401945

#--------------------------------------------
# uncomment the following to render all views
RenderAllViews()
time.sleep(5)
# alternatively, if you want to write images, you can use SaveScreenshot(...).
