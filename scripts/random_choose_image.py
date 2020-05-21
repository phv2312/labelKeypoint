import os
from PIL import Image

##
IMAGE_PER_DIR = 2
##

input_dir  = "/home/kan/Desktop/Cinnamon/datapile/geek/HOR01_Full_Formated/HOR01_Full_Formated"
output_dir = "processed_hor01"

# ------------------------
if not os.path.exists(output_dir): os.makedirs(output_dir)
#if not os.path.exists(os.path.join(output_dir, 'images')): os.makedirs(os.path.join(output_dir, 'images'))

dirs = os.listdir(input_dir)

results = {}

for dir in dirs:
    print ('processing %s ...' % dir)

    try:
        _full_path_color = os.path.join(input_dir, dir, 'color')
        ims = os.listdir(_full_path_color)
        print ('>> total:', len(ims))

        # save to excel
        results[dir] = ims[:IMAGE_PER_DIR]
    except Exception as e:
        print ('Exception:', e)

# rename and re-save
count_offset = 1

for dir, ims in results.items():
    for im in ims:
        offset_dir = 1 + (count_offset / 20)

        if not os.path.exists(os.path.join(output_dir, str(offset_dir), 'images')):
            os.makedirs(os.path.join(output_dir, str(offset_dir), 'images'))

        in_im_path  = os.path.join(input_dir, dir, 'color', im)
        out_im_path = os.path.join(output_dir, str(offset_dir), 'images', "%s_POSE_%s.png" % (dir, os.path.splitext(im)[0]))

        print ('save to %s ...' % out_im_path)
        Image.open(in_im_path).save(out_im_path)

        count_offset += 1