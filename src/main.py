import sys
#%%
import cv2 as cv

from lm_tracking import *


def main():
    if sys.argv[1] == "-d" or sys.argv[1] == "--debug":
        main_debug()
    elif sys.argv[1] == "-s" or sys.argv[1] == "--stream":
        main_stream()
    elif sys.argv[1] == "-f" or sys.argv[1] == "--frame":
        main_frame()
    else:
        incorrect_usage()



def main_frame():
    cap = cv.VideoCapture(0)

    while cap.isOpened():
        with mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            ok, frame = cap.read()
            print(pos_landmark_tracking_by_frame(pose, ok, frame))
    cap.release()


def main_stream():
    cap = cv.VideoCapture(0)
    _ = landmark_tracking(cap)
    cap.release()
    

def main_debug():
    cap = cv.VideoCapture(0)
    _ = landmark_tracking_video_out(cap)
    cap.release()


def incorrect_usage():
    print("""Usage:\n\t-d [--debug]\t:\tgenerates video-out
    \t-s [--stream]\t:\ttakes in a video stream
    \t-f [--frame]\t:\ttakes in a single frame at a time""")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        incorrect_usage()

