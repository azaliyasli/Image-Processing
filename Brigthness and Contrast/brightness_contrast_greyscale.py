from PIL import Image

# Load Image
img = Image.open(r"C:\Users\slkn5\Desktop\Deep Learning\Brigthness and Contrast\istockphoto-1054266396-612x612.jpg")

# Define Variables
b_sum = 0
c_sum = 0

# Conver Image to Array
img_arr= img.load()

# Calculate Brightness
for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        b_sum += img_arr[i,j]
brightness = b_sum / (img.size[0]*img.size[1])

print("Brightness: ", brightness)

# Calculate Contrast
for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        c_sum += abs(img_arr[i,j]-brightness)
contrast = c_sum / (img.size[0]*img.size[1])

print("Contrast: ", contrast)