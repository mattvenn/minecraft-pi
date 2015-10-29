import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# clear area
mc.setBlocks(-60,0,-60,60,50,60,block.AIR.id)

# go there
mc.player.setPos(5,0,0)

# create pixels
pixels = [
	[ 15, 13, 1, 14 ],
	[ 1, 3, 1, 14 ],
	[ 1, 13, 11, 14 ],
	[ 1, 13, 1, 15 ],
	]

x = 0
y = 0
z = 0
for row in pixels:
	x = 0
	y = y + 1
	for pixel in row:
		x = x + 1
		mc.setBlock(x, y, z, block.WOOL.id, pixel)
