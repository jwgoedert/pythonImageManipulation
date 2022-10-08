from PIL import Image, ImageEnhance
img = Image.open("./Assets/IMG_3839.png")

newsize = (300, 300)
img_resized = img.resize(newsize)
print(img.size)
print(img_resized.size)
img_resized.save("resized.jpg")
