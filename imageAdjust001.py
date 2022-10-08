from PIL import Image, ImageEnhance
img = Image.open("./Assets/IMG_3839.png")

newsize = (300, 300)
img_resized = img.resize(newsize)
print(img.size)
print(img_resized.size)
img_resized.save("resized.jpg")

# Define enhancer
enhancer = ImageEnhance.Brightness(img)
img_light = enhancer.enhance(1.8)
img_light.save("brightened.jpg")

enhancer = ImageEnhance.Brightness(img)
img_light = enhancer.enhance(0.8)
img_light.save("darkened.jpg")

# img = Image.open('testme.jpg')
img = img.convert('L')
img.save('grayscaled.jpg')
