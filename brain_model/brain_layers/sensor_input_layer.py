# Test controls based on an array grid for a particle of sorts.
# OpenCV or some camera control.
import cv2
class Sensor:
    # Do something with camera input
    def __init__(self):
        print("Ready")

    def push_to_apl(self):
        return 1
    
    def open_sensors(self):
        return 0
    
    def test_sensors(self):
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        
        while rval:
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27:
                break
        
        cv2.destroyWindow("preview")
        vc.release()