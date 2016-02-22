import mcpi.minecraft as minecraft
import time
from math import sqrt
import pibrella

mc = minecraft.Minecraft.create()

# hide the treasure
treas_x = 100
treas_y = 5
treas_z = 20

while True:
    x, y, z = mc.player.getTilePos()
    
    dist_x = x - treas_x
    dist_y = y - treas_y
    dist_z = z - treas_z

    # work out how far away we are
    # http://math.stackexchange.com/questions/42640/calculate-distance-in-3d-space
    dist = sqrt(dist_x * dist_x + dist_y * dist_y + dist_z * dist_z)
    mc.postToChat(dist)

    # flash the light depending on how close we are
    pibrella.light.on()
    time.sleep(dist/100)
    pibrella.light.off()
    time.sleep(dist/100)
