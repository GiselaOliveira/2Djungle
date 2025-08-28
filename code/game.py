#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


from code.menu import Menu

class Game:
    def __init__(self):
        self.screen = None
        self.timer = None
        self.running = None
        self.player = None
        self.enimies = None
        self.plataform = None
        self.projectiles = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # Check for all events
            #  for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()  # Close Window
             #       quit()  # end pygame

    def process_events(self, ):
        pass

    def update(self, ):
        pass

    def render(self, ):
        pass

