from PIL import Image, ImageDraw, ImageFont
import os

image_dir = 'pngs/'

#how big we want the montage to be
crop_width = 300
crop_y_offset = 50
x_tiles = 8
y_tiles = 16 / x_tiles
mont_width = x_tiles * crop_width

font_path = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
font_size = 50
font = ImageFont.truetype(font_path, font_size)

#sums to work out how many and how big the tiles are
tile_width = mont_width / x_tiles
tile_height = tile_width
mont_height = y_tiles * tile_height
print(mont_width, mont_height)
#create a blank image
montage_image = Image.new('RGB',(mont_width,mont_height), "white")
draw = ImageDraw.Draw(montage_image)

with open('block_types') as fh:
    block_nums = fh.readlines()

all_blocks = []
for block_num in block_nums:
    try:
        block_num = int(block_num)
        all_blocks.append(block_num)
    except ValueError:
        print("skipping line" + block_num)
        continue

image_dir = 'pngs/'
all_files = os.listdir(image_dir)

x = 0
y = 0
for block in all_blocks:
    #crop just the centre of it
    file_name = image_dir + str(block) + ".png"
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
    draw.text([x*tile_width+ 5, y*tile_height+ 5],str(block), font=font, fill="black")

    x += 1
    if x > x_tiles - 1:
        x = 0
        y += 1
    
#save it!
montage_image.save("montage.jpg")

