import cv2 as cv
import numpy as np


windowName = 'Drawing'
image = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow(windowName)



def draw_circle(event, x, y, flags, param):
	if event == cv.EVENT_FLAG_LBUTTON:
		cv.circle(image, (x,y), 20, (255, 0, 0), 3)

	if event == cv.EVENT_RBUTTONDBLCLK:
		cv.rectangle(image, (x,y), (x+150,y+150), (0, 0, 255), 3)



cv.setMouseCallback(windowName, draw_circle)

	


def main():
	while(True):
		cv.imshow(windowName, image)

		if cv.waitKey(1)==0:
			break


if __name__ == "__main__":
	main()	