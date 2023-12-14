import cv2 as cv
import mediapipe as mp

import constants


def landmark_tracking(cap: cv.VideoCapture):
    with mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                continue

            pos = (0, 0)
            landmarks = []

            results = pose.process(frame)
            if results.pose_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
                frame_height, frame_width, _ = frame.shape
                for landmark in results.pose_landmarks.landmark:
                    landmarks.append((((landmark.x * frame_width) - frame_width/2) * landmark.visibility,
                                      ((landmark.y * frame_height) - frame_height / 2) * landmark.visibility))

            x, y = 0, 0
            for lm in landmarks:
                x += lm[0]
                y += lm[1]
            if x != 0 and y != 0:
                l = len(landmarks)
                pos = (x / l), (y / l)

            #TODO Moet per integratie deze waarde gebruiken om de motoren aan te sturen i.p.v. naar de console te
            # printen
            print(pos)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()


def landmark_tracking_video_out(cap: cv.VideoCapture):
    with mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                continue

            pos = (0, 0)
            landmarks = []

            results = pose.process(frame)
            if results.pose_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
                frame_height, frame_width, _ = frame.shape
                for landmark in results.pose_landmarks.landmark:
                    landmarks.append((((landmark.x * frame_width) - frame_width/2) * landmark.visibility,
                                      ((landmark.y * frame_height) - frame_height / 2) * landmark.visibility))

            x, y = 0, 0
            for lm in landmarks:
                x += lm[0]
                y += lm[1]
            if x != 0 and y != 0:
                l = len(landmarks)
                pos = (x / l), (y / l)

            cv.namedWindow("main", cv.WINDOW_NORMAL)
            cv.resizeWindow("main", constants.FRAME_SIZE[0], constants.FRAME_SIZE[1])
            cv.imshow("main", frame)

            print(pos)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()


def pos_landmark_tracking_by_frame(pose, ok, frame) -> (float, float):
    pos = (None, None)
    if not ok:
        return pos

    landmarks = []
    results = pose.process(frame)
    if results.pose_landmarks:
        frame_height, frame_width, _ = frame.shape
        for landmark in results.pose_landmarks.landmark:
            landmarks.append((((landmark.x * frame_width) - frame_width/2) * landmark.visibility,
                              ((landmark.y * frame_height) - frame_height / 2) * landmark.visibility))

    x, y = 0, 0
    for lm in landmarks:
        x += lm[0]
        y += lm[1]
    if x != 0 and y != 0:
        pos = (x / len(landmarks), y / len(landmarks))
    return pos
#%%
