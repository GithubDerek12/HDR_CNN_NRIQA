# -*- coding: utf-8 -*-
#from model import *
import matplotlib.pyplot as plt
import cv2
import numpy as np
# Basic working example shown below. Sampling here is by non overlapping patches.
# The weights given with the code is trained for the whole dataset for 2 epochs.

#####获取图像亮度值#####################################
def get_luminance(img):
	max_Lum = 4250.0
	min_Lum = 0.03
	try:
		[iw,ih,ch] 	= np.shape(img)
		lum = 0.2126*img[:,:,0] + 0.7152*img[:,:,1] + 0.0722*img[:,:,2]
	except :
		[iw,ih] 	= np.shape(img)
		lum = img
	lum = np.clip(lum,min_Lum, max_Lum)
	return lum
########################################################
if __name__=="__main__":
	fname = "data\\test1.jpg"
	# qmodel  = model_IQA_HDR(load_weights=1)
	# [quality,fmap] = qmodel.predict_quality(fname, draw=0)
	plt.imshow(np.log(get_luminance(cv2.imread(fname))))
	plt.title("Log distorted luminance")
	plt.colorbar()
	plt.show()
	# plt.imshow(fmap)
	# plt.title(str(quality))
	# plt.colorbar()