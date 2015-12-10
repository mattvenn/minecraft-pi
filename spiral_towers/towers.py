"""
author: matt venn
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint

"""
requires @martinohanlon's library from http://www.stuffaboutcode.com/2013/04/minecraft-pi-edition-api-tutorial.html
"""

import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#trash everything if you want to start on a flat empty space
#mc.setBlocks(-40, 0, -40, 40, 60, 40, block.AIR)

#this function draws one story of a house. specify w_w for window width and w_h for window height
def house(pos,w,h,w_w=0,w_h=0.5,roof=False):
	l = w/2
	#walls
	corners = [
		[[-1,-1],[-1,+1]],
		[[-1,+1],[+1,+1]],
		[[+1,+1],[+1,-1]],
		[[+1,-1],[-1,-1]],
		]
	
	block_type = block.STONE_BRICK.id
	for wall in corners:
		shapePoints = []
		v = wall	
		for i in [0,1]:
			shapePoints.append(minecraft.Vec3(pos.x+v[i][0]*l, pos.y, pos.z+v[i][1]*l))
		#second set of 2 co-ordinates is the first 2, reversed and lifted by h
		for i in [1,0]:
			shapePoints.append(minecraft.Vec3(pos.x+v[i][0]*l, pos.y+h, pos.z+v[i][1]*l))
		mcdrawing.drawFace(shapePoints, True, block_type)



	#roof
	if roof:
		shapePoints = []
		corners = [[-1,-1],[-1,1],[1,1],[1,-1]]
		for corner in corners:
			shapePoints.append(minecraft.Vec3(pos.x+corner[0]*l, pos.y+h, pos.z+corner[1]*l))
		mcdrawing.drawFace(shapePoints, True, block_type)


	#should we draw a window?
	if w_h == 0:
		return

	corners = [
		[[-1,-1*w_w],[-1,+1*w_w]],
		[[-1*w_w,+1],[+1*w_w,+1]],
		[[+1,+1*w_w],[+1,-1*w_w]],
		[[+1*w_w,-1],[-1*w_w,-1]],
		]
	block_type = block.AIR.id
	w_off = h*(w_h/2)
	for window in corners:
		shapePoints = []
		v = window	
		for i in [0,1]:
			shapePoints.append(minecraft.Vec3(pos.x+v[i][0]*l, pos.y+w_off, pos.z+v[i][1]*l))
		#second set of 2 co-ordinates is the first 2, reversed and lifted by h
		for i in [1,0]:
			shapePoints.append(minecraft.Vec3(pos.x+v[i][0]*l, pos.y+h-w_off, pos.z+v[i][1]*l))
		mcdrawing.drawFace(shapePoints, True, block_type)


#now wrap the house function in a loop to make towers
def tower(pos,w,h,stories,w_w=0,w_h=0.5):
	for i in range(stories-1):	
		house(pos,w,h,w_w,w_h,False)
		pos.y += h
	#last one has a roof
	house(pos,w,h,w_w,w_h,True)


#and now make 20 random towers!
for i in range(20):
	x = -20 + randint(-20,20)
	z = 10 + randint(-20,20)
	pos=minecraft.Vec3(x,0,z)
	stories = randint(1,10)
	story_height = randint(4,8)
	width = randint(4,8)
	window_width = [0,0.3,0.6][randint(0,2)]
	window_height = [0.5,0.8][randint(0,1)]
	print "drawing tower %d at %d,%d, width = %d, height = %d, stories = %d, w_w = %.1f, w_h = %.1f" % (i,x,z,width,story_height,stories,window_width,window_height)
	tower(pos,width,story_height,stories,window_width,window_height)

