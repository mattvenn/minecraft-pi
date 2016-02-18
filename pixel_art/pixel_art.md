# Pixel Art

* This activity will help you understand data structures and lists in Python
* You will need: Minecraft with the Python API

You will draw a simple pattern on graph paper, and then write a program to
reproduce this in Minecraft.

\ ![pixels](pixels.png)

## Draw your art

Get some graph paper or draw a grid on some plain paper. Use different colours
in each block to build a simple image. Keep your image smaller than 8 x 8
blocks.

Then make a copy of your image, but convert the colours to numbers using this
table:

\ ![wool colours](wool_types.jpg)

## Lists

Now convert your picture into a Python data structure - each row is going to
become a list, and all the lists that represent rows will be put into another
list that represents the whole picture.

This is the data structure used to create the picture above:

    pixels = [
        [ 15, 13, 1, 14 ],
        [ 1, 3, 1, 14 ],
        [ 1, 13, 11, 14 ],
        [ 1, 13, 1, 15 ],
        ]

Each number represents one pixel. There are 4 pixels in a row and 4 rows in the
whole picture.

You can test this works by iterating through the data structure. Iterating means
stepping through it. In this case you'll be using a `for loop` because it runs
the indented code _for_ each item in the list.

~~~ { .python }
for row in pixels:
    print("new row:")
    for pixel in row:
        print(pixel)
~~~

When you run the program you should see each value in the pixel data structure
printed out.

Now change your program so that instead of printing out numbers in the shell,
it creates the right coloured blocks in Minecraft.

To start with you'll need the usual stuff at the top of the program:

~~~ { .python }
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
~~~

Then add the `for loop` above. Run your program and check that you can see the
right numbers being printed out in the right order.

Now you need to create the pixels by using the `setBlock` command to create
`WOOL` blocks of different colours (like in the traffic light exercise).

You can do this by creating 2 variables, one for x position and one for y
position. 

~~~ { .python }
x = 0
y = 0
for row in pixels:
    y = y + 1
    x = 0
    for pixel in row:
        print(x, y, pixel)
        x = x + 1
~~~

Use this loop in your program, and add a `setBlock` command to create each pixel
at the correct co-ordinates.
