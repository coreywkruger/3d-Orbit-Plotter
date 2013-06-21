import bge
import mathutils
from math import *
import GameKeys
import GameLogic

co = bge.logic.getCurrentController()
sce = bge.logic.getCurrentScene()
obj = co.owner
cam = sce.objects["cam"]
cam_anchor1 = sce.objects["cam_anchor1"]
cam_anchor2 = sce.objects["cam_anchor2"]
wheel_down = co.sensors["wheel_down"]
wheel_up = co.sensors["wheel_up"]

sca = cam_anchor1.worldScale

if wheel_up.triggered ==  True:
    cam_anchor1.worldScale = cam_anchor1.worldScale - mathutils.Vector((0.1*sca[0],0.1*sca[1],0.1*sca[2]))
    
if wheel_down.triggered == True:
    cam_anchor1.worldScale = cam_anchor1.worldScale + mathutils.Vector((0.1*sca[0],0.1*sca[0],0.1*sca[0]))