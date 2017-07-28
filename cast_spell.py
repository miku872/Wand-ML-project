from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import start
import draw_spell
global s
global t
import time
from multiprocessing import Process,Pipe
import speech_recognition as sr 
def f(conn): 

# obtain audio from the microphone  
	r = sr.Recognizer()
	with sr.Microphone() as source:
	# listen for 5 seconds and create the ambient noise energy level  
	    r.adjust_for_ambient_noise(source, duration=1)
	    print("bhaunk kutte")
	    audio = r.listen(source)  

	    # recognize speech using Sphinx  
	try:  
	    conn.send(r.recognize_google(audio))
	    conn.close
	except sr.UnknownValueError:  
	    return 'dead nigga' 
	except sr.RequestError as e:  
	    return 'dead nigga'
np.set_printoptions(threshold=np.inf)
def feedforward(a):
        """Return the output of the network if ``a`` is input."""
	for b, w in zip(s,t):		
		print ""
		a = sigmoid(np.dot(w, a)+b)
	return a

def evaluate(test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""

	test_results = [np.argmax(feedforward(test_data[0][0])), test_data[0][1]]
	return test_results[0]
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

s,t=start.start()

# define the lower and upper boundaries of the "green"
# ball in the HSV color space
greenLower = (33,157, 131)
greenUpper = (255, 255, 255)

def g(conn):
	
	camera = cv2.VideoCapture(0)
		#press q for start
				
	pts = deque()
	counter = 0
	#(dX, dY) = (0, 0)
	#direction = ""

	# keep looping
	(grabbed, frame) = camera.read()
	
	cv2.startWindowThread()
	while True:

	# grab the curr9ent frame
		

		(grabbed, frame) = camera.read()
		frame = cv2.flip(frame,1)
 
	# resize the frame, blur it, and convert it to the HSV
	# color space
		frame = imutils.resize(frame, width=1000)
		blurred = cv2.GaussianBlur(frame, (11, 11), 0)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
		mask = cv2.inRange(hsv, greenLower, greenUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
 
	# find contours in the mask and initialize the current
	# (x, y) center of the ball
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)[-2]
		center = None

	# only proceed if at least one contour was found
		if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
		# only proceed if the radius meets a minimum size
			if radius > 15:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
				cv2.circle(frame, (int(x), int(y)), int(radius),
					(0, 255, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)
				pts.appendleft(center)
	# loop over the set of tracked points
		for i in np.arange(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
			if pts[i - 1] is None or pts[i] is None:
				continue
 	
			thickness = 8
			cv2.line(frame, pts[i - 1], pts[i], (255, 255, 255), thickness)
 
	# show the frame to our screen and increment the frame counter
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		counter += 1
 
	# if the 'p' key is pressed, stop the loop
		if key == ord("p"):	
			#cv2.destroyAllWindows()	
			camera.release()
			del(camera)		
			break
		#print pp
	# cleanup the camera and close any open windows


	d=draw_spell.draw(pts)
	#cv2.destroyAllWindows()
	z=evaluate(d)
	if z==0:
		conn.send(z)
		conn.close
	elif z==1:
		conn.send(z)
		conn.close
	elif z==2:
		conn.send(z)
		conn.close
	elif z==3:
		conn.send(z)
		conn.close
	elif z==4:
		conn.send(z)
		conn.close
	elif z==5:
		conn.send(z)
		conn.close
	elif z==6:
		conn.send(z)
		conn.close
	elif z==7:
		conn.send(z)
		conn.close
	elif z==8:
		conn.send(z)
		conn.close
	elif z==9:
		conn.send(z)
		conn.close
while(True):
	p_conn,c_conn=Pipe()
	p1 = Process(target=f,args=(c_conn,))
	p1.start()
	p2 = Process(target=g,args=(p_conn,))
	p2.start()
	v_data=p_conn.recv()
	w_data=c_conn.recv()
	if(v_data=='expecto Patronum' and w_data==0):
		print(v_data)
		print(v_data,w_data)
	elif(v_data=='lumos' and w_data==1):
		print(v_data)
		print(v_data,w_data)
	elif(v_data=='Stupify' and w_data==2):
		print(v_data)
		print(v_data,w_data)
	elif(v_data=='accio' and w_data==3):
		print(v_data)
		print(v_data,w_data)
	elif(v_data=='Wingardium Leviosa' and w_data==4):
		print(v_data)
		print(v_data,w_data)
	elif(v_data=='petrificus totalus' and w_data==5):
		print(v_data)
		print(v_data,w_data)
	elif(v_data=='imperio' and w_data==6):
		print(v_data)
		print(v_data,w_data)
	elif(v_data=='Avada Kedavra' and w_data==7):
		print(v_data)
		print(v_data,w_data)
	elif(v_data=='crucio' and w_data==8):
		print(v_data)
		print(v_data,w_data)
	elif(v_data=='Expelliarmus' and w_data==9):
		print(v_data)
		print(v_data,w_data)	
	else:
		print("you're dead nigga")
		print(v_data,w_data)
	p1.join()
	p2.join()	



	
		
