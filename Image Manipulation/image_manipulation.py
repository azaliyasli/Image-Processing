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
cropped_img = Image.new("RGB", (x2-x1, y2-y1))
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
symmetric_img_horizontal = Image.new("RGB", (img_org.size[0], img_org.size[1]))
symmetric_img_horizontal_arr = symmetric_img_horizontal.load()

symmetric_img_vertical = Image.new("RGB", (img_org.size[0], img_org.size[1]))
symmetric_img_vertical_arr = symmetric_img_vertical.load()

# Symmetry along X axis
for i in range(0,img_org.size[0]):
    for j in range(0,img_org.size[1]):
        symmetric_img_horizontal_arr[i, (img_org.size[0]-1)-j] = img_org_arr[i, j]

# Symmetry along Y axis
for i in range(0,img_org.size[0]):
    for j in range(0,img_org.size[1]):
        symmetric_img_vertical_arr[(img_org.size[1]-1)-i, j] = img_org_arr[i, j]

img_org.show()
symmetric_img_vertical.show() # Image expected to look mirrored
symmetric_img_horizontal.show() # Image expected to look upside down

# 3. Rotation
# Define a new image
ninty_degree_counter_clockwise_rot_img = Image.new("RGB", (img_org.size[0], img_org.size[1]))
ninty_degree_counter_clockwise_rot_img_arr = ninty_degree_counter_clockwise_rot_img.load()

one_hundred_eighty_rot_img = Image.new("RGB", (img_org.size[0], img_org.size[1]))
one_hundred_eighty_rot_img_arr = one_hundred_eighty_rot_img.load()

ninty_degree_clockwise_rot_img = Image.new("RGB", (img_org.size[0], img_org.size[1]))
ninty_degree_clockwise_rot_img_arr = ninty_degree_clockwise_rot_img.load()

# Rotate 90 degree counter-clockwise
for i in range(0,img_org.size[0]):
    for j in range(0,img_org.size[1]):
        ninty_degree_counter_clockwise_rot_img_arr[j, (img_org.size[1]-i)-1] = img_org_arr[i, j]

# Rotate 180 degree
for i in range(0,img_org.size[0]):
    for j in range(0,img_org.size[1]):
        one_hundred_eighty_rot_img_arr[(img_org.size[1]-i)-1, (img_org.size[0]-j)-1] = img_org_arr[i, j]

# Rotate 90 degree clockwise (Optional)
for i in range(0,img_org.size[0]):
    for j in range(0,img_org.size[1]):
        ninty_degree_clockwise_rot_img_arr[(img_org.size[0]-j)-1, i] = img_org_arr[i, j]

ninty_degree_counter_clockwise_rot_img.show()
ninty_degree_clockwise_rot_img.show()
one_hundred_eighty_rot_img.show()

# 4. Negative Image
# Convert original image to numpy array
img_org_arr_numpy = np.array(img_org)

# Define a new image array for negative image
neg_img_arr = np.array(img_org_arr_numpy)

# Define a new image for restored image
restored_img_arr = np.array(img_org_arr_numpy)

# Take negative of image
for i in range(0,img_org_arr_numpy.shape[0]):
    for j in range(0,img_org_arr_numpy.shape[1]):
        for k in range(0,3):
            neg_img_arr[i, j, k] = 255 - img_org_arr_numpy[i, j, k]

neg_img = Image.fromarray(neg_img_arr)

# Take positive of negative image
for i in range(0,img_org_arr_numpy.shape[0]):
    for j in range(0,img_org_arr_numpy.shape[1]):
        for k in range(0,3):
            restored_img_arr[i, j, k] = 255 - neg_img_arr[i, j, k]

restored_img = Image.fromarray(restored_img_arr)

img_org.show()
neg_img.show()
restored_img.show() # Image restored by subtracting negative image from 255 again

# 5. Brightness Adjustment
# Define a new image for brighter image
br_img = Image.new("RGB", (img_org.size[0], img_org.size[1]))
br_img_arr = br_img.load()

# Define a new image for darker image
dr_img = Image.new("RGB", (img_org.size[0], img_org.size[1]))
dr_img_arr = dr_img.load()

# Brighten & Darken image
for i in range(0, img_org.size[0]):
    for j in range(0, img_org.size[1]):
        # Get original colors
        r, g, b = img_org_arr[i, j]

        # Brighten the image
        br_img_arr[i, j] = (min(255, r + 100), min(255, g + 100), min(255, b + 100)) # add +100 to each pixel, min function used to prevent not to exceed limit 255

        # Darken the img
        dr_img_arr[i, j] = (max(0, r - 100), max(0, g - 100), max(0, b - 100)) # subtract -100 from each pixel, max function used to prevent not to get negative values

img_org.show()
br_img.show()
dr_img.show()

# 6. RGB to Grayscale
grey_img = Image.new("RGB", (img_org.size[0], img_org.size[1]))
grey_img_arr = grey_img.load()

for i in range(0,img_org.size[0]):
    for j in range(0,img_org.size[1]):
        r, g, b = img_org_arr[i, j]

        grey_img_arr[i, j] = ((r+g+b)//3, (r+g+b)//3, (r+g+b)//3) # each pixel value divided by 3 to naturalize rgb colors

img_org.show()
grey_img.show()

# 7. Convert to Sepia
sepia_img = Image.new("RGB", (img_org.size[0], img_org.size[1]))
sepia_img_arr = sepia_img.load()

img_org.show()

for i in range(0,img_org.size[0]):
    for j in range(0,img_org.size[1]):
        r, g, b = img_org_arr[i, j]

        new_r = min(255, int(0.393 * r + 0.769 * g + 0.189 * b))
        new_g = min(255, int(0.349 * r + 0.686 * g + 0.168 * b))
        new_b = min(255, int(0.272 * r + 0.534 * g + 0.131 * b))

        sepia_img_arr[i, j] = (new_r, new_g, new_b)

sepia_img.show()