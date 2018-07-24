# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

from guizero import App, PushButton

Speed = 0

from guizero import App, Text, Combo


def you_chose_forward(selected_value):
    if selected_value == "0.1":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.2":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.3":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.4":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)
        
    elif selected_value == "0.5":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.6":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.7":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.8":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)
        
    elif selected_value == "0.9":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "1":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

def you_chose_backward(selected_value):
    if selected_value == "0.1":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.2":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.3":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.4":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)
        
    elif selected_value == "0.5":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.6":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.7":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "0.8":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)
        
    elif selected_value == "0.9":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)

    elif selected_value == "1":
        Speed = float(selected_value)
        print(Speed)
        robot.forward(Speed)


robot = CamJamKitRobot()

def Stop():
    robot.stop()
    
app = App()

instructions = Text(app, text="Choose a forward speed")
combo = Combo(app, options=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], command=you_chose_forward)
result = Text(app)

instructions = Text(app, text="Choose a backward speed")
combo = Combo(app, options=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], command=you_chose_backward)
result = Text(app)

Stop_button = PushButton(app, command=Stop, text="Stop")
app.display()





#while True:
 #   instruction = input("Type in f or b or s")
  #  
   # if instruction == "f":
    #    speed = float(input("Type in the speed you want"))
     #   robot.forward(speed)
    #elif instruction == "s":
     #   robot.stop()        
    #elif instruction == "b":
     #   speed = float(input("Type in the speed you want"))
      #  robot.backward(speed)
  


