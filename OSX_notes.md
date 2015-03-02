# Running python minecraft programs on OSX

## Minecraft

you'll need a copy of minecraft, so go to [Mojang](https://account.mojang.com/), create an account and buy Minecraft

Download, install (will require Java) and test it.

## CanaryMod

Previously I used craftbukkit but this seems defunct. I followed some (Windows) [instructions from Martin here](http://www.stuffaboutcode.com/2014/10/minecraft-raspberryjuice-and-canarymod.html).

* [Download CanaryMod](http://canarymod.net/releases) that matches your minecraft version
* Create a new folder called minecraft and copy the jar file inside
* Create a new text document called start.sh with these contents:


	#!/bin/bash
	cd "$( dirname "$0" )"
	java -Xmx1024M -jar CanaryMod.jar -o true

Make sure the jar file (CanaryMod.jar) matches the filename you used. 

* Make the file executable: chmod a+x start.sh
* Test it by running on a terminal: ./start.sh

## RaspberryJuice

The rest of Martin's instructions above work for this. You'll then need to create a symlink to the API library:

	ln -s CanaryRaspberryJuice-master/resources/mcpi/api/python/mcpi

And then from your current directory you'll be able to import from python:

	import mcpi.minecraft as minecraft



