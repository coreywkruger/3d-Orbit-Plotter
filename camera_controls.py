import bge
import mathutils
from math import *

##### GAME ENGINE STUFF
co = bge.logic.getCurrentController()
sce = bge.logic.getCurrentScene()

##### OBJECTS
obj = co.owner
cam = sce.objects["cam"]
cam_anchor1 = sce.objects["cam_anchor1"]
cam_anchor2 = sce.objects["cam_anchor2"]

##### SENSORS
mouse = co.sensors["Mouse"]
shift = co.sensors["shift"]

##### MOUSE POSITION ON SCREEN
##### The position of the mouse found relative to the center of the screen, and scaled up for higher sensitivity to movement.
x = 5*(0.5 + mouse.position[0]/bge.render.getWindowWidth())
z = 5*(0.5 + mouse.position[1]/bge.render.getWindowHeight())


##### INITIALIZATION
##### Rotations and positions from the last tick are acquired.
if mouse.status == bge.logic.KX_INPUT_JUST_ACTIVATED:
    obj["anchor1"] = "(" + str(x) + "," + str(z) + ")"

if shift.status == bge.logic.KX_INPUT_JUST_ACTIVATED:
   pos1 = cam_anchor1.worldPosition
   cam_anchor1["lastPos"] = "(" + str(pos1[0]) + "," + str(pos1[1]) + "," + str(pos1[2]) + ")"
      
##### ACTIVE  
##### Rotation and position of the camera anchor are calculated here while the mouse is active.
if mouse.status == bge.logic.KX_INPUT_ACTIVE:
    mouse_vector = mathutils.Vector((x - eval(obj["anchor1"])[0], 0, z - eval(obj["anchor1"])[1]))
    factor = mouse_vector.magnitude
    mouse_vector_2d = mouse_vector.normalized()
    perpendicular = mathutils.Vector((mouse_vector_2d[2], 0, -mouse_vector_2d[0]))
    lastMat1 = mathutils.Matrix((eval(cam_anchor1["lastRot"])))
    lastMat2 = mathutils.Matrix((eval(cam_anchor2["lastRot"])))

    if perpendicular.magnitude > 0:
        rotx = cam_anchor2.localOrientation.Rotation(mouse_vector[2], 3, mathutils.Vector((1,0,0)))
        rotz = cam_anchor1.worldOrientation.Rotation(-mouse_vector[0], 3, mathutils.Vector((0,0,1)))
    if perpendicular.magnitude == 0:
        rotz = cam_anchor1.worldOrientation.Rotation(0, 3, mathutils.Vector((0,0,0)))
        rotx = cam_anchor2.localOrientation.Rotation(0, 3, mathutils.Vector((0,0,0)))
    if shift.status == bge.logic.KX_INPUT_ACTIVE:
        movement = mouse_vector
        movement.rotate(cam_anchor2.worldOrientation)
        if mouse_vector.magnitude > 0:
            cam_anchor1.worldPosition = mathutils.Vector((eval(cam_anchor1["lastPos"]))) + mathutils.Vector((movement[0], movement[1], 0.6*movement[2]))*cam_anchor1.worldScale.magnitude*4.5
    else:
        lastMat1.rotate(rotz)   
        lastMat2.rotate(rotx)
        cam_anchor2.localOrientation = (lastMat2)
        cam_anchor1.worldOrientation = (lastMat1)

##### ON RELEASE
##### Current positions and rotations are recorded for the next tick.
if mouse.status == bge.logic.KX_INPUT_JUST_RELEASED:
    matrix_1 = cam_anchor1.worldOrientation
    matrix_2 = cam_anchor2.localOrientation
    position_1 = cam_anchor1.worldPosition
    cam_anchor1["lastRot"] = "(" + "(" + str(matrix_1[0][0]) + "," + str(matrix_1[0][1]) + "," + str(matrix_1[0][2]) + ")" + "," + "(" + str(matrix_1[1][0]) + "," + str(matrix_1[1][1]) + "," + str(matrix_1[1][2]) + ")" + "," + "(" + str(matrix_1[2][0]) + "," + str(matrix_1[2][1]) + "," + str(matrix_1[2][2]) + ")" + ")"
    cam_anchor2["lastRot"] = "(" + "(" + str(matrix_2[0][0]) + "," + str(matrix_2[0][1]) + "," + str(matrix_2[0][2]) + ")" + "," + "(" + str(matrix_2[1][0]) + "," + str(matrix_2[1][1]) + "," + str(matrix_2[1][2]) + ")" + "," + "(" + str(matrix_2[2][0]) + "," + str(matrix_2[2][1]) + "," + str(matrix_2[2][2]) + ")" + ")"
    cam_anchor1["lastPos"] = "(" + str(position_1[0]) + "," + str(position_1[1]) + "," + str(position_1[2]) + ")"