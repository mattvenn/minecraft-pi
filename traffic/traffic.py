import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time

# with thanks to Martin O'Hanlon
# http://www.stuffaboutcode.com/2013/11/minecraft-coding-traffic-jam.html

wool = 35
air = 0
iron = 42


# clear area
mc.setBlocks(-60,0,-60,60,50,60,air)

# go there
mc.player.setPos(5,0,0)

# create the traffic light
mc.setBlocks(0,0,0,0,5,0, iron)

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
mc.setBlock(1,red_pos,0,wool, black)
mc.setBlock(1,amb_pos,0,wool, black)
mc.setBlock(1,grn_pos,0,wool, black)

while True:
	# red
	mc.setBlock(1, red_pos, 0, wool, red)
	mc.setBlock(1, amb_pos, 0, wool, black)

	time.sleep(1)

	# red & amber
	mc.setBlock(1, amb_pos, 0, wool, amber)

	time.sleep(1)

	# green
	mc.setBlock(1, red_pos, 0, wool, black)
	mc.setBlock(1, amb_pos, 0, wool, black)
	mc.setBlock(1, grn_pos, 0, wool, green)

	time.sleep(1)

	# amber
	mc.setBlock(1, amb_pos, 0, wool, amber)
	mc.setBlock(1, grn_pos, 0, wool, black)

	time.sleep(1)

	
