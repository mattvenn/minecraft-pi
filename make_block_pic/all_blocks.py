import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import os

pic_width = 900
mc = minecraft.Minecraft.create()
# clear area
mc.setBlocks(-20,0,-20,20,2,20,block.AIR.id)

# ground platform
mc.setBlocks(-20,0,-20,20,1,20,block.WOOL.id)

# wait for minecraft to catch up
time.sleep(5)

# wool types
for wool_type in range(16):
    print(wool_type)
    mc.setBlock(0,2,0, block.WOOL.id, wool_type)
    time.sleep(0.2)
    # take photo
    os.system("./raspi2png -w " + str(pic_width) + " -p ./wool-pngs/" + str(wool_type) + ".png")

"""
with open('block_types') as fh:
    block_nums = fh.readlines()

for block_num in block_nums:
    try:
        block_num = int(block_num)
    except ValueError:
        print("skipping line" + block_num)
        continue
    print(block_num)
    mc.setBlock(0,2,0, block_num)
    time.sleep(0.2)
    # take photo
    os.system("./raspi2png -w " + str(pic_width) + " -p ./pngs/" + str(block_num) + ".png")
"""
