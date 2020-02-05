import turtle, platform, math

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

# cents
#==========================================
# Purpose: To determine the total amount of cents.
#   
# Input Parameter(s):
#   quarters - equates to 25 cents
#   dimes - equates to 10 cents
#   nickles - equates to 5 cents
#   pennies - equates to 1 cent
#   
# Return Value: the total amount of cents
#   
#==========================================

def cents(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters*25
    total += dimes*10
    total += nickels*5
    total += pennies
    return total

# draw_M
#==========================================
# Purpose: to draw the University of Minnesota M logo 
#   
# Input Parameter(s): turtle values
#   
# Return Value:
#   none
#==========================================

def draw_M():
    turtle.delay(0)
    turtle.bgcolor("gold")
    turtle.hideturtle()
    turtle.color("maroon")
    turtle.penup()
    turtle.setpos(-200,-100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(14)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(128)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(14)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(28)
    turtle.right(60)
    turtle.forward(140)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(140)
    turtle.right(60)
    turtle.forward(28)
    turtle.left(90)
    turtle.forward(64)
    turtle.end_fill()

# Part B: star8
#==========================================
# Purpose: To uses turtle to draw a star with eight points
#   
# Input Parameter(s): turtle functions - forward and left
#   
# Return Value: none
#   
#==========================================

def star8(): #using a for loop with 8 repetitions to make the star
    for x in range(8):
        turtle.forward(200) #determines side legth of star
        turtle.left(135) #determines angle for which cursor must move


# Part C: trajectory
#==========================================
# Purpose: To determine the trajectory of the thrown ball
#   
# Input Parameter(s):
#   height - initial height at which the ball is thrown
#   speed -  initial speed at which the ball is thrown, in meters/second                   
#   angle - the angle at which the ball is thrown relative to the horizontal ground plane, in degrees
#
# Return Value:
#   Flight distance of the ball
#   
#==========================================

def trajectory(height, speed, angle):
    initial_horizontal_speed = round(speed * (math.cos(math.radians(angle))), 3) #determine the Horizontal Speed of the ball
    initial_verticle_speed = round(speed * (math.sin(math.radians(angle))), 3) #determine the Verticle Speed of the ball
    math_1 = (initial_verticle_speed**2) + 19.6*(height) #math step 1 for determining flight time
    math_2 = math.sqrt(math_1) #math step 2 for determining flight time
    flight_time = round((math_2 + initial_verticle_speed) / 9.8, 3) #determining the flight time of the ball 
    flight_distance = round(initial_horizontal_speed * flight_time, 3) #determining the flight distance of the ball 
    print("Horizontal Speed: ", initial_horizontal_speed, "m/s")
    print("Verticle Speed: ", initial_verticle_speed, "m/s")
    print("Flight Time: ", flight_time, "s")
    print(flight_distance)

