import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

while True:
	playpos = mc.player.getTilePos()
	if playpos.x == -247 and playpos.y == 10 and playpos.z ==60:
		#trap!
		mc.postToChat("trapped!")
		mc.setBlock(-247, 10, 59, 45)
		mc.setBlock(-247, 11, 59, 45)
