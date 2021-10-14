from PIL import Image
import glob
import cv2

for file in glob.glob("car_alpha.png"):
 im = Image.open(file)
 rgb_im = im.convert('RGB')
 rgb_im.save(file.replace("png", "jpg"), quality=95)



fir = Image.open("car_alpha.png")
sec = Image.open("car_alpha.jpg")

fir.show()
cv2.waitKey(0)


sec.show()
cv2.waitKey(0)
