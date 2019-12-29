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


