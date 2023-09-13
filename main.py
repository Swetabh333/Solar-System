import pygame



pygame.init()




class Planet:
    G = 6.67428e-11
    AU = 1.496e8
    def __init__(self,mass,radius):
        self.mass = mass
        self.radius = radius

        
