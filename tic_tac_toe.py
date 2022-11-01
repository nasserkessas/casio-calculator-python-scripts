from casioplot import *
from random import *
from math import *

squares = []
def init():
  for y in range(1,4):
    for x in range(1,4):
      squares.append({"x":x,"y":y,"contents":""})

def get_input():
  i = input("Enter coords ")
  x = i[0]
  y = i[2]
  for s in squares:
    if s["x"] == int(x) and s["y"] == int(y) and s["contents"] == "":
      s["contents"] = "cross"

def cmp_turn():
  empty = []
  for s in squares:
    if s["contents"] == "":
      empty.append(s)
  a = choice(empty)
  a["contents"] = "circle"

def draw_cross(x,y):
  for a in range(50):  
    set_pixel(117+(x-1)*50+(50-a),20+(y-1)*50+a)
    set_pixel(117+(x-1)*50+(a),20+(y-1)*50+a)

def draw_circle(x,y):
  for i in range(1,360):
    set_pixel(floor(117+cos(i)*25+25*(2*x-1)),floor(20+sin(i)*25+25*(2*y-1)))
    
def draw():
  for s in squares:
    if s["contents"] == "cross":
      draw_cross(s["x"],s["y"])
    elif s["contents"] == "circle":
      draw_circle(s["x"],s["y"])
  for i in range(150):
    if i == 0 or i == 149:
      for a in range(150):
        set_pixel(117+a,20+i)     
    else:
      set_pixel(117+0,20+i)
      set_pixel(117+150,20+i)
    show_screen()

def delay(x):
  for i in range(x):
    continue

def check_game_over():
  s = squares
  if s[0]["contents"] == s[4]["contents"] == s[8]["contents"] == "cross" or s[2]["contents"] == s[4]["contents"] == s[6]["contents"] == "cross":
    clear_screen()
    draw_string(150,75,"You Win")
    return True
  if s[0]["contents"] == s[4]["contents"] == s[8]["contents"] == "circle" or s[2]["contents"] == s[4]["contents"] == s[6]["contents"] == "circle":
    clear_screen()
    draw_string(150,75,"You Lose")
    return True
  for i in range(0,3):
    if s[3*i]["contents"] == s[3*i+1]["contents"] == s[3*i+2]["contents"] == "cross":
      clear_screen()
      draw_string(150,75,"You Win")
      return True
    if s[3*i]["contents"] == s[3*i+1]["contents"] == s[3*i+2]["contents"] == "circle":
      clear_screen()
      draw_string(150,75,"You Lose")
      return True
    if s[0+i]["contents"] == s[3+i]["contents"] == s[6+i]["contents"] == "cross":
      clear_screen()
      draw_string(150,75,"You Win")
      return True    
    if s[0+i]["contents"] == s[3+i]["contents"] == s[6+i]["contents"] == "circle":
      clear_screen()
      draw_string(150,75,"You Lose")
      return True
  return False    

init()
while True:
  cmp_turn()
  draw()
  delay(100000)
  if check_game_over() == True:
    break  
  get_input()
  draw()
  delay(100000)
  if check_game_over() == True:
    break