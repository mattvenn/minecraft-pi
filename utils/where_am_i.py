import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

while True:
	playpos = mc.player.getTilePos()
	mc.postToChat(playpos)
	time.sleep(1)
