import cv2 as cv
#import matplotlib.pyplot as plt 
 

def main():

	windowName = "Live Video Feed"
	cv.namedWindow(windowName)
	
	cap = cv.VideoCapture(0)

	if cap.isOpened():
		ret, frame = cap.read()
		print(ret)
		print(frame)
 
	else:
		ret = False

	while ret:
		ret, frame = cap.read()

		output = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
		cv.imshow(windowName, output)



		if waitKey(1) == 27:
			break



	cap.release()


if __name__ == "___main__":
	main()
