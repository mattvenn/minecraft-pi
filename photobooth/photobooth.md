% KS3
% programming, loops, Python, Minecraft
%

# Photo booth

* KS3
* This activity will help you understand positions in Minecraft and conditional
 statements in Python.
* You will need: Minecraft with the Python API, webcam or picamera.

You will build a photo booth, then create a program that takes a photo when you step inside.

----

## Building the booth

Use Steve's building skills to construct a 3 walled cubicle like the picture below:

![booth](booth.png)

## Positions

You need to include the usual libraries at the start of your program:

~~~ { .python }
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
~~~

Now add the following code to print out Steve's location:

~~~ { .python }
while True:
	playpos = mc.player.getTilePos()
    print(playpos)
~~~

Run the program and walk around. You should see your position in x, y, z
co-ordinates being printed in the Python Shell.

Walk to your booth and make a note of the co-ordinates when you are inside.

## Conditionals

Now you need a `conditional statement` so that something happens only when Steve
is in the exact location you just found:

~~~ { .python }
if playpos.x == -247 and playpos.y == 10 and playpos.z == 60:
    print("say cheese!")
~~~

Put this code into your loop (make sure the code is indented properly) and run
your program again. This time, when you walk into the booth the program should
print out 'say cheese!'.

Now change your program so instead of printing a message it takes a photo of you using an attached web cam or picamera.

## Webcam

If you have a webcam, first install the fswebcam program by opening a terminal and typing:

    sudo apt-get install fswebcam

Then this Python code will take a photo:

~~~ { .python }
filename = 'picture.jpg'
#os.system() runs a linux command called fswebcam which takes a photo
os.system("fswebcam  --no-banner -r 800x600 -d /dev/video0 " + filename)
~~~

## Picamera

The picamera needs to be [installed](https://www.raspberrypi.org/help/camera-module-setup/) along with the [picamera Python library](https://www.raspberrypi.org/documentation/usage/camera/python/README.md).

~~~ { .python }
import picamera
camera = picamera.PiCamera()
camera.capture('image.jpg')
~~~
