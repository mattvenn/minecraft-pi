import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

air = 0
gold = 41

# clear area
mc.setBlocks(-60,0,-60,60,50,60,air)

# go there
mc.player.setPos(5,0,0)

# create a big gold block, 40 units high
mc.setBlocks(-5,0,-5,5,40,5,gold)

