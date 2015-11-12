import os
from PIL import Image
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# clear area
mc.setBlocks(-60,0,-60,60,50,60,block.AIR.id)

# go there
mc.player.setPos(5,0,0)

def take_photo():
	filename = 'picture.jpg'
	#os.system() runs a linux command called fswebcam which takes a photo
	os.system("fswebcam  --no-banner -r 800x600 -d /dev/video0 " + filename)
	print("taken photo!")

take_photo()
image = Image.open('picture.jpg')
result = image.convert('P', palette=Image.ADAPTIVE, colors=16)
import ipdb; ipdb.set_trace()
width, height = result.size

x = 0
y = 0
pix_size = 50
while y < height:
    while x < width:
        # get value of the pixel at that point
        pixel = result.getpixel((x, y))
        print(x, y, pixel)

        # create a wool block
		mc.setBlock(x, y, z, block.WOOL.id, pixel)

        x = x + pix_size

    y = y + pix_size

#result.save('reduced.png')
