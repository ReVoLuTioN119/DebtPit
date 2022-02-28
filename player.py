import pygame.mouse

import cards
import controls_and_game_defs as controls


class Player:
    def __init__(self, deck, player_fields):
        self.card_out = False
        self.card_in_game = {}
        self.card_rect = (0, 0)
        self.move = False
        self.hold_card = []
        self.card_pos = []
        self.deck = deck
        self.player_fields = player_fields
        self.hp = 5
        self.card_to_hold = None
        self.card_to_hold_rect = None

    def reduce_hp(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def take_card(self, card):
        self.deck.append(card)

    def output_fields(self, screen):
        for field in self.player_fields:
            field.output(screen, self.card_in_game)

    def output_hp_hand(self, screen):
        hand_image = eval('controls.arm_player_' + str(self.hp))
        hand_image_rect = hand_image.get_rect()
        hand_image_rect.topleft = pygame.mouse.get_pos()
        screen.blit(hand_image, hand_image_rect)

    def output_cards(self, screen):
        for card in list(self.card_in_game):       
          if card.hp == 0:          
            for field in self.player_fields:
               if field.num == self.card_in_game[card]:
                 field.image = controls.field_image 
            cards.player_dead_cards.append(card)
            del self.card_in_game[card]
              
        # count card pos
        if len(self.deck) > 11:
            self.deck = self.deck[0:11]
        n = 0
        offset = 0
        for card in self.deck:
            if 0 < len(self.deck) <= 9:
                offset = 1.84
            elif len(self.deck) == 10:
                offset = 2.07
            elif len(self.deck) == 11:
                offset = 2.3
            card_move = (card.image.get_height() + (card.image.get_height() / 25)) / offset
            card_width = card.image.get_width()
            card.rect = card.image.get_rect(center=((controls.width / 1.09) - (card_move * n),
                                                    controls.height - (card_width / 1.2)))
            n += 1

            # put the card out
            if card.rect.collidepoint(pygame.mouse.get_pos()) and not controls.card_action:
                card.rect.centery -= 60

            # card actions
            if controls.card_action:

                # zoom card
                if controls.card_show:
                    if card.rect.collidepoint(pygame.mouse.get_pos()):
                        card_show_rect = card.show.get_rect(midright=(controls.width - controls.width / 100,
                                                                      controls.height // 3))
                        screen.blit(card.show, card_show_rect)

                # hold card, move card and remove it from hands
                if controls.hold_card:
                    if card.rect.collidepoint(pygame.mouse.get_pos()):
                        if len(self.hold_card) < 1:
                            self.hold_card.clear()
                            self.hold_card.append(card)
                            self.deck.remove(card)
                            if len(self.deck) == 0:
                                self.deck.append(cards.correct)
                            self.move = True

                    if controls.release_hold:
                        self.move = False
                        controls.hold_card = False
                        controls.card_action = False

                        # put cards on the fields
                        for field in self.player_fields:
                            if field.image_rect.collidepoint(pygame.mouse.get_pos()):
                                if len(self.hold_card) != 0:
                                    if self.hold_card[0] not in self.card_in_game \
                                            and field.num not in self.card_in_game.values():
                                        self.card_in_game[self.hold_card[0]] = field.num
                                        self.hold_card.clear()
                                        controls.card_in_use = True
                        if len(self.hold_card) != 0 and not controls.card_in_use:
                            self.deck.append(self.hold_card[0])
                        controls.card_in_use = False
                        self.hold_card.clear()
                        if cards.correct in self.deck:
                            self.deck.remove(cards.correct)

                    # move card with cursor
                    if self.move and len(self.hold_card) != 0:
                        self.card_to_hold = self.hold_card[0].image
                        self.card_to_hold_rect = self.card_to_hold.get_rect(center=pygame.mouse.get_pos())
                        screen.blit(self.card_to_hold, self.card_to_hold_rect)
                        self.hold_card[0].stats(screen, self.card_to_hold_rect.bottomright,
                                                self.card_to_hold_rect.bottomleft, self.card_to_hold_rect.midtop)

            # output cards
            screen.blit(card.image, card.rect)
            card.stats(screen)

    def get_cards(self):
        return self.card_in_game

    def output(self, screen):
        self.output_fields(screen)
        self.output_cards(screen)
        self.output_hp_hand(screen)
