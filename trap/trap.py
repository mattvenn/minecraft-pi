import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

while True:
	x, y, z = mc.player.getTilePos()
	if x == -247 and y == 10 and z ==60:
		#trap!
		mc.postToChat("trapped!")
		mc.setBlock(-247, 10, 59, 45)
		mc.setBlock(-247, 11, 59, 45)
