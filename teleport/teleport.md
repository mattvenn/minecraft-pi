# Teleport - Pibrella

* This activity will help you understand how to use a Pibrella with Minecraft
* You will need: Minecraft with the Python API
* PiBrella add on board

You will use the PiBrella's button to teleport your player to a random location in Minecraft.

\ ![pibrella](pibrella.jpg)

## Button

To check the PiBrella is working, copy this program and save it as
`teleport.py`.

~~~ { .python }
import pibrella

while True:
	if pibrella.button.read() == 1:
        print("button pressed!")
~~~

If you try and run the program with `F5` as usual, it will fail with the error
message "You must be root to use Pibrella!"

This is because the PiBrella needs super user access to work, which means you
need to run the program with the `sudo` command (a shortening of super user do).

First, open a terminal by double clicking the `LXTerminal` icon on the desktop.
This opens a black window where you can type the following commands:

    sudo python3 teleport.py

When you press the button you should see the message being printed - probably
lots of times. Can you press the button quickly enough to only print one
message? Why do you think more than 1 messages are being printed?

You can slow the loop down by using the `sleep` command. First import the time
library:

    import time

Then inside the loop, add a small delay:

    time.sleep(1)

Run the program again, can you get just one message now?

## Random numbers

For our teleport program to work, you need to pick some random numbers to
teleport to once the button is pressed.

To get a random number, you can use the `random` library.
Try running this program a few times:

~~~ { .python }
import random
x = random.randint(-100, 100)
print(x)
~~~

The `randint(min, max)` function takes 2 parameters that set the range of the random number it returns.

Modify the button test program above so that 3 new random numbers are printed
every time the button is pressed. 

## Teleport

Teleporting in Minecraft is as easy as setting the player position:

~~~ { .python }
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
mc.player.setPos(100, 100, 100)
~~~

Modify your program so that pressing the button teleports you to a random new
location.
