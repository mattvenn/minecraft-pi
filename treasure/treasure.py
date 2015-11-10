import mcpi.minecraft as minecraft
import time
from mcpi.vec3 import Vec3
from math import sqrt
import pibrella

mc = minecraft.Minecraft.create()

# hide the treasure
destination = Vec3(100, 5, 20)

while True:
	playpos = mc.player.getTilePos()
	
	diff = playpos - destination
	# work out how far away we are
	# http://math.stackexchange.com/questions/42640/calculate-distance-in-3d-space
	dist = sqrt(diff.x * diff.x + diff.y * diff.y + diff.z * diff.z)
	mc.postToChat(dist)

	# flash the light depending on how close we are
	pibrella.light.on()
	time.sleep(dist/100)
	pibrella.light.off()
	time.sleep(dist/100)
