import arcade

WIDTH = 640
HEIGHT = 480
window_title = "Mario"
arcade.open_window(WIDTH, HEIGHT, window_title)
arcade.set_background_color(arcade.color.WHITE)


class Mario:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        # Cabeza
        arcade.draw_circle_filled(self.x, self.y + 60, 25, arcade.color.FAWN)
        arcade.draw_circle_filled(self.x - 15, self.y + 60, 8, arcade.color.WHITE)
        arcade.draw_circle_filled(self.x + 15, self.y + 60, 8, arcade.color.WHITE)
        arcade.draw_circle_filled(self.x - 16, self.y + 63, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x + 14, self.y + 63, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x, self.y + 45, 5, arcade.color.BLACK)
        arcade.draw_arc_filled(self.x, self.y + 60, 25, 25, arcade.color.BLACK, 20, 160)

        # Cuerpo
        arcade.draw_rectangle_filled(self.x, self.y + 25, 50, 50, arcade.color.FAWN)

        # Brazos
        arcade.draw_rectangle_filled(self.x - 40, self.y + 20, 20, 10, arcade.color.FAWN)
        arcade.draw_rectangle_filled(self.x + 40, self.y + 20, 20, 10, arcade.color.FAWN)
        arcade.draw_triangle_filled(self.x - 40, self.y + 15, self.x - 50, self.y - 20, self.x - 20, self.y - 20,
                                    arcade.color.FAWN)
        arcade.draw_triangle_filled(self.x + 40, self.y + 15, self.x + 50, self.y - 20, self.x + 20, self.y - 20,
                                    arcade.color.FAWN)

        # Manos
        arcade.draw_circle_filled(self.x - 50, self.y - 20, 7, arcade.color.WHITE)
        arcade.draw_circle_filled(self.x + 50, self.y - 20, 7, arcade.color.WHITE)
        arcade.draw_circle_filled(self.x - 52, self.y - 20, 3, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x + 48, self.y - 20, 3, arcade.color.BLACK)

        # Piernas
        arcade.draw_triangle_filled(self.x - 15, self.y - 45, self.x - 35, self.y - 90, self.x - 5, self.y - 90,
                                    arcade.color.FAWN)
        arcade.draw_triangle_filled(self.x + 15, self.y - 45, self.x + 35, self.y - 90, self.x + 5, self.y - 90,
                                    arcade.color.FAWN)

        # Zapatos
        arcade.draw_rectangle_filled(self.x - 30, self.y - 90, 20, 10, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.x + 30, self.y - 90, 20, 10, arcade.color.BLACK)

        # Botones
        arcade.draw_circle_filled(self.x, self.y + 10, 6, arcade.color.YELLOW)


def on_draw(delta_time):
    arcade.start_render()
    Mario.draw(Mario(300, 200))
    arcade.finish_render()


def main():
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


if __name__ == "__main__":
    main()
