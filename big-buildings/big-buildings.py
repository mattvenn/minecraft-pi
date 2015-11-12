import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

# clear area
mc.setBlocks(-60,0,-60,60,50,60,block.AIR.id)

# go there
mc.player.setPos(5,0,0)

# create a big block
mc.setBlocks(-5,0,-5,5,10,5,block.GOLD_BLOCK.id)

# make a pyramid on top
width = 5
start_height = 10
height = 0
while width > 0:
	# create base of pyramid
	mc.setBlocks(-width,start_height + height,-width, width,start_height+height,width, block.GOLD_BLOCK.id)
	height = height + 1
	width = width - 1

