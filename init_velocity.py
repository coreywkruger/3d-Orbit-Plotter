import bge
import mathutils
import math

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    obj = cont.owner

    xsign = math.copysign(1.0, obj["x_init"]) 
    ysign = math.copysign(1.0, obj["y_init"]) 
    zsign = math.copysign(1.0, obj["z_init"]) 
    
    k = 30
    x_extra = mathutils.Vector((0,0,0))
    y_extra = mathutils.Vector((0,0,0))
    z_extra = mathutils.Vector((0,0,0))
    
    bge.render.drawLine(obj.worldPosition, obj.worldPosition + x_extra + k*mathutils.Vector((obj["x_init"],0,0)), [1,0,0])
    bge.render.drawLine(obj.worldPosition + x_extra + k*mathutils.Vector((obj["x_init"],-0.01,0)), obj.worldPosition + x_extra + k*mathutils.Vector((obj["x_init"],0.01,0)), [1,0,0])
    bge.render.drawLine(obj.worldPosition + x_extra + k*mathutils.Vector((obj["x_init"],-0.01,0)), obj.worldPosition + x_extra + k*mathutils.Vector((obj["x_init"] + xsign*0.01,0,0)), [1,0,0])
    bge.render.drawLine(obj.worldPosition + x_extra + k*mathutils.Vector((obj["x_init"], 0.01,0)), obj.worldPosition + x_extra + k*mathutils.Vector((obj["x_init"] + xsign*0.01,0,0)), [1,0,0])
    
    bge.render.drawLine(obj.worldPosition, obj.worldPosition + y_extra + k*mathutils.Vector((0,obj["y_init"],0)), [0,1,0])
    bge.render.drawLine(obj.worldPosition + y_extra + k*mathutils.Vector((-0.01,obj["y_init"],0)), obj.worldPosition + y_extra + k*mathutils.Vector((0.01,obj["y_init"],0)), [0,1,0])
    bge.render.drawLine(obj.worldPosition + y_extra + k*mathutils.Vector((-0.01,obj["y_init"],0)), obj.worldPosition + y_extra + k*mathutils.Vector((0,obj["y_init"] + ysign*0.01,0)), [0,1,0])
    bge.render.drawLine(obj.worldPosition + y_extra + k*mathutils.Vector(( 0.01,obj["y_init"],0)), obj.worldPosition + y_extra + k*mathutils.Vector((0,obj["y_init"] + ysign*0.01,0)), [0,1,0])
    
    bge.render.drawLine(obj.worldPosition, obj.worldPosition + z_extra + k*mathutils.Vector((0,0,obj["z_init"])), [0,0,1])
    bge.render.drawLine(obj.worldPosition + z_extra + k*mathutils.Vector((-0.01,0,obj["z_init"])), obj.worldPosition + z_extra + k*mathutils.Vector((0.01,0,obj["z_init"])), [0,0,1])
    bge.render.drawLine(obj.worldPosition + z_extra + k*mathutils.Vector((-0.01,0,obj["z_init"])), obj.worldPosition + z_extra + k*mathutils.Vector((0,0,obj["z_init"] + zsign*0.01)), [0,0,1])
    bge.render.drawLine(obj.worldPosition + z_extra + k*mathutils.Vector(( 0.01,0,obj["z_init"])), obj.worldPosition + z_extra + k*mathutils.Vector((0,0,obj["z_init"] + zsign*0.01)), [0,0,1])
    
    
main()