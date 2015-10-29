import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# with thanks to Martin O'Hanlon
# http://www.stuffaboutcode.com/2013/11/minecraft-coding-traffic-jam.html

mc = minecraft.Minecraft.create()

# clear area
mc.setBlocks(-60,0,-60,60,50,60,block.AIR.id)

# go there
mc.player.setPos(5,0,0)

# create the traffic light
mc.setBlocks(0,0,0,0,5,0, block.IRON_BLOCK.id)

# wool can have an id that will change its colour
black = 15
red = 14
amber = 4
green = 13

# light positions
red_pos = 5
amb_pos = 4
grn_pos = 3

# create 3 lights out of wool
mc.setBlock(1,red_pos,0,block.WOOL.id, black)
mc.setBlock(1,amb_pos,0,block.WOOL.id, black)
mc.setBlock(1,grn_pos,0,block.WOOL.id, black)

while True:
	# red
	mc.setBlock(1, red_pos, 0, block.WOOL.id, red)
	mc.setBlock(1, amb_pos, 0, block.WOOL.id, black)

	time.sleep(1)

	# red & amber
	mc.setBlock(1, amb_pos, 0, block.WOOL.id, amber)

	time.sleep(1)

	# green
	mc.setBlock(1, red_pos, 0, block.WOOL.id, black)
	mc.setBlock(1, amb_pos, 0, block.WOOL.id, black)
	mc.setBlock(1, grn_pos, 0, block.WOOL.id, green)

	time.sleep(1)

	# amber
	mc.setBlock(1, amb_pos, 0, block.WOOL.id, amber)
	mc.setBlock(1, grn_pos, 0, block.WOOL.id, black)

	time.sleep(1)

	
