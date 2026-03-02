import numpy as np
from PIL import Image

# Upload Image
img_org = Image.open(r"C:\Users\slkn5\Desktop\Deep Learning\Image Manipulation\detailed-shot-of-ripples-at-sunset-picjumbo-com.jpeg")

# Load image as array
img_org_arr = img_org.load()

# Display Image
img_org.show()

# Print Dimensions
print(img_org.size, img_org.mode)

# 1. Crop Image
# Define coordinates
x1 = 1500 # Beginning of X
y1 = 1500 # Beginning of Y
x2 = 2500 # End of X
y2 = 2500 # End of Y

# Define a new image
cropped_width = x2 - x1
cropped_height = y2 - y1
cropped_img = Image.new("RGB", (cropped_width, cropped_height))
cropped_img_arr = cropped_img.load()

# Crop the image
for i in range(x1,x2):
    for j in range(y1,y2):
        cropped_img_arr[i - x1, j - y1] = img_org_arr[i, j]

# Display Images
img_org.show()
cropped_img.show()

# 2. Symmetry
# Define a new image
symmetric_width = img_org.size[0]
symmetric_height = img_org.size[1]

symmetric_img_horizontal = Image.new("RGB", (symmetric_width, symmetric_height))
symmetric_img_horizontal_arr = symmetric_img_horizontal.load()

symmetric_img_vertical = Image.new("RGB", (symmetric_width, symmetric_height))
symmetric_img_vertical_arr = symmetric_img_vertical.load()

# Symmetry along X axis
for i in range(0,symmetric_width):
    for j in range(0,symmetric_height):
        symmetric_img_horizontal_arr[i, (symmetric_width-1)-j] = img_org_arr[i, j]

# Symmetry along Y axis
for i in range(0,symmetric_width):
    for j in range(0,symmetric_height):
        symmetric_img_vertical_arr[(symmetric_height-1)-i, j] = img_org_arr[i, j]

img_org.show()
symmetric_img_vertical.show() # Image expected to look mirrored
symmetric_img_horizontal.show() # Image expected to look upside down

# 4. Rotation
# Define a new image
rot_width = img_org.size[0]
rot_height = img_org.size[1]

ninty_degree_counter_clockwise_rot_img = Image.new("RGB", (rot_width, rot_height))
ninty_degree_counter_clockwise_rot_img_arr = ninty_degree_counter_clockwise_rot_img.load()

one_hundred_eighty_rot_img = Image.new("RGB", (rot_width, rot_height))
one_hundred_eighty_rot_img_arr = one_hundred_eighty_rot_img.load()

ninty_degree_clockwise_rot_img = Image.new("RGB", (rot_width, rot_height))
ninty_degree_clockwise_rot_img_arr = ninty_degree_clockwise_rot_img.load()

# Rotate 90 degree counter-clockwise
for i in range(0,rot_width):
    for j in range(0,rot_height):
        ninty_degree_counter_clockwise_rot_img_arr[j, (rot_height-i)-1] = img_org_arr[i, j]

# Rotate 180 degree
for i in range(0,rot_width):
    for j in range(0,rot_height):
        one_hundred_eighty_rot_img_arr[(rot_height-i)-1, (rot_width-j)-1] = img_org_arr[i, j]

# Rotate 90 degree clockwise (Optional)
for i in range(0,rot_width):
    for j in range(0,rot_height):
        ninty_degree_clockwise_rot_img_arr[(rot_width-j)-1, i] = img_org_arr[i, j]

ninty_degree_counter_clockwise_rot_img.show()
ninty_degree_clockwise_rot_img.show()
one_hundred_eighty_rot_img.show()

# 5&6. Negative Image
# Convert original image to array
img_org_arr = np.array(img_org)

# Define a new image for negative image
neg_width = img_org.size[0]
neg_height = img_org.size[1]

neg_img = Image.new("RGB", (neg_width, neg_height))

neg_img_arr = np.zeros_like(img_org_arr)

# Define a new image for restored image
restored_width = img_org.size[0]
restored_height = img_org.size[1]

restored_img = Image.new("RGB", (restored_width, restored_height))

restored_img_arr = np.zeros_like(img_org_arr)

# Take negative of image
for i in range(0,neg_width):
    for j in range(0,neg_height):
        for k in range(0,3):
            neg_img_arr[i, j, k] = 255 - img_org_arr[i, j, k]

neg_img = Image.fromarray(neg_img_arr)

# Take positive of negative image
for i in range(0,restored_width):
    for j in range(0,restored_height):
        for k in range(0,3):
            restored_img_arr[i, j, k] = 255 - neg_img_arr[i, j, k]

restored_img = Image.fromarray(restored_img_arr)

img_org.show()
neg_img.show()
restored_img.show() # Image restored by subtracting negative image from 255 again