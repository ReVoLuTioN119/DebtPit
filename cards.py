import pygame.font

import controls_and_game_defs as controls

pygame.init()


class Card:
    def __init__(self, name, atk, hp, cost, image, show, special='', special_image='', special_desc=''):
        self.name_text_rect = None
        self.name_text = None
        self.atk_text_rect = None
        self.atk_text = None
        self.hp_text_rect = None
        self.hp_text = None
        self.font = pygame.font.Font('images/font.ttf', int(50 / controls.correction_mult))
        self.name = name
        self.atk = atk
        self.hp = hp
        self.cost = cost
        self.special = [special, special_image, special_desc]
        self.image = image
        self.show = show
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()

    def hp_count(self):
        if type(self.hp) == int:
            if self.hp < 0:
                self.hp = 0

    def stats(self, screen, hp_text_rect='', atk_text_rect='', name_text_rect=''):
        self.hp_count()

        # name output
        self.name_text = self.font.render(self.name, False, (0, 0, 0))
        self.name_text_rect = self.name_text.get_rect()
        if name_text_rect == '':
            self.name_text_rect.midtop = self.rect.midtop
            self.name_text_rect.y += 20
        else:
            self.name_text_rect.midtop = name_text_rect
            self.name_text_rect.y += 20
        screen.blit(self.name_text, self.name_text_rect)

        # atk output
        self.atk_text = self.font.render(str(self.atk), False, (0, 0, 0))
        self.atk_text_rect = self.atk_text.get_rect()
        if atk_text_rect == '':
            self.atk_text_rect.bottomleft = self.rect.bottomleft
            self.atk_text_rect.x += 20
            self.atk_text_rect.y -= 20
        else:
            self.atk_text_rect.bottomleft = atk_text_rect
            self.atk_text_rect.x += 20
            self.atk_text_rect.y -= 20
        screen.blit(self.atk_text, self.atk_text_rect)

        # hp output
        self.hp_text = self.font.render(str(self.hp), False, (0, 0, 0))
        self.hp_text_rect = self.hp_text.get_rect()
        if hp_text_rect == '':
            self.hp_text_rect.bottomright = self.rect.bottomright
            self.hp_text_rect.x -= 20
            self.hp_text_rect.y -= 20
        else:
            self.hp_text_rect.bottomright = hp_text_rect
            self.hp_text_rect.x -= 20
            self.hp_text_rect.y -= 20
        screen.blit(self.hp_text, self.hp_text_rect)


card1 = Card('kirril', 1, 2, '', controls.card_image, controls.cardd_show)
card2 = Card('kirill1', 1, 2, '', controls.card_image, controls.cardd_show)
card3 = Card('kirill2', 1, 2, '', controls.card_image, controls.cardd_show)
card4 = Card('kirill3', 1, 2, '', controls.card_image, controls.cardd_show)
card5 = Card('kirill4', 1, 2, '', controls.card_image, controls.cardd_show)
card6 = Card('kirill5', 1, 2, '', controls.card_image, controls.cardd_show)
card7 = Card('kirill6', 1, 2, '', controls.card_image, controls.cardd_show)
card8 = Card('kirill7', 1, 2, '', controls.card_image, controls.cardd_show)
card9 = Card('kirill8', 1, 2, '', controls.card_image, controls.cardd_show)
card10 = Card('kirill9', 1, 2, '', controls.card_image, controls.cardd_show)
card11 = Card('kirill0', 1, 2, '', controls.card_image, controls.cardd_show)
card12 = Card('kirill00', 1, 2, '', controls.card_image, controls.cardd_show)
card13 = Card('1', 1, 2, '', controls.card_image, controls.cardd_show)
card14 = Card('2', 1, 3, '', controls.card_image, controls.cardd_show)
card15 = Card('3', 1, 4, '', controls.card_image, controls.cardd_show)
correct = Card('', '', '', '', controls.card_correct, '')

all_cards = (card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12)
player_deck = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11]
enemy_deck = [card13, card15]
player_hands = [card12]
enemy_hands = [card14]
player_dead_cards = []
enemy_dead_cards = []
