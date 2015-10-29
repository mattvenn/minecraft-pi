import mcpi.minecraft as minecraft
import mcpi.block as block
import os

mc = minecraft.Minecraft.create()

def take_photo():
	filename = 'picture.jpg'
	#os.system() runs a linux command called fswebcam which takes a photo
	os.system("fswebcam  --no-banner -r 800x600 -d /dev/video0 " + filename)
	print("taken photo!")

while True:
	playpos = mc.player.getTilePos()
	if playpos.x == -247 and playpos.y == 10 and playpos.z ==60:
		#photo!
		mc.postToChat("smile!")
		time.sleep(2)
		take_photo()
