# Minecraft Intro

* Looking and moving around
* Building and destroying blocks
* Hello world with Python
* Moving the player with Python
* Creating blocks with Python

## Getting started with Minecraft

Double click the `Minecraft Pi Edition` icon on the desktop. 

When Minecraft Pi has loaded, click on Start Game, followed by Create new. 

*Leave the window the size it is, if it's maximised it can cause problems
later.*

Use the mouse to look around, and the following keys:

Key             Action 
-------         ------
W		        Forward
A		        Left
S		        Backward
D		        Right
E		        Inventory
Space		    Jump
Double Space	Fly up / Fall
Shift           Fly down
Esc     		Pause / Game menu
Tab     		Release mouse cursor
------------------------------------

You can select an item from the quick draw panel with the mouse's scroll wheel (or use the numbers on your keyboard), or press E and select something from the inventory.

You can also double tap the space bar to fly into the air. You'll stop flying when you release the space bar, and if you double tap it again you'll fall back to the ground.

With the sword in your hand, you can click on blocks in front of you to remove them (or to dig). With a block in your hand, you can use right click to place that block in front of you, or left click to remove a block.

## Hello World with Python

With Minecraft running, bring the focus away from the game by pressing the Tab
key, which will free your mouse. Open Python 3 by double clicking the `IDLE 3`
desktop icon.

The first program you'll write will print a message on the Minecraft screen.

In the Python Idle window, click `File > New window`. This will open a new
window which you're going to write the program in.

Type the following in, paying attention to capitals and punctuation!

~~~ { .python }
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

mc.postToChat('Hello World!')
~~~

The first line uses the `import` command to load the Minecraft library. 
The second line creates the interface between Python and Minecraft, and the final `postToChat` command is what prints the message.

Save the file as `message.py` by clicking `File > Save`. You can then run
the program by pressing the `F5` key on the keyboard.

## Find your location

For each program you write, we recommend you create a new file by clicking `File
> New window`. Feel free to copy and paste the parts you need from your previous
programs.

This program starts exactly the same way, but then stores your location into 3
variables and later prints them out.

~~~ { .python }
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
# convert the x, y, z co-ordinate numbers into a string
position = str(x) + ", " + str(y) + ", " + str(z)
# print the string in your minecraft window
mc.postToChat(position)
~~~

The x, y, and z variables contain each part of your position coordinates: x and z are the walking directions (forward/back and left/right) and y is up/down.

\ ![xyz](xyz.png)

Try running the program with `F5` and check that the location matches the
numbers printed in the top left of the screen. Then move somewhere else and run
the program again - do the numbers still match?

## Teleport

As well as finding out your current location you can specify a particular
location to teleport to. 
Create a new file and save it as `teleport.py`.

~~~ { .python }
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
mc.player.setPos(x, y+100, z)
~~~

This program will first get your location and store it in the x, y and z
variables. Then it uses `setPos` to transport your player 100 spaces higher up
than you currently are. This means you'll teleport up in the air and if you're
not already flying, will fall down to the ground.

Try teleporting to somewhere else!

## Single blocks

First, start a new Python program and include the usual 2 starting lines.

Then to place a block, use the `setBlock` code:

    mc.setBlock(x, y, z, block_id)

`x`, `y` and `z` set the position of the block, and `block_id` sets the type of
block.

This program should set a block right next to your player:

~~~ { .python }
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
mc.setBlock(x + 1, y, z, 41)
~~~

If you can't see the block, it might be because it's behind you! Try turning
around with the mouse.

Each block has a number and a name. For example, the block you created with the
last program was a gold block. Its number is 41 and the name is `GOLD_BLOCK`.

Sometimes it's clearer to create a block with the name instead of the number. We
can do that by importing the `block` library first:

~~~ { .python }
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
mc.setBlock(x + 1, y, z, block.GOLD_BLOCK.id)
~~~

Here are a list of all the blocks with their ID and name:

\ ![blocks](blocks.jpg)

## Creating blocks as you walk

\ ![trail](mcpi-flowers.png)

Now you know how find your location using `getPos` and create a block using
`setBlock`, let's put it together in a loop, so that wherever you walk you
create a trail of blocks behind you automatically.

~~~ { .python }
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, block.FLOWER_CYAN.id)
~~~

Since we used a `while True` loop this will go on forever. To stop it, hit Ctrl + C in the Python window.

Try a few different types of blocks. Can you work out how to change the code so
the blocks get created above you or below you?
