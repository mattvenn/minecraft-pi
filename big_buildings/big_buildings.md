# Big buildings

* This activity will help you understand positions in Minecraft,
* How to define volumes in 3D space
* Loops in Python,

It's possible to build amazing things in the Minecraft world, and it can often
be a lot quicker with a few Python tricks!

\ ![shuttle](space-shuttle.jpg)
Image courtesy of [crpeh](https://www.reddit.com/r/Minecraft/comments/14i1lu/we_are_ready_for_liftoff_captain/)

## Bigger blocks

You've already seen how to build single blocks at a time with the `setBlock`
function. 

Placing one block at a time is great, but there is also a way to creat big volumes of blocks by asking Minecraft to fill in all the space in between 2 co-ordinates:

\ ![cuboid](cuboid2.png)

The volume between x1, y1, z1 and x2, y2, z2 will be filled with blocks of type
`block_id`. Here's what the code would look like for the picture above:

    setBlocks(x1, y1, z1, x2, y2, z2, block_id)

Note that `x1`, `y1`, `z1`, `x2`, `y2` and `z2` are just telling you what
parameters are needed and how they work. You'd need to put real numbers in to
make it work.

Let's say you want to build a block 20 blocks wide, centered at the x=0, z=0
point, starting at ground level and going up to y=10. The code would be:

    setBlocks(-10, 0, -10, 10, 10, 10, blocks.GOLD_BLOCK.id)

So when you clear the area with the command above, the volume is
from x = -10 to x = 10, y = 0 to y = 10, and z = -10 to z = 10. Remember in the
Minecraft world, y is vertical.

An easy way to clear a big space ready to start building is to use `setBlocks` to fill a volume with air blocks:

    mc.setBlocks(-60, 0, -60, 60, 60, 60, block.AIR.id)

## Tower blocks

Try using `setBlocks` to build a few big blocks.

\ ![tower](spiral_towers.png)

If you use a loop, you could build a tower block with each story built of a
different kind of block:

# TODO test this and get a picture of it

~~~ { .python }
story = 0
# a 10 story building
while story < 10:
    block_id = story
    mc.setBlocks(-5, story, -5, 5, story, 5, block_id)
    story = story + 1
~~~

## Pyramids

Try building a pyramid by stacking 5 squares on top of each other, with each square a bit smaller than the last:

    mc.setBlocks(-5,0,-5,5,0,5,block.GOLD_BLOCK.id)
    mc.setBlocks(-4,1,-4,4,1,4,block.GOLD_BLOCK.id)
    mc.setBlocks(-3,2,-3,3,2,3,block.GOLD_BLOCK.id)
    ...

Complete the pattern and test your code, does it make a pyramid?

Now you'll use a loop to build a gigantic pyramid without having to do lots of
repetitive typing.

There are 3 patterns in the numbers. Remember the definition of the `setBlocks`
commmand:

    setBlocks(x1, y1, z1, x2, y2, z2, block_id)

* `x1` and `z1` are the same, starting at -5 and increasing by 1 each time,
* `x2` and `z2` are the same, starting at 5 and decreasing by 1 each time,
* `y1` and `y2` are the same, starting at 0 and increasing by 1 each time.

Try running this program - does it create the right numbers?

~~~ { .python }
width = 5
height = 0

while width > 0:
    print(width, -width, height)
    height = height + 1
    width = width - 1
~~~

Can you add an extra line that uses `setBlocks` to create a pyramid?

\ ![pyramid](pyramid.png)
