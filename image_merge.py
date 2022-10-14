import cv2
import cvzone

cap = cv2.imread("3.jpg")
img_video = cv2.imread("4.jpg", cv2.IMREAD_UNCHANGED)
imgResult = cvzone.overlayPNG(cap, img_video, [0, 0])
cv2.imshow("h", imgResult)
cv2.waitKey(0)

# from PIL import Image
#
# # Load the image and convert to 32-bit RGBA
# im = Image.open("5.jpg").convert('RGBA')
#
# # Save result
# im.save("6.png")