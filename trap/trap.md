# Trap!

* This activity will help you understand positions in Minecraft
* conditional statements in Python

You will build a trap, then create a program that builds a wall the instant you
step inside.

## Building a trap

This time, you'll build a 3 walled cubicle by hand.

* Use the mouse to look around. Left click destroys a block, right click places a block.
* Use number keys or mouse scroll wheel to choose what block to place. 
* Use the inventory (press the E key) to select different block types.

![trap](trap.png)

## Positions

You'll need the usual lines at the start of your program:

~~~ { .python }
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
~~~

Now add the following code to print out your location:

~~~ { .python }
while True:
	playpos = mc.player.getTilePos()
    print(playpos)
~~~

Run the program and walk around. You should see your position in x, y, z
co-ordinates being printed in the Python Shell.

Walk to your trap and make a note of the co-ordinates when you are inside.

## Conditionals

Now you need a `conditional statement` so that something happens only when
you're in the exact location you just found. Don't use my numbers below, use the
numbers you found when you ran your program.

~~~ { .python }
if playpos.x == -247 and playpos.y == 10 and playpos.z == 60:
    print("trapped!")
~~~

Put this code into your loop (make sure the code is indented properly) and run
your program again. This time, when you walk into the trap the program should
print out 'trapped!'.

Now change your program so instead of printing a message it builds a wall behind
you after you've walked in - preventing you from walking out.
