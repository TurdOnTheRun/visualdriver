from multiprocessing import Process
from ctypes import Structure, c_double
import time

import pylibfreenect2 as kinect
import cv2
import numpy as np
import mediapipe as mp
mp_pose = mp.solutions.pose

NOSE = 0
LEFT_EYE_INNER = 1
LEFT_EYE = 2
LEFT_EYE_OUTER = 3
RIGHT_EYE_INNTER = 4
RIGHT_EYE = 5
RIGHT_EYE_OUTER = 6
LEFT_EAR = 7
RIGHT_EAR = 8
MOUTH_LEFT = 9
MOUTH_RIGHT = 10
LEFT_SHOULDER = 11
RIGHT_SHOULDER = 12
LEFT_ELBOW = 13
RIGHT_ELBOW = 14
LEFT_WRIST = 15
RIGHT_WRIST = 16
LEFT_PINKY = 17
RIGHT_PINKY = 18
LEFT_INDEX = 19
RIGHT_INDEX = 20
LEFT_THUMB = 21
RIGHT_THUMB = 22
LEFT_HIP = 23
RIGHT_HIP = 24
LEFT_KNEE = 25
RIGHT_KNEE = 26
LEFT_ANKLE = 27
RIGHT_ANKLE = 28
LEFT_HEEL = 29
RIGHT_HEEL = 30
LEFT_FOOT_INDEX = 31
RIGHT_FOOT_INDEX = 32


class KinectReader(Process):

    def __init__(self, lock, queue, shutdownQueue):
        super().__init__()
        self.daemon = True
        self.lock = lock
        self.queue = queue
        self.shutdownQueue = shutdownQueue

    def run(self):
        print('Setting up Kinect...')
        try:
            fn = kinect.Freenect2()
            assert fn.enumerateDevices() > 0
            serial = fn.getDeviceSerialNumber(0)
            device = fn.openDevice(serial)
            listener = kinect.SyncMultiFrameListener(kinect.FrameType.Ir)
            pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
            device.setIrAndDepthFrameListener(listener)
            device.start()
        except Exception as e:
            print('Failed to connect to Kinect')
            raise e
        print('Kinect ready!')
        while True:
            if not self.shutdownQueue.empty():
                print("Shutting down kinect...")
                device.stop()
                device.close()
            frames = kinect.FrameMap()
            listener.waitForNewFrame(frames)
            ir = frames[kinect.FrameType.Ir]
            arr = ir.asarray()
            maximum = arr.max()
            image = np.rint((arr/maximum)*255).astype(np.uint8)
            listener.release(frames)
            image.flags.writeable = False
            image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
            # image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
            results = pose.process(image)
            if results.pose_landmarks:
                res = []
                for data_point in results.pose_landmarks.landmark:
                    res.append((data_point.x, data_point.y, data_point.z, data_point.visibility))
                with self.lock:
                    while not self.queue.empty():
                        self.queue.get()
                    self.queue.put(res)
