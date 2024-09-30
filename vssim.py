import turtle as trtl
import random

# =====================
# Make & Move "people" By: Angad Chhibber
#======================
screenwidth = 600
screenheight = 600


population = list() # lists that hold the different kinds of people
infected = list()
immune = list()


def infect(person):
  person.shape("turtle")
  person.color("red")
  infected.append(person)


def make_immune(person):
  person.color("green")
  person.shape("square")
  person.setheading(0)
  immune.append(person)


def check_infected(person):# 
  for i in infected:
    if person.distance(i) <= infection_rate: # If a certain person (argument) is close to any person that is infected, they will be infected
      infect(person)
      break


def move_population():
  count = 0
  while(True):
    for person in population:
      person.right(random.randint(-30,30))
      person.forward(random.randint(-30,30))
      x,y = person.pos()
      if x < -screenwidth/2 or x > screenwidth/2 or y < 0 or y > screenheight/2:# Making the border
        person.undo()
      if person not in infected and person not in immune:
        check_infected(person)
      count += 1
      if len(infected) == 48:
        return count
def make_population(hop, healthy_color): # This algorithm makes all of the turtle objects hop(parameter) is the distance the turtles are from eachother. and healthy_color is the color of the healthy people
  infected = random.randint(10,40)
  immune1 = random.randint(infected+1,49)
  immune2 = random.randint(0,infected-1)


  for x in range(-5*hop,5*hop,hop): # -200  200
    for y in range(90,90+5*(hop),hop): # 90  290
      person = trtl.Turtle()
      person.speed(0)
      person.penup()
      person.shapesize(1)


      if (infected == 0):
        infect(person)
      elif (immune1 == 0) or (immune2 == 0):
        make_immune(person) # An algorithm that includes sequencing, selection, and iteration that is in the body of make_population()
      else:
        person.shape("circle")
        person.color(healthy_color)


      person.setpos(x,y)
      population.append(person)
      infected -= 1
      immune1 -= 1
      immune2 -= 1


# Main Program
low_irate = 20
high_irate = 80
healthy_color = "blue"
print("What do you want the infection rate to be? ", end="")
print("(please have numbers be between {} and {})".format(low_irate, high_irate))
infection_rate = int(input()) # User input of infection rate
if (infection_rate < low_irate) or (infection_rate > high_irate):
  print("Wrong Value. Please try again.")
  exit()
# ===================
# Make Hosptial By: Brighton Alcantara
#====================


htrtl = trtl.Turtle() # Create a turtle that makes the hospital
htrtl.hideturtle()
htrtl.speed(0)


# Create hospital building
htrtl.fillcolor("brown")
htrtl.begin_fill()
htrtl.penup()
htrtl.goto(-250, -50)
htrtl.pendown()
for count in range(2):
  htrtl.forward(500)
  htrtl.right(90)
  htrtl.forward(200)
  htrtl.right(90)
htrtl.end_fill()


# Create Red Cross
htrtl.penup()
htrtl.goto(10, -135)
htrtl.pendown()
htrtl.pensize(3)
htrtl.fillcolor("red")
htrtl.begin_fill()
for count in range(4):
  htrtl.forward(50)
  htrtl.right(90)
  htrtl.forward(30)
  htrtl.right(90)
  htrtl.forward(50)
  htrtl.left(90)
htrtl.end_fill()


# Create helipad
htrtl.pencolor("yellow")
htrtl.penup()
htrtl.goto(175, -135)
htrtl.pendown()
htrtl.forward(30)
htrtl.backward(15)
htrtl.setheading(0)
htrtl.forward(15)
htrtl.setheading(270)
htrtl.backward(15)
htrtl.forward(30)


# ===================
# Move Infected People to Hospital By: Brighton Alcantara
# ===================


def infected_goto_hospital():
  for person in infected:
    person.speed(10)
    person.goto(-8, -70) # Every person moves into hospital
    #person.hideturtle()


# ===================
# Move Now Immune People Back By: Angad Chhibber
# ===================


def immune_come_back():
  index = len(population)-1
  for x in range(-5*40,5*40,40): # -200  200
    for y in range(90,90+5*(40),40): # 90  290
      make_immune(population[index])
      population[index].showturtle()
      population[index].goto(x,y)
      index -= 1
      if (index < 0):
        return


# ===================
# Make divider line By: Angad Chhibber
# ===================


def line():
  line = trtl.Turtle()
  line.penup()
  line.goto(-300 ,0)
  line.pendown()
  line.width(6)
  line.forward(700)


# ===================
# Turning the Clock By: Brighton Alcantara
# ===================


def clock_turn():
  minheading = 90 # Setheading that clock turtle will face drawing minute hand
  hourheading = 90 # Setheading that clock turtle will face drawing hour hand


  clock = trtl.Turtle()
  clock.hideturtle()
  clock.speed(10)
  clock.pensize(2)
  clock.penup()
  clock.goto(-180, -175)
  clock.pendown()
  clock.circle(50)
  clock.penup()
  clock.goto(-180, -125)
  clock.pendown()
  count = None
  for count in range(15): # 15 turns
    # Draw both hands (first draw minute hand then hour hand)
    clock.setheading(minheading)
    clock.forward(40) # Minute hand
    clock.backward(40)
    clock.setheading(hourheading)
    clock.forward(25)
    clock.backward(25)
    # Erase the hands (first erase hour hand then minute hand)
    clock.pencolor("brown")
    clock.forward(25)
    clock.backward(25)
    clock.setheading(minheading)
    clock.forward(40)
    clock.backward(40)


    # Configure clock turtle heading & color
    clock.pencolor("black")
    minheading -= 24 # Turn minute hand clockwise
    hourheading -= 2 # Turn hour hand clockwise
    count += 0


# Erase clock
  clock.seth(90)
  clock.pencolor("brown")
  clock.penup()
  clock.goto(-230, -176)
  clock.pendown()
  clock.fillcolor("brown")
  clock.begin_fill()
  clock.forward(100)
  clock.right(90)
  clock.forward(100)
  clock.right(90)
  clock.forward(100)
  clock.left(90)
  clock.end_fill()


#=====================
# make syringe: By: Angad Chhibber
#======================


def syringe():
  from turtle import Screen, Turtle
  screen = Screen()
  syringe = []
  x = 200
  y = -200


  screen.tracer(False)


  part = Turtle()
  part.penup()
  part.shape("classic")
  part.setpos(x,y)
  part.setheading(180)
  part.shapesize(1,20,1)
  syringe.append(part)


  for x in range(280,320,20):
          part = Turtle()
          part.penup()
          part.shape("square")
          part.color("green")
          part.setpos(x,y)
          syringe.append(part)

  for x in range(320,380,20):
          part = Turtle()
          part.penup()
          part.shape("square")
          part.setpos(x,y)
          syringe.append(part)


  x += 20
  part = Turtle()
  part.penup()
  part.shape("arrow")
  part.setheading(180)
  part.setpos(x,y)
  syringe.append(part)


  steps = 100
  while steps >= 0:
      for i in syringe:
          x,y = i.position()
          i.setpos(x-2, y+1.3)
      screen.update()
      steps -= 1

  screen.tracer(True)

# ===================
# Person Function Calls
# ===================

#line()
screen = trtl.Screen()
screen.setup(screenheight,screenwidth)
screen.listen()
screen.tracer(False)

make_population(40, healthy_color) # takes the distance each turtle will be from one another and the color of the healthy population as parameters.

screen.tracer(True)

moves = move_population()
infected_goto_hospital()

syringe()

clock_turn()
# Vaccine animation placed here
immune_come_back()
print("+-----------------------------------------------------+")
print("| It took " + str(moves) + " moves for the whole population to be infected.|")
print("+-----------------------------------------------------+")


screen.exitonclick()

