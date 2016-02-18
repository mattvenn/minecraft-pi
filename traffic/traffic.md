# Traffic lights

* KS3
* This activity will help you understand loops using Python.
* You will need: Minecraft with the Python API

You will create traffic lights in Minecraft and animate them with a loop.

![traffic lights](traffic.png)

## Creating blocks

You need to import the Minecraft library and setup the `handle`:

~~~ { .python }
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
~~~

Then clear a space and send Steve there:

~~~ { .python }
# clear area
mc.setBlocks(-60,0,-60,60,50,60,block.AIR.id)

# go there
mc.player.setPos(5,0,0)
~~~

Either use a few `setBlock` commands or a single `setBlocks` command to create a
traffic light.

## Coloured wool blocks

Then create the 3 lights with a wool block set to black:

    mc.setBlock(x, y, z, block.WOOL.id, 15)

In this case, you pass an extra parameter (15) to setBlock which sets the wool
block to be black. Here are all the colours:

\ ![wool colours](wool_types.jpg)

## Loops

To create an animation of the lights changing you'll use an infinite loop.
Here's an example that flashes a block between black and red:

~~~ { .python }
import time
while True:

    # make block red
    mc.setBlock(x, y, z, block.WOOL.id, 14)
    # wait for 1 second
    time.sleep(1)

    # make block black
    mc.setBlock(x, y, z, block.WOOL.id, 15)
    # wait for 1 second
    time.sleep(1)
~~~

Now extend the loop to animate the whole traffic light sequence.
