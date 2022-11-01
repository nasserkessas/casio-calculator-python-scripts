from casioplot import *
from math import *
from random import *

dim_x=384
dim_y=192

r=7
g=-9.8
scale=12


def draw(x,y,loc,balls):
  clear_screen()
  
  #ground
  for i in range(1,dim_x):
    set_pixel(i,dim_y-3)
  
  #current ball
  for i in range(1,360,10):
    set_pixel(floor(cos((pi*i/180))*r+x),floor(sin(pi*i/180)*r+y))  

  #scale
  for i in range(1,dim_x,scale):
    set_pixel(i,dim_y-1)
    set_pixel(i,dim_y-2)
  for i in range(1,dim_y,scale):
    set_pixel(0,i)
    set_pixel(1,i)

  #target
  for i in range(0,scale):
    set_pixel(loc+i,dim_y-2)
    set_pixel(loc+i,dim_y-4)
  
  #previous balls
  for ball in balls:
    for i in range(1,360,10):
      set_pixel(floor(cos((pi*i/180))*r+ball[0]),floor(sin(pi*i/180)*r+ball[1]))

  #mass/angle
  if stg >= 3:
    draw_string(dim_x-150,10,str(angle)+" '")
  if stg >= 2:
    draw_string(dim_x-75,10,str(mass)+" Kg")

  show_screen()

def make_target():
  loc=randint(50,dim_x-20)
  return loc

def delay(x):
  for i in range(x):
    continue
    
def update_pos(sx,sy,x,y):
  sx=ux*t
  sy=1/2*g*(t**2)+uy*t
  x=scale*sx+r
  y=dim_y-r-3-scale*sy
  if up==False and sy <= 0:
    y=dim_y-r-2
  return [sx,sy,x,y]

def checkhit():
  if x+3>loc and x-3<loc+scale:
    return True
  return False

def get_input(stg,mass,angle,a):
  if a==1:
    print("\n\n\n    ---Stage "+str(stg)+"---\n    ---Round "+str(rnd)+"---\n")
  else:
    print("\n\n\n\n   ---Attempt "+str(a)+"---\n")
  if stg == 3:
    print(str(mass)+" Kg")
    print(str(angle)+" Degrees")
    energy=input("K Energy(J): ")
  elif stg == 2:
    print(str(mass)+" Kg")
    angle=input("Angle(Degrees): ") 
    energy=input("K Energy(J): ")
  else: 
    angle=input("Angle(Degrees): ")
    mass=input("Mass(Kg): ")
    energy=input("K Energy(J): ")
  return [mass,angle,energy]  
  
masses=[0.1,0.2,0.5,1,2,3,4,5,6,7,8,9,10]
stg=1
rnd=0
loc=0
up=True
angle=0
mass=0
energy=0
attempt=0

while True:
  if attempt>3:
      break
  rnd+=1
  if rnd>3 and stg<3:
    stg+=1
    rnd=1
  
  x=r
  y=dim_y-r-3
  attempt=1
  hit=False
  balls=[]
  loc=make_target()   
  if stg >= 2:
    mass=choice(masses)
  if stg >= 3:
    angle=randint(5,85)

  draw(x,y,loc,balls)
  delay(500000)

  while hit==False:
    if attempt>3:
      break
    sx=0
    sy=0
    x=r
    y=dim_y-r-3
    t=0
    up=True    
    
    [mass,angle,energy]=get_input(stg,mass,angle,attempt)
    ux=float((2*float(energy)/float(mass))**0.5)*cos(pi*int(angle)/180)
    uy=float((2*float(energy)/float(mass))**0.5)*sin(pi*int(angle)/180)

    attempt+=1
    
    while up==True or sy > 0:
      t+=0.05
      [sx,sy,x,y]=update_pos(sx,sy,x,y)
      draw(x,y,loc,balls)
      if sy>0:
        up=False
    
    delay(250000)
    hit=checkhit()
    if hit==False:
      balls.append([x,y])
    else:
      balls=[]
      attempt=0

clear_screen()      
print("\n\n\n#####################\n#     Game Over     #\n#####################\n")