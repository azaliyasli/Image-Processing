from PIL import Image

img = Image.open("Brightness and Contrast/istockphoto-1054266396-612x612.jpg")

b_sum = 0
c_sum = 0

for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        b_sum += img.getpixel((i, j))
brightness = b_sum / (img.size[0]*img.size[1])

print("Brightness: ", brightness)

for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        c_sum += abs(img.getpixel((i, j))-brightness)
contrast = c_sum / (img.size[0]*img.size[1])

print("Contrast: ", contrast)