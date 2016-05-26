from visual import *
from math import sin, cos

initialHeight = 2
initialVelocity = 20
Angle = 45

#Set up display window
scene1  = display(title = "Projectile",x=0,y=0,width=800,height=600,range=10, background=color.white, center=(7,initialHeight,0))

#create our objects:
table = box(pos=(-1,initialHeight-0.5, 0),size=(5,1,4))
ball = sphere(pos=(0,initialHeight,0),radius=1,color=color.green,make_trail=True)
floor = box(pos=(0,0,0),size=(100,0.25,10))
#ball2 = sphere(pos=(0,initialHeight,0),radius=1,color=color.red, make_trail=True)


t = 0
dt = 0.0001
g = -32  #ft/s**2

Vx=initialVelocity*cos(Angle*pi/180)
Vy=initialVelocity*sin(Angle*pi/180)

#print Vx,"\n",Vy
UpForce=Vy
DownForce=g*t




Fgrav = vector(0,DownForce,0)		#Force Due to gravity
#Fgrav = vector(0,g*dt,0)

ball_velocity = vector(Vx,Vy,0)
#print Vy


#Arrow Lengths ############################################################################################
vertical_arrow_length=2
horizontal_arrow_length=2
vertical_arrow = arrow(pos=(ball.x,ball.y,0), axis=(0,vertical_arrow_length,0), shaftwidth=0.1)
horizontal_arrow = arrow(pos=(ball.x+ball.radius,ball.y,0), axis=(horizontal_arrow_length,0,0), shaftwidth=0.1)
#############################################################################################################



while True:
#for i in range(3):
	rate(3000)
	vertical_arrow.pos=(ball.x,ball.y,0)
	horizontal_arrow.pos=(ball.x+ball.radius,ball.y,0)

	vertical_arrow_length = (Vy+Fgrav.y)*0.3
	vertical_arrow.axis=(0,vertical_arrow_length,0)

	Fgrav=Fgrav+(0,g*dt,0)
	#print Fgrav
	#ball1_velocity=ball1_velocity+Fgrav
	#ball1.pos += ball1_velocity*dt
	ballv=ball_velocity+Fgrav
	ball.pos += ballv*dt
	
	#ball2.pos = (Vx*t,initialHeight+Vy*t+0.5*g*t**2)

	
	if ball.y<1: #when ball hits the ground
		#t+=dt
		print "ball.pos = ", ball.pos, "t = ",t
		#print "ball2.pos = ", ball2.pos
		break

	t += dt


