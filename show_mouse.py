import bge
import Rasterizer

co = bge.logic.getCurrentController()
sce = bge.logic.getCurrentScene()
obj = co.owner

if obj["start"] == 0:
    bge.render.setMousePosition(int(bge.render.getWindowWidth() / 2), int(bge.render.getWindowHeight() / 2))
    obj["start"] = 1
    
Rasterizer.showMouse(True)