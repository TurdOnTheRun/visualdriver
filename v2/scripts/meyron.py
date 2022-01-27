buildUp = thatSpatialEvolvingFuzz([(0.15,0.025), (0.15,0.025), (0.15,0.025), (0.15,0.025), (0.15,0.025), (0.15,0.025), (0.15,0.035)], 5, (40, 50), (10,20), [(Top1, 100), (Top2, 100), (Top3, 100), (Top4, 100)])
bigBumps = thatSpatialEvolvingFuzz([(0.3, 0.035), (0.3, 0.035), (0.3, 0)], 8, (40, 50), (10,20), [(Top1, 100), (Top2, 100), (Top3, 100), (Top4, 100)])
eventDict = buildUp
eventDict['position'] += bigBumps['position']
eventDict['time'] += bigBumps['time']
eventDict['position'] = [MotorSpeed(At(0), 70, 30), TimeEventsUnblock(At(0.5))] + eventDict['position']
eventDict['time'] = [TimeEventsBlock(At(0)),] + eventDict['time']



# eventDict = dancingInTheVoid(28, (50,70), [(Top1, 100), (Top2, 100), (Top3, 100), (Top4, 100)], motorspeed=100, accelerationArc=0.5)
