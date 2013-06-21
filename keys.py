import bge

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    obj = cont.owner
    
    a = cont.sensors["a"]
    d = cont.sensors["d"]
    w = cont.sensors["w"]
    s = cont.sensors["s"]
    r = cont.sensors["r"]
    f = cont.sensors["f"]
    
    up = cont.sensors["up"]
    down = cont.sensors["down"]
    
    increment = 0.001
    
    if a.status == bge.logic.KX_INPUT_ACTIVE:
        obj["x_init"] -= increment
    if d.status == bge.logic.KX_INPUT_ACTIVE:
        obj["x_init"] += increment
    if w.status == bge.logic.KX_INPUT_ACTIVE:
        obj["y_init"] += increment
    if s.status == bge.logic.KX_INPUT_ACTIVE:
        obj["y_init"] -= increment
    if r.status == bge.logic.KX_INPUT_ACTIVE:
        obj["z_init"] += increment
    if f.status == bge.logic.KX_INPUT_ACTIVE:
        obj["z_init"] -= increment
        
    if up.status == bge.logic.KX_INPUT_ACTIVE:
        obj["future"] += 1
    if down.status == bge.logic.KX_INPUT_ACTIVE:
        obj["future"] -= 1
main()