import numpy as np
import cv2
from collections import deque
def draw(pts):
	img=np.zeros((640,640,3), np.uint8)
	for i in np.arange(1, len(pts)):
		if pts[i - 1] is None or pts[i] is None:
			continue
		else:
			cv2.line(img,pts[i-1], pts[i] , (0,0,255),  3)	
	while True:
		cv2.imshow('spell',img)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			break	
			
	
	return img
