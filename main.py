"""Game made by ReVoLuTioN119"""

# import libs
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
    screen = pygame.display.set_mode((controls.width, controls.height))
    if controls.fs:
        pygame.display.toggle_fullscreen()
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('Gold card')
    icon = pygame.image.load('images/icon.png').convert()
    bg = pygame.image.load('images/bg.jpg').convert()
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    font = pygame.font.Font('images/font.ttf', int(50 / controls.correction_mult))

    while True:
        # background image
        screen.blit(bg, (0, 0))

        # FPS
        if controls.show_FPS:
            fps = font.render(str(int(clock.get_fps())), False, (0, 0, 0))
            screen.blit(fps, (50, 0))

        # game code
        controls.deck_def(player, screen)
        controls.turn_button_def(screen)
        controls.battle(player.get_cards(), enemy.get_cards(), player, enemy)
        enemy.output(screen)
        player.output(screen)

        # checking player's actions
        controls.capture_keyboard()

        # updating pygame
        pygame.display.flip()
        clock.tick(60)
        controls.testing()


if __name__ == '__main__':
    main()

# нужны свои шрифты
