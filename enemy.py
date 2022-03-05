import random

import controls_and_game_defs as controls
from cards import enemy_dead_cards


class Enemy:
    def __init__(self, enemy_cards, enemy_fields, enemy_deck, name, image, description):
        self.name = name
        self.description = description
        self.image = image
        self.hp = 5
        self.enemy_cards = enemy_cards
        self.enemy_fields = enemy_fields
        self.card_in_game = {}
        self.enemy_deck = enemy_deck
        self.free_fields = []
        self.free_fields.extend(self.enemy_fields)

    def output_hp_hand(self, screen):
        hand_image = eval('controls.arm_enemy_' + str(self.hp))
        hand_image_rect = hand_image.get_rect(topleft=(0, 0))
        screen.blit(hand_image, hand_image_rect)

    def reduce_hp(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def pick_card(self):
        self.enemy_cards.append(random.choice(self.enemy_deck))

    def play_turn(self):
        # delete card if it's hp is 0
        for card in list(self.card_in_game):
            if card.hp == 0:
                self.free_fields.append(self.enemy_fields[self.card_in_game[card] - 4])
                busy_field = self.card_in_game[card]
                enemy_dead_cards.append(card)
                del self.card_in_game[card]
                for field in self.enemy_fields:
                    if field.num == busy_field:
                        field.image = controls.field_image

        if controls.turn_enemy:
            if len(self.enemy_cards) != 0:
                controls.can_turn = False
            else:
                controls.stop_output_text_before_taking = True
            self.pick_card()
            for card in self.enemy_cards:
                shall_put_card = random.randint(1, 3)
                if shall_put_card != 1 and len(self.free_fields) != 0:
                    put_field = random.choice(self.free_fields)
                    if put_field.num not in self.card_in_game.values() and card not in self.card_in_game.keys() \
                            and card.hp != 0:
                        self.free_fields.remove(put_field)
                        self.card_in_game[card] = put_field.num
            controls.take_card = True
            controls.turn_took = False
            controls.can_enemy_attack = True

    def output_fields(self, screen):
        for field in self.enemy_fields:
            field.output(screen, '', self.card_in_game)
            if controls.reset_player:
                field.image = controls.field_image

    def output(self, screen):
        self.output_fields(screen)
        self.output_hp_hand(screen)
        self.play_turn()
