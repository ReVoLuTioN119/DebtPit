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
enemy1 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Frunk Cosello', controls.boss_image, 'description')
companion1 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Thomas Dyson', controls.enemy_image, 'description')
companion2 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Daniel Hancock', controls.enemy_image, 'description')
companion3 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Justine Baker', controls.enemy_image, 'description')
enemy2 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Jack Emerald', controls.boss_image, 'description')
companion4 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Adam Carter', controls.enemy_image, 'description')
companion5 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Gareth Babcock', controls.enemy_image, 'description')
companion6 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Lewis Clapton', controls.enemy_image, 'description')
enemy3 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'John Fotty', controls.boss_image, 'description')
companion7 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Zhess Campbell', controls.enemy_image, 'description')
companion8 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'James Flannagan', controls.enemy_image, 'description')
companion9 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Miguel Brooks', controls.enemy_image, 'description')
enemy4 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Frunk Simarta', controls.boss_image, 'description')
companion10 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'James Freeman', controls.enemy_image, 'description')
companion11 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Jeremiah Galbraith', controls.enemy_image, 'description')
companion12 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Cameron Jones', controls.enemy_image, 'description')
enemy5 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Harvard Capcone', controls.boss_image, 'description')
companion13 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Stephen Williams', controls.enemy_image, 'description')
companion14 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Charles Galbraith', controls.enemy_image, 'description')
companion15 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Robbie Campbell', controls.enemy_image, 'description')
boss = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Don Corneone', controls.boss_image, 'description')
companion16 = Enemy(cards.enemy_hands, enemy_fields, cards.enemy_deck, 'Consiglieri', controls.enemy_image, 'description')
bosses = [enemy1, enemy2, enemy3, enemy4, enemy5, boss]
enemies0 = [companion1, companion2, companion3, enemy1]
enemies1 = [companion4, companion5, companion6, enemy2]
enemies2 = [companion7, companion8, companion9, enemy3]
enemies3 = [companion10, companion11, companion12, enemy4]
enemies4 = [companion13, companion14, companion15, enemy5]
enemies5 = [companion16, boss]


def main():
    # screens
    battle_screen = pygame.display.set_mode((controls.width, controls.height))
    menu_screen = pygame.display.set_mode((controls.width, controls.height))
    story_screen = pygame.display.set_mode((controls.width, controls.height))
    choose_battle_screen = pygame.display.set_mode((controls.width, controls.height))

    # configure pygame
    if controls.fs:
        pygame.display.toggle_fullscreen()
    pygame.display.set_caption('DebtPit')
    icon = pygame.image.load('images/icon.png').convert()
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    font = pygame.font.Font('images/font.ttf', int(50 / controls.correction_mult))

    while True:

        # battle
        if controls.episode == 'battle':
            if controls.stopper_battle_num:
                controls.battle_num += 1
                controls.stopper_battle_num = False
            eval('controls.battle_scene(battle_screen, player, enemy' + str(controls.battle_num) + ')')

        # menu
        elif controls.episode == 'menu':
            controls.main_menu_scene(menu_screen, font)

        # story
        elif controls.episode == 'story':
            controls.story_scene(story_screen, font)
            close = pygame.time.get_ticks()
            if close - controls.pressed_timer >= 15000:
                controls.episode = 'choose_battle'

        # choose enemy
        elif controls.episode == 'choose_battle':
            eval('controls.choose_battle_scene(choose_battle_screen, font, bosses, enemies' + str(controls.battle_num) + ')')

        # FPS
        if controls.show_FPS:
            fps = font.render(str(int(clock.get_fps())), False, (0, 0, 0))
            battle_screen.blit(fps, (50, 0))

        # updating pygame
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
