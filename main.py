# L. Louque
# 1/13/2023
# mikeWazowski

import turtle

t = turtle.Turtle()

def drawHorns():
    #left
    t.up()
    t.begin_fill()
    t.setpos(-40, 90)
    t.down()
    t.color("gray")
    t.setpos(-70, 110)
    t.setpos(-80, 60)
    t.end_fill()
    #right
    t.up()
    t.begin_fill()
    t.setpos(40, 90)
    t.down()
    t.color("gray")
    t.setpos(70, 110)
    t.setpos(80, 60)
    t.end_fill()


def drawHead():
    t.up()
    t.begin_fill()
    t.setpos(0, -100)
    t.down()
    t.color("limeGreen")
    t.circle(100)
    t.end_fill()


def drawMouth():
    #right
    t.up()
    t.begin_fill()
    t.setpos(0, -80)
    t.down()
    t.color("green")
    t.circle(80, 60)
    t.setpos(0, -40)
    t.end_fill()
    #left
    t.up()
    t.begin_fill()
    t.setpos(0, -80)
    t.seth(180)
    t.down()
    t.color("green")
    t.circle(-80, 60)
    t.setpos(0, -40)
    t.end_fill()


def tooth():
  t.seth(0)
  for x in range(0,3):
    t.forward(15)
    t.right(120)
  t.up()
  t.forward(20)
  t.down()
def drawTeeth():
  t.up()
  t.begin_fill()
  t.setpos(-57.5, -40)
  t.down()
  t.color("white")
  for x in range(0,6):
    tooth()
  t.end_fill()


def drawEyes():
  #whites
  t.up()
  t.begin_fill()
  t.seth(0)
  t.setpos(0, -22)
  t.down()
  t.color("white")
  t.circle(50)
  t.end_fill()
  #iris
  t.up()
  t.begin_fill()
  t.seth(0)
  t.setpos(0, -9)
  t.down()
  t.color("darkCyan")
  t.circle(35)
  t.end_fill()
  #pupil
  t.up()
  t.begin_fill()
  t.seth(0)
  t.setpos(0, 5)
  t.down()
  t.color("black")
  t.circle(20)
  t.end_fill()
  #sparkle
  t.up()
  t.begin_fill()
  t.seth(0)
  t.setpos(-17, 28)
  t.down()
  t.color("white")
  t.circle(7)
  t.end_fill()

  

t.ht()
drawHorns()
drawHead()
drawMouth()
drawTeeth()
drawEyes()
# drawHat()