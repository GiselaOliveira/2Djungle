#!/usr/bin/python
# -*- coding: utf-8 -*-

from projectile import Projectile


class Player(Projectile):
    def __init__(self):
        self.life = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.speed = None
        self.on_ground = None

    def jump(self, ):
        pass

    def move_left(self, ):
        pass

    def move_right(self, ):
        pass

    def shoot(self, ):
        pass

    def update(self, ):
        pass
