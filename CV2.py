import cv2 as cv
import numpy as np


cam = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
count =0
faceData = []
username = input("enter your name")


while (True):
	ret,frame = cam.read()
	if ret ==False:
		print("Something went wrong")
		continue

	key_pressed = cv.waitKey(1)&0xFF
	if key_pressed == ord('q'):
		break


		
	#bright_image = frame + 100
	#bright_image[bright_image > 255] = 250	
	faces = face_cascade.detectMultiScale(frame,  1.3, 5)
	if(len(faces)==0):
		continue
	for face in faces:
		x,y,w,h = face #x,y,w,h is a tuple
		face_section = frame[y-10:y+h+10, x-10:x+w+10];
		face_section = cv.resize(face_section,(100,100))


		cv.putText(frame, username, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), )
		cv.rectangle(frame,(x,y),(x+w, y+h),(0, 255, 255), 2)


		pred = knn()

		if count%10 ==0:
			print("Taking picture", count//10)
			faceData.append(face_section)
		count+=1	


		

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	cv.imshow("video title", frame)
	cv.imshow("Video Gray", face_section)	
	#saving the data in a numpy array
faceData = np.array(faceData)
faceData = faceData.reshape((faceData.shape[0], -1))	



np.save("FaceData"+ username + " .npy", faceData)
print("Saved at faceData/" +username+ ".npy")



print(faceData.shape)

cam.release()
cam.destroyAllWindows()