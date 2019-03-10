from bluedot import BlueDot
from signal import pause
from gpiozero import CamJamKitRobot

Fwd_Speed = 0
Bck_Speed = 0
robot = CamJamKitRobot()

def swiped(swipe):
    global Fwd_Speed
    global Bck_Speed 
    if swipe.up:
        Fwd_Speed = Fwd_Speed +0.1
        print("fwd ++",str(Fwd_Speed))
        if Fwd_Speed >= 1.0:
            Fwd_Speed = 0
        robot.forward(Fwd_Speed)
    elif swipe.down:
        Bck_Speed = Bck_Speed +0.1
        print("bck ++",Bck_Speed)
        if Bck_Speed >= 1.0:
            Bck_Speed = 0
        robot.backward(Bck_Speed)
    elif swipe.left:
        print("stop")
        robot.stop()
        Bck_Speed = 0
        Fwd_Speed = 0
        
    elif swipe.right:
        print("stop")
        robot.stop()
        Bck_Speed = 0
        Fwd_Speed = 0

bd = BlueDot()

bd.when_swiped = swiped

pause()
