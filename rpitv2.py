# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

from guizero import App, PushButton
from guizero import App, Slider, TextBox


from guizero import App, Text, Combo
from time import sleep


Speed = 0




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
        robot.backward(Speed)

    elif selected_value == "0.2":
        Speed = float(selected_value)
        print(Speed)
        robot.backward(Speed)

    elif selected_value == "0.3":
        Speed = float(selected_value)
        print(Speed)
        robot.backward(Speed)

    elif selected_value == "0.4":
        Speed = float(selected_value)
        print(Speed)
        robot.backward(Speed)
        
    elif selected_value == "0.5":
        Speed = float(selected_value)
        print(Speed)
        robot.backward(Speed)

    elif selected_value == "0.6":
        Speed = float(selected_value)
        print(Speed)
        robot.backward(Speed)

    elif selected_value == "0.7":
        Speed = float(selected_value)
        print(Speed)
        robot.backward(Speed)

    elif selected_value == "0.8":
        Speed = float(selected_value)
        print(Speed)
        robot.backward(Speed)
        
    elif selected_value == "0.9":
        Speed = float(selected_value)
        print(Speed)
        robot.backward(Speed)

    elif selected_value == "1":
        Speed = float(selected_value)
        print(Speed)
        robot.backward(Speed)

def slider_changed(slider_value):
    textbox.value = float(slider_value)/100
    robot.forward(float(slider_value)/100)

def Turtle():
    Speed = 0.3
    print(Speed)
    robot.forward(Speed)
    sleep(5)
    robot.stop()
    sleep(12)
    robot.backward(Speed)
    sleep(5)
    robot.stop()

robot = CamJamKitRobot()

def Stop():
    robot.stop()
    

app = App()

slider = Slider(app, command=slider_changed)
textbox = TextBox(app)

instructions = Text(app, text="Choose a forward speed")
combo = Combo(app, options=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], command=you_chose_forward)
combo.width = 60
combo.height = 5
result = Text(app)




instructions = Text(app, text="Choose a backward speed")
combo = Combo(app, options=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], command=you_chose_backward)
combo.width = 60
combo.height = 5
result = Text(app)

Turtle_button = PushButton(app, command=Turtle, text="Turtle")
Turtle_button.width = 20
Turtle_button.height = 10


Stop_button = PushButton(app, command=Stop, text="Stop")
Stop_button.width = 20
Stop_button.height = 10


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
  

