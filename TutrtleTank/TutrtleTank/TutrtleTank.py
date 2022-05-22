#Alexander King
#CSET 3150.041
#Introduction to Algorithms
#June 9th 2021
#Tank Class

import turtle
 
screen = turtle.Screen()
screen.setup(500,500)
screen.tracer(0)            # tell screen to not show automatically
tur = turtle.Turtle()
tur.speed(0)                #draw as fast as possible
tur.width(4)
tur.hideturtle()            # hide the turtle
 
 

#movespeed=.8
#pos=0
forward=True



class Tank:
    def __init__(tank, squareRange, triangleRange, sizeL, rightA, triA, sqC, triC):
        tank.squareRange = squareRange
        tank.triangleRange = triangleRange
        tank.sizeL = sizeL
        tank.rightAngle = rightA
        tank.triA = triA
        tank.sqC = sqC
        tank.triC = triC
        tank.dir = dir
        #tank.startPOS = startPOS
        #startPOS = randint(0,359)
t1 = Tank(4,3,100,90,-360/3,"green","blue")  #square has *4* sides, triangle has *3* sides, Length *100*px, angle *90*deg, angle *360/3* deg for triangle.
# t2 = Tank(4,3,50,90,-360/3, "red", "black") # same tank halfed the size sizeL
# t3 = Tank(4,3,150,90,-360/3, "purple", "yellow") # same tank increased sizeL by 50%. 
# t4 = Tank(4,3,75,90,-360/3, "orange", "brown") # same tank 75% of t1 sizeL.



def DrawTank1():
    forward = True
    pos = 0
    movespeed=.8
    tur.setheading(0)
    tur.penup()                 # initialize position and variables
    tur.goto(-250, 0)
    tur.pendown()
    while True:
        
        tur.clear()
        for side in range(t1.squareRange):   #draw a square
            tur.color(t1.sqC)
            tur.forward(t1.sizeL)
            tur.left(t1.rightAngle)

        for side in range(t1.triangleRange):   #draw a Triangle in the square (turret points forward)
            tur.color(t1.triC)           
            tur.forward(t1.sizeL) 
            tur.right(t1.triA)  #360 deg /3 gives equal angular triangle.



        if forward:             # bounce back and forth on the screen
            pos+=movespeed
            if pos >= 400:
                forward = False
            tur.forward(movespeed)
        else:
            pos-=movespeed
            if pos <= 0:
                forward = True
                return False
            tur.forward(-movespeed)
        screen.update()


def DrawTank0():
    forward = True
    pos = 0
    movespeed=.2
    tur.setheading(90)
    tur.penup()                 # initialize position and variables
    tur.goto(-250, 0)
    tur.pendown()
    while True:
        
        tur.clear()
        for side in range(t2.squareRange):   #draw a square
            tur.color(t2.sqC)
            tur.forward(t2.sizeL)
            tur.left(t2.rightAngle)

        for side in range(t2.triangleRange):   #draw a Triangle in the square (turret points forward)
            tur.color(t2.triC)           
            tur.forward(t2.sizeL) 
            tur.right(t2.triA)  #360 deg /3 gives equal angular triangle.



        if forward:             # bounce back and forth on the screen
            pos+=movespeed
            if pos >= 400:
                forward = False
            tur.forward(movespeed)
        else:
            pos-=movespeed
            if pos <= 0:
                forward = True
                return False
            tur.forward(-movespeed)
        screen.update()
def DrawTank2():
    forward = True
    pos = 0
    movespeed=.5
    tur.setheading(270)
    tur.penup()                 # initialize position and variables
    tur.goto(400, 0)
    tur.pendown()
    while True:
        
        tur.clear()
        for side in range(t3.squareRange):   #draw a square
            tur.color(t3.sqC)
            tur.forward(t3.sizeL)
            tur.left(t3.rightAngle)

        for side in range(t3.triangleRange):   #draw a Triangle in the square (turret points forward)
            tur.color(t3.triC)           
            tur.forward(t3.sizeL) 
            tur.right(t3.triA)  #360 deg /3 gives equal angular triangle.



        if forward:             # bounce back and forth on the screen
            pos+=movespeed
            if pos >= 400:
                forward = False
            tur.forward(movespeed)
        else:
            pos-=movespeed
            if pos <= 0:
                forward = True
                return False
            tur.forward(-movespeed)
        screen.update()
                   
 
while True :                 #game loop
    
    #so drawing and moving all the tanks at the same time has been a daunting task... BUT I can draw them sequentially and make them move, face different directions, have different velocities, etc.
    # By my reading of the directions this is technically correct. The best kind of correct. 
    #It's the Fog of War? Your low-tech situational-awareness tools only allow to track one at a time. Yeah! 

    DrawTank0() #draws and moves tanks 0
    DrawTank1() #Draws and moves tank 1
    DrawTank2() #Draws and moves tank 2. 
    
 
    