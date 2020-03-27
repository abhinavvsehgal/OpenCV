import cv2 as cv
import time

cap = cv.VideoCapture(0)


width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))



x = width // 2
y = height // 2 

w = width //4
h = height //4



while True:

	ret, frame = cap.read() 

	cv.rectangle(frame, (x,y), (x+w,y+h), color = (0,255,0), thickness =2)
	cv.imshow('frame', frame)
	
	if cv.waitKey(1) & 0xFF ==ord('q'):
		break
        


cap.release()
cv.destroyAllWindows()