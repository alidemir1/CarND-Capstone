from styx_msgs.msg import TrafficLight
import os
import cv2
import numpy as np


class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        cimg = image
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # color range
        lower_red1 = np.array([0,10,100]) #np.array([0,100,100])
        upper_red1 = np.array([0,0,255]) #np.array([10,255,255])
        lower_red2 = np.array([160,100,100])
        upper_red2 = np.array([180,255,255])
        lower_green = np.array([40,50,50])
        upper_green = np.array([90,255,255])
        # lower_yellow = np.array([15,100,100])
        # upper_yellow = np.array([35,255,255])
        lower_yellow = np.array([15,150,150])
        upper_yellow = np.array([35,255,255])
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        maskg = cv2.inRange(hsv, lower_green, upper_green)
        masky = cv2.inRange(hsv, lower_yellow, upper_yellow)
        maskr = cv2.add(mask1, mask2)

        size = image.shape
        # print size

        # hough circle detect
        r_circles = cv2.HoughCircles(maskr, cv2.HOUGH_GRADIENT, 1, 80,
                                   param1=50, param2=10, minRadius=0, maxRadius=30)

        g_circles = cv2.HoughCircles(maskg, cv2.HOUGH_GRADIENT, 1, 60,
                                     param1=50, param2=10, minRadius=0, maxRadius=30)

        y_circles = cv2.HoughCircles(masky, cv2.HOUGH_GRADIENT, 1, 30,
                                     param1=50, param2=5, minRadius=0, maxRadius=30)

        # traffic light detect
        if r_circles is not None:
            return TrafficLight.RED

        if g_circles is not None:
            return TrafficLight.GREEN

        if y_circles is not None:
            return TrafficLight.YELLOW
           
                    
        #TODO implement light color prediction
        return TrafficLight.UNKNOWN
