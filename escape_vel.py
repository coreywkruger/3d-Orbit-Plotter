import bge
import mathutils
import math

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    obj = cont.owner
    planet = sce.objects["planet"]
    
    vel = mathutils.Vector((obj["x_init"], obj["y_init"], obj["z_init"]))
    
    g = obj["g"]*(1e-11)
    M = planet["ob_mass"]*(1e24)
    m = obj["ob_mass"]
    
    scaling = 1e6
    r = obj.worldPosition - planet.worldPosition
    escape = math.sqrt(2*(g*M)/(r.magnitude*scaling)) 
    
    force = -(M*m*g)/((r.magnitude*scaling)**2)    
    gravity = force*(r.normalized()) + vel*(1e3)

    if gravity.magnitude > escape:
        print("Orbit lost, planet's gravity was overcome.")

    
main()