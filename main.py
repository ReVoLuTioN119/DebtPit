"""Game made by ReVoLuTioN119"""

# import libs
import sys

import pygame

# import stuff from files
import cards
import controls_and_game_defs as controls
import fields
from player import Player
from enemy import Enemy

# init stuff
pygame.init()
player = Player(cards.player_hands, fields.player_fields)
enemy = Enemy(cards.enemy_hands, fields.enemy_fields, cards.enemy_deck)


def main():
    # configure pygame
    battle_screen = pygame.display.set_mode((controls.width, controls.height))
    main_menu = pygame.display.set_mode((controls.width, controls.height))
    if controls.fs:
        pygame.display.toggle_fullscreen()
    # pygame.mouse.set_visible(False)
    pygame.display.set_caption('Gold card')
    icon = pygame.image.load('images/icon.png').convert()
    bg_battle = pygame.image.load('images/bg.jpg').convert()
    bg_menu = pygame.image.load('images/menu.jpg').convert()
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    font = pygame.font.Font('images/font.ttf', int(50 / controls.correction_mult))

    while True:
        if controls.start_battle:
            '''Battle'''
            # background image
            battle_screen.blit(bg_battle, (0, 0))
            pygame.mouse.set_visible(False)

            # FPS
            if controls.show_FPS:
                fps = font.render(str(int(clock.get_fps())), False, (0, 0, 0))
                battle_screen.blit(fps, (50, 0))

            # game code
            controls.deck_def(player, battle_screen)
            controls.turn_button_def(battle_screen)
            enemy.output(battle_screen)
            player.output(battle_screen)
            controls.battle(player, enemy)

            # checking player's actions
            controls.capture_keyboard_battle()

        else:
            '''Menu'''
            pygame.mouse.set_visible(True)
            main_menu.blit(bg_menu, (0, 0))
            start_button = font.render('Start', False, (0, 0, 0))
            start_button_rect = start_button.get_rect(center=(controls.width / 2, controls.height / 2))
            main_menu.blit(start_button, start_button_rect)

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    sys.exit()
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_ESCAPE:
                        sys.exit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                        controls.start_battle = True

        # updating pygame
        pygame.display.flip()
        clock.tick(60)
        controls.testing()


if __name__ == '__main__':
    main()
