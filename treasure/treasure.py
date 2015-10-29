import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from mcpi.vec3 import Vec3
from math import sqrt, pow
import pibrella

mc = minecraft.Minecraft.create()

# pick a random spot
x = random.randint(-60,60)
y = random.randint(0,60)
z = random.randint(-60,60)
destination = Vec3(x, y, z)

while True:
	playpos = mc.player.getTilePos()
	
	diff = playpos - destination
	# work out how far away we are
	# http://math.stackexchange.com/questions/42640/calculate-distance-in-3d-space
	dist = sqrt(pow(diff.x, 2) + pow(diff.y, 2) + pow(diff.z, 2))
	mc.postToChat(dist)
	# flash the light depending on how close we are
	pibrella.light.on()
	time.sleep(dist/10)
	pibrella.light.off()
	time.sleep(dist/10)
