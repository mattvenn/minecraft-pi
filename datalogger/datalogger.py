import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
import random

# clear area
mc.setBlocks(-60,0,-60,60,50,60,block.AIR.id)

# go there
mc.player.setPos(5,0,0)

x = 0
while True:
	y = random.randint(1, 6)
	x = x + 1
	mc.setBlocks(x, 0, 0, x, y, 0, block.WOOL.id, 3)
	
	time.sleep(1)
