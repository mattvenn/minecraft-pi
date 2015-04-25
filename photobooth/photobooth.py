import mcpi.minecraft as minecraft
import time
import os

mc = minecraft.Minecraft.create()

def take_photo():
	filename = 'picture.jpg'
	#os.system() runs a linux command called fswebcam which takes a photo
	os.system("fswebcam  --no-banner -r 800x600 -d /dev/video0 " + filename)
	print("taken photo!")

while True:
	playpos = mc.player.getTilePos()
	# print(playpos)
	if playpos.x == -61 and playpos.y == 9 and playpos.z == -14:
		#photo!
		mc.postToChat("smile!")
		time.sleep(2)
		take_photo()
