"""
author: matt venn
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint, choice
import time

mc = minecraft.Minecraft.create()

import ipdb; ipdb.set_trace()
mc.player.setPos(0,10,0)

# ids of some solid type blocks
solid_blocks = [14,15,16,1,17,49,98]

# wipe out everything if you want to start on a flat empty space
mc.setBlocks(-40, 0, -40, 40, 200, 40, block.AIR)


time.sleep(5)

for x in range(50):
    mc.setBlock(x, 1, 0, block.BRICK_BLOCK)
    time.sleep(0.1)



time.sleep(5)


def tower(pos,width,height):
    for y in range(height):
        block_type = choice(solid_blocks)
        for z in range(width):
            for x in range(width):
                #put the block
                mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block_type)
        time.sleep(0.05)


#and now make 20 random towers!
for i in range(20):
    x = -20 + randint(-20,20)
    z = 10 + randint(-20,20)
    pos=minecraft.Vec3(x,0,z)
    width = randint(3,10)
    height = randint(1,50)
    print "building tower at %d,%d, width = %d, height = %d" % (pos.x,pos.z,width,height)
    tower(pos,width,height)
