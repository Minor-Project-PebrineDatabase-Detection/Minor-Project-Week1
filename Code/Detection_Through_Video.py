import cv2
import numpy as np
import sys

sys.path.insert(0, './Helper')
from Helper.Motion_Detection import MotionDetection
isclosed = 0

def start_vid():
    while True:

        # Capturing video
        video = cv2.VideoCapture('../pebrin database/Video-7_2019-08-14.wmv')

        if MotionDetection(video) == False:
            break

    video.release()

    # Destroying all the windows
    cv2.destroyAllWindows()

# if __name__== "__main__":
#     main()
