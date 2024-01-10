Web VPython 3.2


scene.autoscale = False
sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=5000,shininess=0)
scene.camera.pos= vector(2000,2000,0)
scene.camera.axis=vector(-2000,-2000,0)

scene.caption = """Kepler-62 system --> 62b(red), 62c(grey), 62d(orenge), 62e(grey), 62f(yellow)
Made by Mohammed Salama - Mohammed Ibrahim - Seif-Eldin Hatem"""

trial_radius=2

star= local_light(pos=vector(0,0,0),color=color.yellow,)

kepler = sphere(pos=vector(0,0,0), radius =140,texture="https://i.imgur.com/vy5teR7.png",opacity=1,)          #kepler 62 Star


Kb = sphere(pos=vector(270,0,0), radius=15, texture="https://i.imgur.com/O9bCHV3.png",shininess=0)    #Kepler 62-b planet
attach_trail(Kb,color=color.red,retain = 400, radius=trial_radius)
Kc= sphere(pos=vector( 400,0,0), radius=6, texture="https://i.imgur.com/w0O6Rhe.png",shininess=0)                       #Kepler 62-c planet
attach_trail(Kc,color=color.white,retain = 600, radius= trial_radius)
Kd= sphere(pos=vector(505,0,0), radius=30,texture="https://i.imgur.com/ljAvyiH.png",shininess=0)   #Kepler 62-d planet
attach_trail(Kd,color=color.orange,retain = 800, radius= trial_radius)
Ke = sphere(pos=vector(700, 0,0), radius= 28,texture="https://i.imgur.com/7TfVxOS.png",shininess=0)   #Kepler 62-e planet
attach_trail(Ke,color=color.white,retain = 1150, radius= trial_radius)
Kf = sphere(pos=vector(850, 0,0), radius=25,texture="https://gmonna.github.io/HereComesTheSun/img/earthsized.png",shininess=0)   #Kepler 62-f planet
attach_trail(Kf,color=color.yellow,retain = 1700, radius= trial_radius)

Kb.v = vector(0,0,6)
Kc.v = vector(0,0,5.7)
Kd.v = vector(0,0,5)
Ke.v = vector(0,0,4.2)
Kf.v = vector(0,0,3.9)


    

while(True):
    rate(100)
    
    
    
    dist2 =(Kb.pos.x**2 + Kb.pos.y**2 + Kb.pos.z**2)**0.5
    radialVector = (kepler.pos-Kb.pos)/dist2                             #For kepler 62-b planet
    Fgrav = 10000 *radialVector/dist2**2
    Kb.v += Fgrav                                                      # += is Add and Assign: Add right side operand with left side operand and then assign to left operand
    Kb.pos += Kb.v



    
    distance =(Kc.pos.x**2 + Kc.pos.y**2 + Kc.pos.z**2)**0.5               #For kepler 62-c planet
    radialVector2 = (kepler.pos-Kc.pos)/distance
    Fograv2 = 12000 *radialVector2/distance**2
    Kc.v += Fograv2
    Kc.pos += Kc.v
    
    
    
    
    
    distance = (Kd.pos.x**2 + Kd.pos.y**2 + Kd.pos.z**2)**0.5
    radialVector2 = (kepler.pos-Kd.pos)/distance                           #For kepler 62-d planet
    Fograv2 = 12000 *radialVector2/distance**2
    Kd.v += Fograv2
    Kd.pos += Kd.v
    
    
    
    
    
    
    distance = (Ke.pos.x**2 + Ke.pos.y**2 + Ke.pos.z**2)**0.5
    radialVector2 = (kepler.pos-Ke.pos)/distance                               #For kepler 62-e planet
    Fograv3 = 12000 *radialVector2/distance**2
    Ke.v += Fograv3
    Ke.pos += Ke.v
    
    
    
    distance = (Kf.pos.x**2 + Kf.pos.y**2 + Kf.pos.z**2)**0.5
    radialVector2 = (kepler.pos-Kf.pos)/distance                             #For kepler 62-f planet
    Fograv3 = 12000 *radialVector2/distance**2
    Kf.v += Fograv3
    Kf.pos += Kf.v
    
    
    
    
    
    
    
    
    
    if distance <= kepler.radius: break

    
