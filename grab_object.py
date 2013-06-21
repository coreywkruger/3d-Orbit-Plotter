import bge
import mathutils
import math

def main():
    co = bge.logic.getCurrentController()
    sce = bge.logic.getCurrentScene()
    obj = co.owner
    
    name = obj.name + "_"
    grab_prev = name + "grab_prev"
    grab_diff = name + "grab_diff"
    cam_dist = name + "cam_dist"
    grab = name + "grab"
    
    mouse = co.sensors["Mouse"]
    over = co.sensors["over"]
    cam = sce.active_camera
 
    x = mouse.position[0]/bge.render.getWindowWidth()
    z = mouse.position[1]/bge.render.getWindowHeight()
    m_vect = -cam.far*cam.getScreenVect(x, z)
    straight = -cam.far*cam.getScreenVect(0.5, 0.5)
    
    if mouse.status == bge.logic.KX_INPUT_JUST_ACTIVATED and over.status == bge.logic.KX_INPUT_ACTIVE:
        bge.logic.globalDict[grab_prev] = mathutils.Vector((obj.worldPosition[0], obj.worldPosition[1], obj.worldPosition[2]))
        cam_distance = mathutils.geometry.intersect_point_line(bge.logic.globalDict[grab_prev], cam.worldPosition, m_vect)
        bge.logic.globalDict[grab_diff] = bge.logic.globalDict[grab_prev] - cam_distance[0]
        bge.logic.globalDict[cam_dist] = bge.logic.globalDict[grab_prev] - cam.worldPosition
        obj[grab] = True
        
    if mouse.status == bge.logic.KX_INPUT_ACTIVE and obj[grab] == True:
        cam_distance = mathutils.geometry.intersect_point_line(bge.logic.globalDict[grab_prev], cam.worldPosition, m_vect)
        new = cam_distance[0] - bge.logic.globalDict[grab_prev]

        theta = (bge.logic.globalDict[grab_prev] - cam.worldPosition).angle(cam_distance[0] - cam.worldPosition)
        phi = (bge.logic.globalDict[grab_prev] - cam.worldPosition).angle(cam_distance[0] - bge.logic.globalDict[grab_prev])
        beta = math.pi/2 - phi
        adjacent = math.sin(beta)*(cam_distance[0] - bge.logic.globalDict[grab_prev]).magnitude
        Hyp = adjacent/math.cos(phi + theta - math.pi/2 + beta) 
        to_ob = bge.logic.globalDict[grab_prev] - cam.worldPosition
        additive = -((to_ob.magnitude + Hyp)/to_ob.magnitude - 1)

        obj.worldPosition = bge.logic.globalDict[grab_prev] + bge.logic.globalDict[grab_diff] + new + (cam_distance[0] - cam.worldPosition)*additive
        
    if mouse.status == bge.logic.KX_SENSOR_JUST_DEACTIVATED or mouse.status == bge.logic.KX_SENSOR_INACTIVE:
        obj[grab] = False
        bge.logic.globalDict[grab_prev] = obj.worldPosition

        
main()