import pylibfreenect2 as kinect
import cv2
import numpy as np
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

fn = kinect.Freenect2()
assert fn.enumerateDevices() > 0
serial = fn.getDeviceSerialNumber(0)
device = fn.openDevice(serial)

typ = 'ir'

if typ == 'depth':
    listener = kinect.SyncMultiFrameListener(kinect.FrameType.Depth)
else:
    listener = kinect.SyncMultiFrameListener(kinect.FrameType.Ir)

device.setIrAndDepthFrameListener(listener)
device.start()

pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

while True:
    frames = kinect.FrameMap()
    listener.waitForNewFrame(frames)

    # color = frames[kinect.FrameType.Color]
    if typ == 'depth':
        depth = frames[kinect.FrameType.Depth]
        arr = depth.asarray()
    else:
        ir = frames[kinect.FrameType.Ir]
        arr = ir.asarray()

    maximum = arr.max()
    image = np.rint((arr/maximum)*255).astype(np.uint8)
    listener.release(frames)
    image.flags.writeable = False
    image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
    #image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
    results = pose.process(image)

    print(results.pose_landmarks)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break