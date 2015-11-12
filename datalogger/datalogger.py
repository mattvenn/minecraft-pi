import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import pibrella

mc = minecraft.Minecraft.create()
import random

# clear area
mc.setBlocks(-60,0,-60,60,50,60,block.AIR.id)

# go there
mc.player.setPos(5,0,0)

data = 0

def button_pressed(pin):
    global data
    data = data + 1

pibrella.button.pressed(button_pressed)

x = 0
while True:
    print(data)
    x = x + 1
    mc.setBlocks(x, 0, 0, x, data, 0, block.WOOL.id, 3)
    data = 0
	
    time.sleep(1)
