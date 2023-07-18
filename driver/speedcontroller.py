import time
from multiprocessing import Process
from settings import SPEED_KP, SPEED_KI, SPEED_KD, MOTOR_STEP_TIME, MOTOR_MAXIMUM_STATE


class SpeedController(Process):

    def __init__(self, speed, targetSpeed, targetDirection, encoderLock, distance, bottomQueue, shutdownQueue):
        super().__init__()
        self.daemon = True
        self.speed = speed
        self.targetSpeed = targetSpeed
        self.targetDirection = targetDirection
        self.encoderLock = encoderLock
        self.distance = distance
        self.bottomQueue = bottomQueue
        self.shutdownQueue = shutdownQueue

        with self.targetDirection.get_lock():
            self.direction = self.targetDirection.value
        self.arduinoSpeed = 0


    def run(self):
        prevTime = time.time()
        with self.encoderLock:
            prevDistance = self.distance.value
        prevError = 0
        integral = 0
        time.sleep(1)

        while self.shutdownQueue.empty():

            currentTime = time.time()
            dt = currentTime - prevTime
            with self.encoderLock:
                currentDistance = self.distance.value
            distanceTraveled = abs(currentDistance - prevDistance)/10
            speed = distanceTraveled/dt
            with self.speed.get_lock():
                self.speed.value = speed
            with self.targetSpeed.get_lock():
                targetSpeed = self.targetSpeed.value
            with self.targetDirection.get_lock():
                targetDirection = self.targetDirection.value

            if targetSpeed == 0 or targetDirection != self.direction:
                if speed != 0:
                    self.arduinoSpeed = 0
                    self.bottomQueue.put([220, self.arduinoSpeed, MOTOR_STEP_TIME])
                elif targetDirection != self.direction:
                    self.bottomQueue.put([221,])
                    self.direction = targetDirection
                error = 0
            else:
                error = targetSpeed - speed
                integral = integral + error*dt
                derivative = (error - prevError)/dt
                output = int(round(SPEED_KP*error + SPEED_KI*integral + SPEED_KD*derivative))

                if output != 0:
                    if self.arduinoSpeed == 0:
                        self.arduinoSpeed = 20
                    self.arduinoSpeed += output
                    if self.arduinoSpeed > MOTOR_MAXIMUM_STATE:
                        self.arduinoSpeed = MOTOR_MAXIMUM_STATE
                    elif self.arduinoSpeed < 0:
                        self.arduinoSpeed = 0
                    self.bottomQueue.put([220, self.arduinoSpeed, MOTOR_STEP_TIME])
                
                #print(speed, self.arduinoSpeed, output, error, integral, derivative)

            prevTime = currentTime
            prevDistance = currentDistance
            prevError = error
            time.sleep(0.1)

        print('SpeedController shutting down...')
        self.bottomQueue.put([220, 0, MOTOR_STEP_TIME])


