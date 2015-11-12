import os
from PIL import Image
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# clear area
mc.setBlocks(-10,0,-60,80,60,60,block.AIR.id)

# go to a good viewing position
mc.player.setPos(30,0,30)

filename = 'picture.jpg'
print("taking photo...")
os.system("fswebcam  --no-banner -r 800x600 -d /dev/video0 " + filename)

print("processing...")
image = Image.open(filename)
image = image.transpose(Image.FLIP_TOP_BOTTOM)
result = image.convert('P', palette=Image.ADAPTIVE, colors=16)
width, height = result.size

x = 0
y = 0
z = 0
pix_size = 10

print("drawing...")
while y < height:
    while x < width:
        # get value of the pixel at that point
        pixel = result.getpixel((x, y))
        # print(x, y, pixel)

        # create a wool block
        mc.setBlock(x/pix_size, y/pix_size, z, block.WOOL.id, pixel)

        x = x + pix_size

    # next row, so set x to 0 and increase y
    x = 0
    y = y + pix_size
