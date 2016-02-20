import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# clear area
mc.setBlocks(-60,0,-60,60,50,60,block.AIR.id)

# go there
mc.player.setPos(5,0,0)

# create a big gold block, 40 units high
mc.setBlocks(-5,0,-5,5,40,5,block.GOLD_BLOCK.id)

