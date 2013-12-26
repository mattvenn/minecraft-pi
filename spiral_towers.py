"""
author: matt venn
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint

mc = minecraft.Minecraft.create()

#trash everything if you want to start on a flat empty space
mc.setBlocks(-40, 0, -40, 40, 60, 40, block.AIR)

def tower(pos,width,height,win_space_x,win_space_y=3):
    print "building tower at %d,%d, width = %d, height = %d, win space x = %d, win space y = %d" % (pos.x,pos.z,width,height,win_space_x,win_space_y)

    for story in range(height):
        #counter so we know when to make a window
        bricks = 0 
        for wall in range(4):
            for brick in range(width):
                bricks += 1
                block_type = block.STONE_BRICK.id
                
                #if we're up enough stories...
                if story % win_space_y == 0:
                    block_type = block.BRICK_BLOCK
                    #and we've made enough blocks...
                    if bricks % win_space_x == 0:
                        #make a window
                        block_type = block.AIR

                #put the block
                mc.setBlock(pos.x,pos.y,pos.z,block_type)

                #move to next position
                if wall == 0:
                    pos.x += 1
                if wall == 1:
                    pos.z += 1
                if wall == 2:
                    pos.x -=1
                if wall == 3:
                    pos.z -=1

        #go up a story
        pos.y += 1

#start building at 0,0,0
pos=minecraft.Vec3(0,0,0)

#and now make 20 random towers!
for i in range(20):
    x = -20 + randint(-20,20)
    z = 10 + randint(-20,20)
    pos=minecraft.Vec3(x,0,z)
    width = randint(3,10)
    height = randint(1,50)
    win_space_x = randint(4,8)
    win_space_y = randint(2,8)
    tower(pos,width,height,win_space_x,win_space_y)
