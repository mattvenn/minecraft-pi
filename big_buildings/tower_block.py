import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
air = 0

# clear area
mc.setBlocks(-60,0,-60,60,50,60,air)
time.sleep(5)
story = 0
block_id = 10
# a 10 story building
while story < 10:
    mc.setBlocks(-5, story, -5, 5, story, 5, block_id)
    story = story + 1
    block_id = block_id + 1
