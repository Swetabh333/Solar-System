import pygame
import numpy as np
import math

class Planet:
    G = 6.67e-11  # kgm**3/s**2
    AU = 1.496e11  #meters
    SCALE = 220 / AU
    TIMESPAN = 60*60*12

    def __init__(self,x,y,mass,radius,color):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.color = color
        self.vel_x = self.vel_y = 0

    def draw(self,screen,height,width):
        x = ( self.x * self.SCALE ) + height/2 
        y = ( self.y * self.SCALE ) + width/2
        pygame.draw.circle(screen,self.color,(x,y),self.radius)

    def gravity(self,planet):
        distance_x = planet.x - self.x
        distance_y = planet.y -self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        F = self.G * planet.mass * self.mass / distance **2

        angle = math.atan2(distance_y,distance_x)

        F_x = math.cos(angle) * F
        F_y = math.sin(angle) * F

        return F_x,F_y
    
    def new_positions(self,planet_array):
        total_fx , total_fy = 0 , 0
        for planet in planet_array:
            if self == planet :
                continue
            fx , fy = self.gravity(planet)
            total_fx += fx
            total_fy += fy
        
        self.vel_x += total_fx / self.mass * self.TIMESPAN
        self.vel_y += total_fy /self.mass * self.TIMESPAN

        self.x += self.vel_x * self.TIMESPAN
        self.y += self.vel_y * self.TIMESPAN
        
        


pygame.init()
screen = pygame.display.set_mode((1920,945),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

planet_array = []

Sun = Planet(0,0,1.9891e30,40,'yellow')
planet_array.append(Sun)
Earth = Planet(-1*Planet.AU,0,5.9742e24,25,'blue')
Earth.vel_y = 29.783e3
planet_array.append(Earth)
Mars = Planet(-1.52*Planet.AU,0,6.39e23,17,'red')
Mars.vel_y = 24.08e3
planet_array.append(Mars)
Venus = Planet(0.72*Planet.AU,0,4.867e24,22,'orange')
Venus.vel_y = -35.02e3
planet_array.append(Venus)
Mercury = Planet(0.39*Planet.AU,0,3.30104e23,14,'grey')
Mercury.vel_y = -47.90e3
planet_array.append(Mercury)
Jupiter = Planet(5.2*Planet.AU,0,1.898e27,30,'brown')
Jupiter.vel_y = -13.06e3
planet_array.append(Jupiter)



height,width=pygame.display.get_window_size()

while running:
    clock.tick(60)
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for planet in planet_array:
        planet.new_positions(planet_array)
        planet.draw(screen,height,width)

    pygame.display.update()


pygame.quit()