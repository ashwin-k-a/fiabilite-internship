from PIL import Image
import cv2

background = Image.open("road.png")
foreground = Image.open("car.png")

background.show()
cv2.waitKey(0)


foreground.show()
cv2.waitKey(0)

background.paste(foreground, (500, 500), foreground)
background.show()
