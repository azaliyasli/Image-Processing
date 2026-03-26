from PIL import Image
import numpy as np

# Upload Image and Convert to RGB
img = Image.open(r"C:\Users\slkn5\Desktop\Deep Learning\Brigthness and Contrast\pngtree-tranquil-waterfall-and-vibrant-flowers-at-sunset-picture-image_15899089.jpg").convert("RGB")

# Define Variables
b_sum = 0
c_sum = 0

# Convert Image to Array
img_arr = np.array(img, dtype=int)

# Find Brightness of Image
for i in range(0,img_arr.shape[0]):
    for j in range(0, img_arr.shape[1]):
        for k in range(0,3):
            b_sum += img_arr[i,j,k]
brightness = b_sum / (img_arr.shape[0] * img_arr.shape[1] * 3)

# Find Contrast of Image
for i in range(0,img_arr.shape[0]):
    for j in range(0,img_arr.shape[1]):
        for k in range(0,3):
            c_sum += abs(img_arr[i,j,k]-brightness)
contrast = c_sum / (img_arr.shape[0] * img_arr.shape[1] * 3)

# Print the Results
print(f"""Brightness: {brightness}
Contrast: {contrast}""")