#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
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
        self.window = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

    def process_events(self, ):
        pass

    def update(self, ):
        pass

    def render(self, ):
        pass

