import cv2
import numpy as np

hole_count = 0

img_bgr = cv2.imread('foam sheet test 2.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

def main():
        find_w_template('foam_hole_4.jpg')
        #find_w_template('foam_hole_3.jpg')
        resized_image = cv2.resize(img_bgr, (0,0), fx=1, fy=1)
        cv2.imshow('detected', resized_image)
        print('found ' + str(hole_count) + ' holes with template')

        find_circles(img_bgr)

        # cv2.imshow("output", np.hstack([resized_image, output]))

def find_w_template(template_file):
        template = cv2.imread(template_file, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
                cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+w), (0, 255, 255), 2)
                global hole_count
                hole_count += 1

def find_circles(image):
 	# https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/
	
 	circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.5, 30)
 	if circles is not None:
 		# convert the (x, y) coordinates and radius of the circles to integers
 		circles = np.round(circles[0, :]).astype("int")
 
 	# loop over the (x, y) coordinates and radius of the circles
 	for (x, y, r) in circles:
 		# draw the circle in the output image, then draw a rectangle
 		# corresponding to the center of the circle
 		#cv2.circle(output, (x, y), r, (0, 255, 0), 4)
 		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
 	return output
	


if __name__ == "__main__":
	main()

