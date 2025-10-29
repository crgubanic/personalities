from PIL import Image

img = Image.open("background.png")

img.save("background.webp", "WEBP", quality=85)