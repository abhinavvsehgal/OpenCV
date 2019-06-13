import cv2 as cv
import numpy as np





def emptyFunction():
	pass



def main():
	
	image = np.zeros((512, 512, 3), np.uint8)
	windowName = 'Open CV BGR Color Palette'
	cv.namedWindow(windowName)
	cv.createTrackbar('B', windowName, 0, 255, emptyFunction)
	cv.createTrackbar('G', windowName, 0, 255, emptyFunction)
	cv.createTrackbar('R', windowName, 0, 255, emptyFunction)

	while(True):
		cv.imshow(windowName, image)



		if cv.waitKey(1)==0:
			break


		blue = cv.getTrackbarPos('B', windowName)
		green = cv.getTrackbarPos('G', windowName)
		red = cv.getTrackbarPos('R', windowName)

		image[:] = [blue, green, red]
		print(blue, green, red)

		
	cv.destroyAllWindows()



if __name__ == "__main__":
	main()	