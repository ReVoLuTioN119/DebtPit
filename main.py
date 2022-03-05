"""Game made by ReVoLuTioN119"""

# import libs
import pygame

# import stuff from files
import cards
import controls_and_game_defs as controls
from fields import player_fields, enemy_fields
from player import Player
from enemy import Enemy

# init stuff
pygame.init()
player = Player(cards.player_hands, player_fields)
enemy = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck)


def main():
    # screens
    battle_screen = pygame.display.set_mode((controls.width, controls.height))
    menu_screen = pygame.display.set_mode((controls.width, controls.height))
    story_screen = pygame.display.set_mode((controls.width, controls.height))

    # configure pygame
    if controls.fs:
        pygame.display.toggle_fullscreen()
    pygame.display.set_caption('Gold card')
    icon = pygame.image.load('images/icon.png').convert()
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    font = pygame.font.Font('images/font.ttf', int(50 / controls.correction_mult))

    while True:

        # battle
        if controls.episode == 'battle':
            controls.battle_scene(battle_screen, player, enemy)

        # menu
        elif controls.episode == 'menu':
            '''Menu'''
            controls.main_menu_scene(menu_screen, font)

        # story
        elif controls.episode == 'story':
            controls.story_scene(story_screen, font)
            now = pygame.time.get_ticks()
            if now - controls.pressed_timer >= 5000:
                controls.episode = 'battle'

        # FPS
        if controls.show_FPS:
            fps = font.render(str(int(clock.get_fps())), False, (0, 0, 0))
            battle_screen.blit(fps, (50, 0))

        # updating pygame
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
