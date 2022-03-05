import pygame

import controls_and_game_defs as controls


class Field:
    def __init__(self, num):
        self.num = num
        self.image = controls.field_image
        if self.num < 4:
            self.image_rect = self.image.get_rect(
                bottomleft=(controls.width // 5.82 + ((self.image.get_width() + (controls.width / 21.3)) * self.num),
                            controls.height // 1.54)
            )
        elif self.num >= 4:
            self.image_rect = self.image.get_rect(
                bottomleft=(
                    controls.width // 5.82 + ((self.image.get_width() + (controls.width / 21.3)) * (self.num - 4)),
                    controls.height / 3.1))

    def output(self, screen, player_cards='', enemy_cards=''):
        screen.blit(self.image, self.image_rect)
        font = pygame.font.Font('images/font.ttf', int(100 / controls.correction_mult))

        # output player cards on player fields
        if player_cards != '':
            if len(player_cards) != 0:
                for card in player_cards.keys():
                    rect = self.image.get_rect(
                        bottomleft=((controls.width / 5.84) + (player_cards[card] * (controls.width / 6.09)),
                                    controls.height / 1.54)
                    )
                    card.stats(screen, rect.bottomright, rect.bottomleft, rect.midtop)
                    for num in player_cards.values():
                        if self.num == num:
                            self.image = card.image

        # output enemy cards on enemy fields
        if enemy_cards != '':
            if len(enemy_cards) != 0:
                for card in enemy_cards.keys():
                    rect = self.image.get_rect(bottomleft=((controls.width / 5.84) + ((controls.width / 6.09) *
                                                                (int(enemy_cards[card]) - 4)), controls.height / 3.1))
                    card.stats(screen, rect.bottomright, rect.bottomleft, rect.midtop)
                    for num in enemy_cards.values():
                        if self.num == num:
                            self.image = card.image
        if controls.output_text_before_taking:
            take_card_text = font.render('You have to take card first', False, (0, 0, 0))
            take_card_text_rect = take_card_text.get_rect(center=(controls.width / 2, controls.height / 2))
            screen.blit(take_card_text, take_card_text_rect)
        if controls.output_not_enough_space:
            text = font.render('You have not enough space for new card', False, (0, 0, 0))
            text_rect = text.get_rect(center=(controls.width / 2, controls.height / 2))
            screen.blit(text, text_rect)


field1 = Field(0)
field2 = Field(1)
field3 = Field(2)
field4 = Field(3)
field5 = Field(4)
field6 = Field(5)
field7 = Field(6)
field8 = Field(7)
player_fields = [field1, field2, field3, field4]
enemy_fields = [field5, field6, field7, field8]
