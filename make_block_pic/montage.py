from PIL import Image, ImageDraw, ImageFont
from block_names import names
import os
import math

image_dir = 'block-pngs/'
id_file = 'block_types'

with open(id_file) as fh:
    block_nums = fh.readlines()

#how big we want the montage to be
crop_width = 280
crop_y_offset = 50
x_tiles = 7
print(len(block_nums))
y_tiles = int(math.ceil(len(block_nums) / float(x_tiles)))
mont_width = x_tiles * crop_width

font_path = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
id_font_size = 40
id_font = ImageFont.truetype(font_path, id_font_size)
text_font_size = 20
text_font = ImageFont.truetype(font_path, text_font_size)

#sums to work out how many and how big the tiles are
tile_width = mont_width / x_tiles
tile_height = tile_width
mont_height = y_tiles * tile_height
print(mont_width, mont_height)
#create a blank image
montage_image = Image.new('RGB',(mont_width,mont_height), "white")
draw = ImageDraw.Draw(montage_image)


all_blocks = []
for block_num in block_nums:
    try:
        block_num = int(block_num)
        all_blocks.append(block_num)
    except ValueError:
        print("skipping line" + block_num)
        continue

all_files = os.listdir(image_dir)

x = 0
y = 0
for block_id in all_blocks:
    #crop just the centre of it
    file_name = image_dir + str(block_id) + ".png"
    print(file_name)
    tile = Image.open(file_name)
    w, h = tile.size
    crop_box = (
        w / 2 - crop_width / 2,
        h / 2 - crop_width / 2 - crop_y_offset,
        w / 2 + crop_width / 2,
        h / 2 + crop_width / 2 - crop_y_offset, )
    crop = tile.crop(crop_box)
    print(crop.size)

    # resize it
    crop.thumbnail((tile_width,tile_width))

    # paste it in
    box=(x*tile_width,y*tile_height,x*tile_width+tile_width,y*tile_height+tile_width)
    montage_image.paste(crop,box)
    for block_name in names.keys():
        if names[block_name] == block_id:
            text = block_name
    draw.text([x*tile_width+ 5, y*tile_height+ 5],text, font=text_font, fill="black")
    draw.text([x*tile_width+ 5, y*tile_height+ text_font_size*1.2],str(block_id), font=id_font, fill="black")

    x += 1
    if x > x_tiles - 1:
        x = 0
        y += 1
    
#save it!
montage_image.save("montage.jpg")

