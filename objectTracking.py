import cv2

cap=cv2.VideoCapture(0)
tracker=cv2.TrackerKCF_create()

_,img = cap.read()
bbox =cv2.selectROI('Tracker',img,False)
tracker.init(img,bbox)

def drawBox(img,bbox):
	x,y,w,h=map(int,bbox)
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),3,1)
	cv2.putText(img,'Tracking',(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

while True:
	_,img=cap.read()
	success,bbox=tracker.update(img)
	if success:
		drawBox(img,bbox)
	else:
		cv2.putText(img,'Lost',(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
	cv2.imshow('Object Tracker',img)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break