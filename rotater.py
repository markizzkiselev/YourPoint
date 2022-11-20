import PIL
from PIL import Image


im = Image.open(f'arrow_left.png')
im_rotate = im.transpose(Image.FLIP_LEFT_RIGHT)
im_rotate.save('arrow.png')
