import bge
import mathutils
import math

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    obj = cont.owner
    
    scaling = 1e6
    
    prev = scaling*mathutils.Vector((obj["x_init"], obj["y_init"], obj["z_init"]))
    bge.logic.globalDict["time"] = obj["time"]
    planet = sce.objects["planet"]
    future = obj["future"]
    bge.logic.globalDict["coordinates"] = []
    bge.logic.globalDict["current"] = []
    bge.logic.globalDict["coordinates"] = [obj.worldPosition.copy()*scaling]
    i = 0
    

    while i <= future:
        bge.logic.globalDict["time"] = i
        M = planet["ob_mass"]*(1e24)
        m = obj["ob_mass"]
        g = (obj["g"]*(1e-11))*1e3

        
        if i == 0:
            r = (obj.worldPosition.copy() - planet.worldPosition.copy())*scaling
            force = -(M*m*g)/((r.magnitude)**2)    

            gravity = (force)*(r.normalized()) + prev
            bge.logic.globalDict["prev_force"] = gravity
            bge.logic.globalDict["coordinates"] += [mathutils.Vector((obj.worldPosition.copy()*scaling + gravity))]
            bge.logic.globalDict["current"] = mathutils.Vector((obj.worldPosition.copy()*scaling + gravity))
        
        else:
            r = (bge.logic.globalDict["coordinates"][i] - planet.worldPosition.copy()*scaling)
            force = -(M*m*g)/((r.magnitude)**2)    
            
            gravity = (force)*(r.normalized()) + bge.logic.globalDict["prev_force"]
            bge.logic.globalDict["prev_force"] = gravity
            
            bge.logic.globalDict["coordinates"] += [mathutils.Vector((bge.logic.globalDict["current"] + gravity))]
            bge.logic.globalDict["current"] = mathutils.Vector((bge.logic.globalDict["current"] + gravity))

        i += 1

    

    
main()