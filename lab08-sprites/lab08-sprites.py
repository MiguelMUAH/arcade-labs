import random
import arcade

SPRITE_SCALING_PLAYER = 0.6
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 20

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 700


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")
        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.WHITE_SMOKE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()


def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
