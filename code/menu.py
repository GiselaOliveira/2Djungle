#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, MENU_COLOR, OUTLINE_COLOR, OUTLINE_SIZE, WHITE_COLOR


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/background/background 1/background 1.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/sonmenu.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            # Título principal
            self.menu_text(50, "Welcome", MENU_COLOR, (WIN_WIDTH / 2, 70), OUTLINE_COLOR, OUTLINE_SIZE)
            self.menu_text(50, "2D Jungle", MENU_COLOR, (WIN_WIDTH / 2, 120), OUTLINE_COLOR, OUTLINE_SIZE)

            # Menu
            self.menu_text(30, "INICIAR JOGO", WHITE_COLOR, (WIN_WIDTH / 2, 200), OUTLINE_COLOR, OUTLINE_SIZE)
            self.menu_text(30, "SCORE", WHITE_COLOR, (WIN_WIDTH / 2, 250), OUTLINE_COLOR, OUTLINE_SIZE)
            self.menu_text(30, "SAIR", WHITE_COLOR, (WIN_WIDTH / 2, 300), OUTLINE_COLOR, OUTLINE_SIZE)

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple,
                  outline_color: tuple = None, outline_size: int = 0):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        x, y = text_center_pos

        # Desenhar primeiro o contorno
        if outline_color and outline_size > 0:
            # Desenha o contorno em todas as direções ao redor
            for dx in range(-outline_size, outline_size + 1):
                for dy in range(-outline_size, outline_size + 1):
                    if dx != 0 or dy != 0:  # Não desenha na posição central
                        outline_surf: Surface = text_font.render(text, True, outline_color).convert_alpha()
                        outline_rect: Rect = outline_surf.get_rect(center=(x + dx, y + dy))
                        self.window.blit(source=outline_surf, dest=outline_rect)

        # Desenhar o texto principal por cima
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
