import pygame
import sys

import cards
import random

# screen params
screen_help = pygame.display.set_mode((0, 0), pygame.HIDDEN)
resolution = pygame.display.Info()
width = 1000  # resolution.current_w
height = 564  # resolution.current_h
correction_image = [1920 / width, 1080 / height]
correction_mult = (1920 + 1080) / (width + height)
fs = False
show_FPS = False

# images uploading
deck_full_raw = pygame.image.load('images/deck.png').convert()
deck_full = pygame.transform.scale(
    deck_full_raw, (deck_full_raw.get_width() / correction_image[0],
                    deck_full_raw.get_height() / correction_image[1]))
deck_full_point_raw = pygame.image.load('images/deck_point.png').convert()
deck_full_point = pygame.transform.scale(
    deck_full_point_raw,
    (deck_full_point_raw.get_width() / correction_image[0],
     deck_full_point_raw.get_height() / correction_image[1]))
deck_empty_raw = pygame.image.load('images/empty_deck.png').convert()
deck_empty = pygame.transform.scale(
    deck_empty_raw, (deck_full_raw.get_width() / correction_image[0],
                     deck_full_raw.get_height() / correction_image[1]))
field_image_raw = pygame.image.load('images/field.png').convert()
field_image = pygame.transform.scale(
    field_image_raw, (field_image_raw.get_width() / correction_image[0],
                      field_image_raw.get_height() / correction_image[1]))
card_image_raw = pygame.image.load('images/cardsback.png').convert()
card_image = pygame.transform.scale(
    card_image_raw, (card_image_raw.get_width() / correction_image[0],
                     card_image_raw.get_height() / correction_image[1]))
card_show_raw = pygame.image.load('images/cardsback_show.png').convert()
cardd_show = pygame.transform.scale(
    card_show_raw, (card_show_raw.get_width() / correction_image[0],
                    card_show_raw.get_height() / correction_image[1]))
card_correct_raw = pygame.Surface((20, 20), pygame.SRCALPHA,
                                  32).convert_alpha()
card_correct = pygame.transform.scale(
    card_correct_raw, (card_correct_raw.get_width() / correction_image[0],
                       card_correct_raw.get_height() / correction_image[1]))
turn_button_raw = pygame.image.load('images/turn_button.png').convert()
turn_button = pygame.transform.scale(
    turn_button_raw, (turn_button_raw.get_width() / correction_image[0],
                      turn_button_raw.get_height() / correction_image[1]))
turn_button_point_raw = pygame.image.load(
    'images/turn_button_point.png').convert()
turn_button_point = pygame.transform.scale(
    turn_button_point_raw,
    (turn_button_point_raw.get_width() / correction_image[0],
     turn_button_point_raw.get_height() / correction_image[1]))
arm_enemy_5_raw = pygame.image.load('images/arm/arm_5.png').convert_alpha()
arm_enemy_5 = pygame.transform.scale(
    arm_enemy_5_raw, ((arm_enemy_5_raw.get_width() / correction_image[0]),
                      (arm_enemy_5_raw.get_height() / correction_image[1])))
arm_enemy_4_raw = pygame.image.load('images/arm/arm_4.png').convert_alpha()
arm_enemy_4 = pygame.transform.scale(
    arm_enemy_4_raw, ((arm_enemy_4_raw.get_width() / correction_image[0]),
                      (arm_enemy_4_raw.get_height() / correction_image[1])))
arm_enemy_3_raw = pygame.image.load('images/arm/arm_3.png').convert_alpha()
arm_enemy_3 = pygame.transform.scale(
    arm_enemy_3_raw, ((arm_enemy_3_raw.get_width() / correction_image[0]),
                      (arm_enemy_3_raw.get_height() / correction_image[1])))
arm_enemy_2_raw = pygame.image.load('images/arm/arm_2.png').convert_alpha()
arm_enemy_2 = pygame.transform.scale(
    arm_enemy_2_raw, ((arm_enemy_2_raw.get_width() / correction_image[0]),
                      (arm_enemy_2_raw.get_height() / correction_image[1])))
arm_enemy_1_raw = pygame.image.load('images/arm/arm_1.png').convert_alpha()
arm_enemy_1 = pygame.transform.scale(
    arm_enemy_1_raw, ((arm_enemy_1_raw.get_width() / correction_image[0]),
                      (arm_enemy_1_raw.get_height() / correction_image[1])))
arm_enemy_0_raw = pygame.image.load('images/arm/arm_0.png').convert_alpha()
arm_enemy_0 = pygame.transform.scale(
    arm_enemy_0_raw, ((arm_enemy_0_raw.get_width() / correction_image[0]),
                      (arm_enemy_0_raw.get_height() / correction_image[1])))
arm_player_0 = pygame.transform.rotate(arm_enemy_0, 180)
arm_player_1 = pygame.transform.rotate(arm_enemy_1, 180)
arm_player_2 = pygame.transform.rotate(arm_enemy_2, 180)
arm_player_3 = pygame.transform.rotate(arm_enemy_3, 180)
arm_player_4 = pygame.transform.rotate(arm_enemy_4, 180)
arm_player_5 = pygame.transform.rotate(arm_enemy_5, 180)
bg_menu = pygame.image.load('images/menu.jpg').convert()
bg_battle = pygame.image.load('images/bg.jpg').convert()

# helpful args
episode = 'menu'  # what screen is now
take_card = False  # was the left mouse button pressed
card_show = False  # show card in hands on left click
card_action = False  # stopper when sth is in process with cards
hold_card = False  # holding card with cursor
release_hold = True  # release holding card with cursor
turn_push = False  # was the turn button pushed
turn_took = False  # was the card picked in that turn
output_not_enough_space = False  # print if no space for new cards
card_in_use = False  # remove correction card or not
turn_enemy = False  # is it enemy's turn now
turn_player = True  # is it player's turn now
can_turn = False  # stopper for the turn button
can_enemy_attack = False  # gives enemy attack if dead cards are black
can_player_attack = False  # gives player attack if he pushes turn button
output_text_before_taking = False  # show text when mouse on the turn button
stop_output_text_before_taking = False  # stop show text when mouse on the turn button
deck_image = deck_full
deck_image_empty = deck_empty
deck_image_rect = deck_image.get_rect(midright=(width - width / 100,
                                                height // 4))


def deck_def(player, screen):
    global take_card, deck_image, deck_image_rect, turn_took, can_turn, output_not_enough_space, \
        stop_output_text_before_taking, output_text_before_taking
    if len(cards.player_deck) != 0:
        if take_card and deck_image_rect.collidepoint(
                pygame.mouse.get_pos()) and not turn_took:
            if len(cards.player_hands) <= 10:
                card = random.choice(cards.player_deck)
                cards.player_deck.remove(card)
                player.take_card(card)
                take_card = False
                turn_took = True
                can_turn = True
    elif len(cards.player_deck) == 0:
        deck_image = deck_image_empty
        can_turn = True
        stop_output_text_before_taking = True
        output_text_before_taking = False
    if deck_image_rect.collidepoint(
            pygame.mouse.get_pos()) and len(cards.player_deck) != 0:
        deck_image = deck_full_point
    if len(cards.player_hands) > 10 and deck_image_rect.collidepoint(pygame.mouse.get_pos()) \
            and len(cards.player_deck) != 0:
        output_not_enough_space = True
    else:
        output_not_enough_space = False
    take_card = False
    screen.blit(deck_image, deck_image_rect)


def turn_button_def(screen):
    global turn_push, turn_player, output_text_before_taking, turn_button, card_action, can_player_attack
    turn_button_rect = turn_button.get_rect(
        midright=(width - width / 100,
                  (height // 4) + (deck_full.get_height() / 1.3)))
    if turn_button_rect.collidepoint(pygame.mouse.get_pos()):
        image = turn_button_point
    else:
        image = turn_button
    screen.blit(image, turn_button_rect)
    if turn_push and turn_button_rect.collidepoint(pygame.mouse.get_pos()):
        turn_player = False
        turn_push = False
        card_action = False
        can_player_attack = True
    elif not turn_push and turn_button_rect.collidepoint(pygame.mouse.get_pos()) and not turn_took \
            and not stop_output_text_before_taking:
        output_text_before_taking = True
        card_action = False
    elif not turn_push and not turn_button_rect.collidepoint(
            pygame.mouse.get_pos()):
        output_text_before_taking = False


def card_battle(player, enemy):
    global turn_enemy, can_enemy_attack, turn_player, can_player_attack

    # creating lists if cards on field
    field_cards_player = [0, 1, 2, 3]
    field_cards_enemy = [0, 1, 2, 3]
    for card, num in player.card_in_game.items():
        field_cards_player.remove(num)
        field_cards_player.insert(num, card)
    for card, num in enemy.card_in_game.items():
        field_cards_enemy.remove(num - 4)
        field_cards_enemy.insert(num - 4, card)

    if can_player_attack:

        # player's turn
        for p_card in field_cards_player:
            if type(p_card) != int:
                for e_card in field_cards_enemy:
                    if field_cards_player.index(
                            p_card) == field_cards_enemy.index(e_card):
                        if type(e_card) == int:
                            enemy.reduce_hp(p_card.atk)
                        else:
                            e_card.hp -= p_card.atk
        can_player_attack = False

    if not turn_player:

        turn_enemy = True

        # enemy's turn
        if can_enemy_attack:
            for e_card in field_cards_enemy:
                if type(e_card) != int:
                    for p_card in field_cards_player:
                        if field_cards_enemy.index(
                                e_card) == field_cards_player.index(p_card) and e_card.hp != 0:
                            if type(p_card) == int:
                                player.reduce_hp(e_card.atk)
                            else:
                                p_card.hp -= e_card.atk
            can_enemy_attack = False
            turn_player = True
            turn_enemy = False


def battle_scene(battle_screen, player, enemy):
    global take_card, card_show, card_action, deck_image, hold_card, release_hold, turn_push, show_FPS
    # background image
    battle_screen.blit(bg_battle, (0, 0))
    pygame.mouse.set_visible(False)

    # game code
    deck_def(player, battle_screen)
    turn_button_def(battle_screen)
    enemy.output(battle_screen)
    player.output(battle_screen)
    card_battle(player, enemy)

    # checking player's actions
    for events in pygame.event.get():
        '''Exiting'''
        if events.type == pygame.QUIT:
            sys.exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                sys.exit()
            if events.key == pygame.K_F1:
                show_FPS = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_F1:
                show_FPS = False
        if events.type == pygame.MOUSEBUTTONDOWN:
            if events.button == 3 and not card_action:
                card_show = True
                card_action = True
            if events.button == 1 and not card_action:
                hold_card = True
                release_hold = False
                card_action = True
                take_card = True
                if can_turn:
                    turn_push = True
        if events.type == pygame.MOUSEBUTTONUP:
            if events.button == 3:
                card_show = False
                card_action = False
            if events.button == 1:
                release_hold = True
                turn_push = False


def main_menu_scene(main_menu, font):
    global episode
    pygame.mouse.set_visible(True)
    main_menu.blit(bg_menu, (0, 0))

    # start button
    start_button = font.render('New game', False, (0, 0, 0))
    start_button_rect = start_button.get_rect(center=(width / 2, height / 2
                                                      - (start_button.get_height() * 3)))
    main_menu.blit(start_button, start_button_rect)

    # continue button
    continue_button = font.render('Continue', False, (0, 0, 0))
    continue_button_rect = continue_button.get_rect(center=(width / 2,
                                                            height / 2 - continue_button.get_height()))
    main_menu.blit(continue_button, continue_button_rect)

    # settings button
    settings_button = font.render('Settings', False, (0, 0, 0))
    settings_button_rect = settings_button.get_rect(center=(width / 2,
                                                            height / 2 + settings_button.get_height()))
    main_menu.blit(settings_button, settings_button_rect)

    # exit button
    exit_button = font.render('Exit', False, (0, 0, 0))
    exit_button_rect = exit_button.get_rect(center=(width / 2, height / 2
                                                    + (exit_button.get_height() * 3)))
    main_menu.blit(exit_button, exit_button_rect)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                episode = 'beginning'
            elif continue_button_rect.collidepoint(pygame.mouse.get_pos()):
                episode = 'battle'
            elif exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                sys.exit()
