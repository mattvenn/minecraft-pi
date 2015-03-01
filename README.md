# Minecraft on the Raspberry Pi

my explorations of the python interface to minecraft on the raspberry pi

If you want to run on another platform, see [Martin O'Hanlon's post about CanaryMod](http://www.stuffaboutcode.com/2014/10/minecraft-raspberryjuice-and-canarymod.html). My notes on installing on [OSX are here](OSX_notes.md)

My notes on useful [CanaryMod commands are here](CanaryMod.md)

# Demos

## Spiral Towers

Creates a random collection of buildings, but using much simpler code than my first attempt (towers.py). Also faster and more fun to watch building.

![spiral towers](spiral_towers.png "spiral towers")

## Towers

Creates a random collection of buildings, code is a bit hard to read. Uses a matrix of values to define the corners of each face of a story. Then towers are made of multiple stories.

![towers](towers.png "towers")

# Required

Some demos require Martin O'Hanlon's library for drawing shapes: http://www.stuffaboutcode.com/2013/11/coding-shapes-in-minecraft.html

# Thanks

* @martinohanlon for inspiration
* raspberry pi crew
* minecraft crew for making a special version available for the pi!

