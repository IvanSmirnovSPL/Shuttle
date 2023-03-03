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
# uncomment following to set a specific view size
renderView1.ViewSize = [1528, 795] ## change here size of window!!!

# show data in view
rightstlDisplay = Show(rightstl, renderView1)

# trace defaults for the display properties.
rightstlDisplay.Representation = 'Surface'
rightstlDisplay.ColorArrayName = [None, '']
rightstlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
rightstlDisplay.SelectOrientationVectors = 'None'
rightstlDisplay.ScaleFactor = 0.005231130123138428
rightstlDisplay.SelectScaleArray = 'None'
rightstlDisplay.GlyphType = 'Arrow'
rightstlDisplay.GlyphTableIndexArray = 'None'
rightstlDisplay.GaussianRadius = 0.0002615565061569214
rightstlDisplay.SetScaleArray = [None, '']
rightstlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
rightstlDisplay.OpacityArray = [None, '']
rightstlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
rightstlDisplay.DataAxesGrid = 'GridAxesRepresentation'
rightstlDisplay.PolarAxes = 'PolarAxesRepresentation'

# reset view to fit data
renderView1.ResetCamera()

# show data in view
shuttle_editstlDisplay = Show(shuttle_editstl, renderView1)

# trace defaults for the display properties.
shuttle_editstlDisplay.Representation = 'Surface'
shuttle_editstlDisplay.ColorArrayName = [None, '']
shuttle_editstlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
shuttle_editstlDisplay.SelectOrientationVectors = 'None'
shuttle_editstlDisplay.ScaleFactor = 0.04055113792419434
shuttle_editstlDisplay.SelectScaleArray = 'None'
shuttle_editstlDisplay.GlyphType = 'Arrow'
shuttle_editstlDisplay.GlyphTableIndexArray = 'None'
shuttle_editstlDisplay.GaussianRadius = 0.002027556896209717
shuttle_editstlDisplay.SetScaleArray = [None, '']
shuttle_editstlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
shuttle_editstlDisplay.OpacityArray = [None, '']
shuttle_editstlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
shuttle_editstlDisplay.DataAxesGrid = 'GridAxesRepresentation'
shuttle_editstlDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data in view
leftstlDisplay = Show(leftstl, renderView1)

# trace defaults for the display properties.
leftstlDisplay.Representation = 'Surface'
leftstlDisplay.ColorArrayName = [None, '']
leftstlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
leftstlDisplay.SelectOrientationVectors = 'None'
leftstlDisplay.ScaleFactor = 0.005231130123138428
leftstlDisplay.SelectScaleArray = 'None'
leftstlDisplay.GlyphType = 'Arrow'
leftstlDisplay.GlyphTableIndexArray = 'None'
leftstlDisplay.GaussianRadius = 0.0002615565061569214
leftstlDisplay.SetScaleArray = [None, '']
leftstlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
leftstlDisplay.OpacityArray = [None, '']
leftstlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
leftstlDisplay.DataAxesGrid = 'GridAxesRepresentation'
leftstlDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data in view
topstlDisplay = Show(topstl, renderView1)

# trace defaults for the display properties.
topstlDisplay.Representation = 'Surface'
topstlDisplay.ColorArrayName = [None, '']
topstlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
topstlDisplay.SelectOrientationVectors = 'None'
topstlDisplay.ScaleFactor = 0.005964210629463196
topstlDisplay.SelectScaleArray = 'None'
topstlDisplay.GlyphType = 'Arrow'
topstlDisplay.GlyphTableIndexArray = 'None'
topstlDisplay.GaussianRadius = 0.0002982105314731598
topstlDisplay.SetScaleArray = [None, '']
topstlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
topstlDisplay.OpacityArray = [None, '']
topstlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
topstlDisplay.DataAxesGrid = 'GridAxesRepresentation'
topstlDisplay.PolarAxes = 'PolarAxesRepresentation'

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.6027791295647092, -0.5167305140989987, 0.6246441500134292]
renderView1.CameraFocalPoint = [-0.005759477615356451, 4.875591740376526e-18, 0.05757633596658706]
renderView1.CameraViewUp = [0.29389576929683675, 0.5319427579207354, 0.7941424173818589]
renderView1.CameraParallelScale = 0.2516020386401945

#### uncomment the following to render all views
RenderAllViews()
time.sleep(1)
# alternatively, if you want to write images, you can use SaveScreenshot(...).