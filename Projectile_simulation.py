from visual import *
from math import sin, cos

initialHeight = 20
limit=0
initialVelocity = 20
Angle = 45



#Set up display window
scene1  = display(title = "Projectile",x=0,y=0,width=800,height=600,range=30, background=color.white, center=(7,initialHeight,0))

#create our objects:
#table = box(pos=(-1,initialHeight-(initialHeight/2), 0),size=(5,initialHeight,4))
#table = box(pos=(0,initialHeight-0.5, 0),size=(5,1,4))

ball = sphere(pos=(0,initialHeight,0),radius=1,make_trail=True, material=materials.marble)
floor = box(pos=(0,0,0),size=(200,0.25,50))

#sun = sphere(pos=(-10,60,0),radius=5,color=color.yellow, material=materials.emissive)
#lamp = local_light(pos=(0,0,0), color=color.yellow)

if initialHeight!=0:
	rod1 = cylinder(pos=(-4,0 , 0), axis=(0,initialHeight+(initialHeight/5),0), radius=3)
	top1 = sphere(pos=(-4,initialHeight+(initialHeight/5)-0.01, 0), radius=rod1.radius)
	rod2 = cylinder(pos=(-4,top1.y+top1.radius-0.5 , 0), axis=(0,initialHeight/9,0), radius=top1.radius/10)
	top2 = cone(pos=(-4,rod2.y+rod2.axis.y,0), axis=(0,rod2.y/6,0), radius=rod2.radius)
	#table = box(pos=(-2,initialHeight-ball.radius, 0),size=(5,rod1.radius/6,2.3))
	#hole1 = ring(pos=(-4,initialHeight-ball.radius, 0),  axis=(0,1,0), radius=3, thickness=0.1)
	hole1 = ring(pos=(-4,initialHeight-ball.radius, 0),  axis=(0,1,0), radius=rod1.radius+2, thickness=0.1)
	hole2 = ring(pos=(-4,initialHeight+ball.radius/2, 0),  axis=(0,1,0), radius=rod1.radius+2, thickness=0.1)
	table = box(pos=(-2,initialHeight-ball.radius, 0),size=(hole1.radius+1.2,rod1.radius/6,2.3))

	stair1 = cylinder(pos=(-4,0 , 0), axis=(0,initialHeight/7,0), radius=rod1.radius+rod1.radius*0.5)
	stair2 = cylinder(pos=(-4,0 , 0), axis=(0,initialHeight/9,0), radius=rod1.radius+rod1.radius*1)
	stair3 = cylinder(pos=(-4,0 , 0), axis=(0,initialHeight/11,0), radius=rod1.radius+rod1.radius*1.5)
	stair4 = cylinder(pos=(-4,0 , 0), axis=(0,initialHeight/13,0), radius=rod1.radius+rod1.radius*2.5)
	stair5 = cylinder(pos=(-4,0 , 0), axis=(0,initialHeight/15,0), radius=rod1.radius+rod1.radius*3)

	hole3 = ring(pos=(-4,initialHeight-initialHeight/4, 0),  axis=(0,1,0), radius=rod1.radius+0.01, thickness=0.1)
	hole4 = ring(pos=(-4,initialHeight-initialHeight/2, 0),  axis=(0,1,0), radius=rod1.radius+0.01, thickness=0.1)
	hole5 = ring(pos=(-4,initialHeight+initialHeight/6.3, 0),  axis=(0,1,0), radius=rod1.radius+0.1, thickness=0.1)
	limit=1
	


t = 0
dt = 0.0001
g = -32 #m/s**2

Vx=initialVelocity*cos(Angle*pi/180)
Vy=initialVelocity*sin(Angle*pi/180)

#print Vx,"\n",Vy
UpForce=Vy
DownForce=g*t


#Fgrav = vector(0,g*dt,0)
Fgrav = vector(0,g*t,0)		#Force Due to gravity
ball_velocity = vector(Vx,Vy,0)


#Arrow Lengths ############################################################################################
arrow_constant=0.25
vertical_arrow_length = (Vy+Fgrav.y)*arrow_constant
horizontal_arrow_length=(Vx+Fgrav.x)*arrow_constant
vertical_arrow = arrow(pos=(ball.x,ball.y,0), axis=(0,vertical_arrow_length,0), shaftwidth=0.1)
horizontal_arrow = arrow(pos=(ball.x,ball.y,0), axis=(horizontal_arrow_length,0,0), shaftwidth=0.1)
#############################################################################################################

vertical_arrow_length = (Vy+Fgrav.y)*arrow_constant
minimal_arrow_length = vertical_arrow_length




while True:
#for i in range(3):
	ball.make_trail=True
	rate(10000*3)
	vertical_arrow.pos=(ball.x,ball.y,0)
	horizontal_arrow.pos=(ball.x,ball.y,0)

	vertical_arrow_length = (Vy+Fgrav.y)*arrow_constant
	vertical_arrow.axis=(0,vertical_arrow_length,0)

	if abs(vertical_arrow_length)<=minimal_arrow_length:
		minimal_arrow_length=vertical_arrow_length
		max_vertical_height=ball.y
	
	Fgrav=Fgrav+(0,g*dt,0)
	ballv=ball_velocity+Fgrav
	ball.pos += ballv*dt
	
	if ball.y<limit: #when ball hits the ground
		#t+=dt
		print "ball.pos = ", ball.pos, "t = ",t
		#print "ball2.pos = ", ball2.pos
		label(pos=(ball.x+horizontal_arrow_length+6,ball.y+1,0), text="Vx= %1.5f"% ballv.x, border=6)
		label(pos=(ball.x,ball.y+vertical_arrow_length-2,0), text="Vy= %1.5f"% ballv.y, border=6)
		label(pos=(-16,30,0), text="Range= %1.5f"% ball.x, border=6)
		label(pos=(-15,25,0), text="Time Taken= %1.5f"% t, border=6)
		label(pos=(-12,20,0), text="Max Height Reached= %1.5f"% max_vertical_height, border=6)
		print max_vertical_height
		break

	t += dt

exit()


