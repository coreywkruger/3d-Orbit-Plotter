import bge
import mathutils
import math

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    obj = cont.owner
    cam = sce.active_camera
    planet = sce.objects["planet"]
    
    scale_down = 1e-6
    
    list = []
    i = 0
    while i < len(bge.logic.globalDict["coordinates"]):
        dist = (cam.worldPosition - bge.logic.globalDict["coordinates"][i]*scale_down).magnitude
        radius = (planet.worldPosition - bge.logic.globalDict["coordinates"][i]*scale_down).magnitude
        list += [bge.logic.globalDict["coordinates"][i]]

        if radius < planet.worldScale[0]:
            '''print(dist)'''
            print("Hit Atmosphere!!!!")
            break
        else:    
            if dist > 2:
                i += int((dist*0.1)**2) + 1
            else:
                i += 1
            
    j = 0
    future = obj["future"]
    while j < len(list) - 1:
        
        coords = list
        
        vec = (coords[j + 1] - coords[j]).normalized()
        v1 = (coords[j] - planet.worldPosition).normalized()
        v2 = mathutils.Vector((vec[0], vec[1])).normalized()
        m = 0.05
        
        s1 = mathutils.Vector((-m,0,-m))
        s2 = mathutils.Vector((-m,0, m))
        
        s3 = mathutils.Vector((m,0,-m))
        s4 = mathutils.Vector((m,0, m))
                
        yrot = math.asin(v2[1]) - math.pi/2
        xrot = math.asin(vec[2])
        zrot = -math.asin(v1[2])
        
        if v2[0] < 0:
            yrot = -yrot
        '''if vec[1] < 0:
            xrot = xrot'''
        if v1[0] < 0:
            zrot = zrot 

        s1.rotate(obj.localOrientation.Rotation(zrot, 3, [0,1,0])) 
        s1.rotate(obj.localOrientation.Rotation(xrot, 3, [1,0,0])) 
        s1.rotate(obj.localOrientation.Rotation(yrot, 3, [0,0,1]))

        s2.rotate(obj.localOrientation.Rotation(zrot, 3, [0,1,0]))  
        s2.rotate(obj.localOrientation.Rotation(xrot, 3, [1,0,0])) 
        s2.rotate(obj.localOrientation.Rotation(yrot, 3, [0,0,1]))

        s3.rotate(obj.localOrientation.Rotation(zrot, 3, [0,1,0]))  
        s3.rotate(obj.localOrientation.Rotation(xrot, 3, [1,0,0])) 
        s3.rotate(obj.localOrientation.Rotation(yrot, 3, [0,0,1]))

        s4.rotate(obj.localOrientation.Rotation(zrot, 3, [0,1,0]))  
        s4.rotate(obj.localOrientation.Rotation(xrot, 3, [1,0,0]))    
        s4.rotate(obj.localOrientation.Rotation(yrot, 3, [0,0,1]))
        
        '''
        bge.render.drawLine((coords[j])*scale_down + s1, (coords[j])*scale_down + s2, [1,1,0])
        bge.render.drawLine((coords[j])*scale_down + s2, (coords[j])*scale_down + s4, [1,1,0])
        bge.render.drawLine((coords[j])*scale_down + s4, (coords[j])*scale_down + s3, [1,1,0])
        bge.render.drawLine((coords[j])*scale_down + s3, (coords[j])*scale_down + s1, [1,1,0])
        '''
        
        bge.render.drawLine(coords[j]*scale_down, coords[j + 1]*scale_down, [.95,0.4,0])
        
        above = 1.05
        
        if j%10 == 0:
            bge.render.drawLine(((coords[j + 1] - planet.worldPosition)*0.99)*scale_down, (above*planet.worldScale[2]*(coords[j + 1] - planet.worldPosition).normalized())*scale_down, [0.4,0.4,0.4])
        bge.render.drawLine(above*planet.worldScale[2]*(coords[j]*scale_down - planet.worldPosition).normalized(), (above*planet.worldScale[2]*(coords[j + 1]*scale_down - planet.worldPosition).normalized()), [0,1,0])
        j += 1
        
        
main()