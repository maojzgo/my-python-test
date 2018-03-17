from PIL import Image, ImageDraw, ImageFont, ImageFilter

im=Image.open('D:/a.jpg')

im.filter(ImageFilter.EDGE_ENHANCE)

im.show()