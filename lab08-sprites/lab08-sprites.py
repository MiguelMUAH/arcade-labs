import random
import arcade

SPRITE_SCALING_PLAYER = 0.6
SPRITE_SCALING_COIN = 0.028
SPRITE_SCALING_DEBT = 0.4
COIN_COUNT = 20
DEBT_COUNT = 20
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 700


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.REDWOOD)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Hacienda Simulator 2", 300, 300,
                         arcade.color.DUTCH_WHITE, font_size=160, anchor_x="center", font_name="Kenney Pixel")
        arcade.draw_text("Click to play", 200, 124,
                         arcade.color.COOL_BLACK, font_size=80, anchor_x="center", font_name="Kenney Pixel")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.PURPLE_NAVY)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Guía rápida", 300, 200,
                         arcade.color.BLACK, font_size=200, anchor_x="center", font_name="Kenney Pixel")
        arcade.draw_text("Desplaza el cursor para mover a la agencia tributaria .Recolecta todo el dinero que puedas."
                         "Evita deudas.",
                         300, 200,
                         arcade.color.GRAY, font_size=30, anchor_x="center", font_name="Kenney Pixel")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        mygame = MyGame()
        self.window.show_view(mygame)


class Coin(arcade.Sprite):

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "HACIENDA 2")
        self.background = arcade.load_texture("ministerio.jpg")
        self.player_list = None
        self.coin_list = None
        self.debt_list = None
        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.debt_list = arcade.SpriteList()
        # Score
        self.score = 0
        self.player_sprite = arcade.Sprite("Agencia_Tributaria.svg.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        for i in range(COIN_COUNT):
            coin = Coin("12-Moneda-de-1-euro.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)
        for j in range(DEBT_COUNT):
            debt = Coin("ImagenBBO.png", SPRITE_SCALING_DEBT)
            debt.center_x = random.randrange(SCREEN_WIDTH)
            debt.center_y = random.randrange(SCREEN_HEIGHT)
            self.debt_list.append(debt)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.background)
        self.coin_list.draw()
        self.debt_list.draw()
        self.player_list.draw()
        output = f"Beneficial neto: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        self.coin_list.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        for coin in coins_hit_list:
            coin.reset_pos()
            self.score += 1
        self.debt_list.update()
        debt_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.debt_list)
        for debt in debt_hit_list:
            debt.reset_pos()
            self.score -= 1


def main():
    window = MyGame()
    window.setup()
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
