from PIL import Image
import os

# Upload Image
img_org = Image.open(r"C:\Users\slkn5\Desktop\Deep Learning\Image Compression\bird-8788491_1280.jpg")

# Load Image as Array
img_org_arr = img_org.load()

# Crop Image
# Define coordinates
x1 = 680 # Beginning of X
y1 = 160 # Beginning of Y
x2 = 1180 # End of X
y2 = 720 # End of Y

# Define a New Image
cropped_width = x2 - x1
cropped_height = y2 - y1
cropped_img = Image.new("RGB", (cropped_width, cropped_height))
cropped_img_arr = cropped_img.load()

# Crop the Image
for i in range(x1,x2):
    for j in range(y1,y2):
        cropped_img_arr[i - x1, j - y1] = img_org_arr[i, j]

# Display Cropped Image
cropped_img.show()

# Compress cropped image
cropped_img.save("compressed_cropped_img.jpg", quality = 30, optimize = True)

# Show File Size of Original Image and Compressed Image
org_size = os.path.getsize("Image Compression/bird-8788491_1280.jpg")
compressed_size = os.path.getsize("compressed_cropped_img.jpg")

print(f"Original file size: {org_size/1024:.2f} KB")
print(f"Compressed file size: {compressed_size/1024:.2f} KB") # File size significantly decreased due to compression process as expected. 