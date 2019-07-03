import pygame

from ball import Ball
from block import init_blocks
from colors import BLACK, GREY
from game_states import GameStates
from message import (
    FONT,
    FONT_SIZE,
    LIVES_X,
    LIVES_Y,
    SCORE_X,
    SCORE_Y,
    get_rendered_text,
    search_font,
)
from player import Player
from wall import init_walls


class Game:
    def __init__(self):
        self.player = Player()
        self.ball = Ball()
        self.walls = init_walls()
        self.blocks = init_blocks()
        self.font = search_font(FONT)
        self.score = 0
        self.lives = 3

    def update(self, action):
        move = action.get("move")
        launch = action.get("launch")

        self.player.update(move, self.walls)
        results = self.ball.update(launch, self.player, self.blocks, self.walls)

        loss = results.get("loss")
        self.score += results.get("points")

        if loss:
            self.lives -= 1

            if self.lives > 0:
                self.player = Player()
                self.ball = Ball()
                return {"lost": False}
            else:
                return {"lost": True}

        return {}

    def render(self, screen, game_state):
        screen.fill(BLACK)

        self.player.render(screen)
        self.ball.render(screen)
        for block in self.blocks:
            block.render(screen)
        for wall in self.walls:
            wall.render(screen)

        score_text = get_rendered_text(self.font, FONT_SIZE, GREY, str(self.score))
        lives_text = get_rendered_text(self.font, FONT_SIZE, GREY, str(self.lives))

        screen.blit(score_text, (SCORE_X, SCORE_Y))
        screen.blit(lives_text, (LIVES_X, LIVES_Y))

        if game_state == GameStates.MAIN_MENU:
            title_text = get_rendered_text(self.font, 100, BLACK, "BREAKOUT")
            menu_text_1 = get_rendered_text(self.font, 50, GREY, "1. Play game")
            menu_text_2 = get_rendered_text(self.font, 50, GREY, "2. Exit")

            screen.blit(title_text, (210, 150))
            screen.blit(menu_text_1, (250, 270))
            screen.blit(menu_text_2, (250, 315))

        if game_state == GameStates.GAME_OVER:
            title_text = get_rendered_text(self.font, 100, GREY, "GAME OVER")
            menu_text_1 = get_rendered_text(self.font, 50, GREY, "1. Play again")
            menu_text_2 = get_rendered_text(self.font, 50, GREY, "2. Exit")

            screen.blit(title_text, (210, 150))
            screen.blit(menu_text_1, (250, 270))
            screen.blit(menu_text_2, (250, 315))

        pygame.display.flip()
