from PIL import Image
import sys
import cv2


if __name__ =='__main__':
	# Image.open(sys.argv[1]).convert('RGB').save('test.pgm','ppm')
	img = cv2.imread(sys.argv[1])
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	if len(sys.argv)>2:
		outputfile = sys.argv[2]
	else:
		outputfile = '{0}.pgm'.format(sys.argv[1].rsplit('.',1)[0])
	

	cv2.imwrite(outputfile,img)