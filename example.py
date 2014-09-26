import v4l2
import logging
import cv2
from time import time
logging.basicConfig(level=logging.DEBUG)
from time import time,sleep

import numpy as np



cap = v4l2.Capture("/dev/video0")
# cap.transport_formats
# print cap.frame_rate 
# print cap.frame_size b
# print cap.transport_format,cap.transport_formats

cap.frame_size = (800, 600)
cap.frame_rate= (1,30)
cap.enum_controls()
cap.set_control(9963776,120)
print cap.get_control(9963776)
print 'Will capture at:',cap.transport_format,cap.frame_size,cap.frame_rate
for x in range(0):
	frame = cap.get_frame()
	# print frame.width,frame.height
	# print frame.d
	# y= frame.gray
	# print v.shape
	img = frame.yuv
	y,u,v = img
	# y = frame.bgr
	# print y.data
	# y = np.ones((1080,1920,1))
	# print y[].shape
	# print u[]s.shape
	cv2.imshow("img",y)
	# cv2.imshow("u",u)
	# cv2.imshow("v",v)

	cv2.waitKey(1)
	# print img
cap.close()
cap = None


import numpy as np

d = np.ones((1920,1080))
print d.shape
print d[::2,:].shape
