import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# clear area
mc.setBlocks(-60,0,-60,60,50,60,block.AIR.id)

# go there
mc.player.setPos(25,0,0)

# make a pyramid by stacking smaller squares on top of each other
width = 20  # width starts at 20, decreases to 0
height = 0  # height starts at 0, increases to 20

while width > 0:
	mc.setBlocks(-width,height,-width,width,height,width, block.GOLD_BLOCK.id)
	height = height + 1
	width = width - 1
