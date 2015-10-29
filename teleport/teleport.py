import mcpi.minecraft as minecraft
import random
import pibrella

mc = minecraft.Minecraft.create()

while True:
	if pibrella.button.read() == 1:
		mc.postToChat("teleporting!")
		# pick a random spot
		x = random.randint(-60,60)
		y = random.randint(0,60)
		z = random.randint(-60,60)
		mc.setPos(x, y, z)
