import arcade

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 700
MOVEMENT_SPEED = 3


def dibujar_persona(posicion, altura, radio):
    arcade.draw_circle_filled(posicion, altura, 30, arcade.color.BLACK)  # cabeza
    arcade.draw_lrtb_rectangle_filled(posicion - 5, posicion + 5, altura, altura - 140,
                                      arcade.color.BLACK)  # cuerpo
    arcade.draw_lrtb_rectangle_filled(posicion + 5, posicion + 45, altura - 50, altura - 60, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(posicion - 45, posicion + 15, altura - 50, altura - 60,
                                      arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(posicion - 7, posicion - 2, altura - 130, altura - 220,
                                      arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(posicion + 2, posicion + 7, altura - 130, altura - 220,
                                      arcade.color.BLACK)
    arcade.draw_circle_filled(posicion - 10, altura, 10, arcade.color.WHITE)  # ojos
    arcade.draw_circle_filled(posicion + 20, altura, 10, arcade.color.WHITE)
    arcade.draw_circle_filled(posicion + 20, altura, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(posicion - 10, altura, 5, arcade.color.BLACK)
class Personaje:
    def __init__(self, position_x, position_y, change_x, change_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        dibujar_persona(self.position_x, self.position_y, self.radius)
    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x
        if self.position_x < self.radius+20:
            self.position_x = self.radius+20

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius+190:
            self.position_y = self.radius+190

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class MyGame(arcade.Window):
    """ Ventana de la clase"""

    def __init__(self):
        """ Initializer """

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Control")
        self.personaje = Personaje(200,300, 0, 0, 30)
        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)
        arcade.start_render()
        # ACERA
        arcade.draw_lrtb_rectangle_filled(0, 1700, 100, 0, arcade.color.GRAY)
        # EDIFICIO
        arcade.draw_lrtb_rectangle_filled(400, 1200, 500, 40, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(400, 1200, 100, 40, arcade.color.BLACK_BEAN)
        arcade.draw_lrtb_rectangle_filled(600, 1000, 600, 300, arcade.color.ANDROID_GREEN)
        arcade.draw_lrtb_rectangle_filled(700, 900, 450, 350, arcade.color.COCOA_BROWN)
        arcade.draw_circle_filled(750, 460, 25, arcade.color.RED)
        arcade.draw_circle_filled(780, 455, 15, arcade.color.ORANGE_PEEL)
        arcade.draw_circle_filled(875, 460, 25, arcade.color.ARMY_GREEN)
        arcade.draw_circle_filled(865, 450, 25, arcade.color.APPLE_GREEN)
        arcade.draw_lrtb_rectangle_filled(700, 715, 500, 350, arcade.color.COCOA_BROWN)
        arcade.draw_lrtb_rectangle_filled(900, 915, 500, 350, arcade.color.COCOA_BROWN)
        arcade.draw_lrtb_rectangle_filled(700, 915, 500, 490, arcade.color.COCOA_BROWN)
        arcade.draw_lrtb_rectangle_filled(810, 830, 475, 450, arcade.color.PURPLE)
        arcade.draw_lrtb_rectangle_filled(815, 825, 490, 450, arcade.color.PURPLE)
        arcade.draw_lrtb_rectangle_filled(700, 900, 450, 350, arcade.color.COCOA_BROWN)
        arcade.draw_lrtb_rectangle_filled(600, 1000, 300, 40, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(610, 990, 290, 40, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_lrtb_rectangle_filled(790, 800, 300, 40, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(770, 780, 100, 70, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(810, 820, 100, 70, arcade.color.BLACK)
        # ARBOLES
        arcade.draw_lrtb_rectangle_filled(200, 250, 350, 100, arcade.color.BRONZE)
        arcade.draw_line(200, 250, 300, 200, arcade.color.BRONZE, 3)
        arcade.draw_line(230, 240, 160, 170, arcade.color.BRONZE, 3)
        arcade.draw_circle_filled(225, 350, 100, arcade.color.GO_GREEN)
        arcade.draw_lrtb_rectangle_filled(1300, 1350, 350, 100, arcade.color.BRONZE)
        arcade.draw_circle_filled(1325, 350, 100, arcade.color.GO_GREEN)
        # PERSONA
        arcade.draw_circle_filled(50, 300, 30, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(45, 55, 300, 160, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(55, 95, 250, 240, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(5, 65, 250, 240, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(43, 48, 170, 80, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(52, 57, 170, 80, arcade.color.BLACK)
        arcade.draw_circle_filled(40, 300, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(70, 300, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(70, 300, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(40, 300, 5, arcade.color.BLACK)
        def dibujar_nube(posicion):
            arcade.draw_circle_filled(posicion + 150, 650, 80, arcade.color.WHITE)
            arcade.draw_circle_filled(posicion + 250, 630, 80, arcade.color.WHITE)
            arcade.draw_circle_filled(posicion + 350, 660, 80, arcade.color.WHITE)
            arcade.draw_circle_filled(posicion + 410, 660, 40, arcade.color.WHITE)
            arcade.draw_circle_filled(posicion + 75, 660, 40, arcade.color.WHITE)

        dibujar_nube(200)
        # MONEDA
        arcade.draw_circle_filled(100, 250, 7, arcade.color.YELLOW)
        arcade.draw_circle_filled(100, 250, 5, arcade.color.SILVER)
        # SOL
        arcade.draw_circle_filled(100, 650, 100, arcade.color.YELLOW)
        # CARTERA CON DINERO ALREDEDOR
        arcade.draw_lrtb_rectangle_filled(300, 330, 60, 40, arcade.color.RED_BROWN)
        arcade.draw_lrtb_rectangle_filled(340, 380, 50, 30, arcade.color.ARMY_GREEN)
        arcade.draw_lrtb_rectangle_filled(345, 375, 45, 35, arcade.color.ANDROID_GREEN)
        dibujar_persona(1200, 300, 0)
        dibujar_persona(1350, 400, 0)
        dibujar_persona(900, 250, 0)
        self.personaje.draw()
        arcade.finish_render()
    def update(self, delta_time):
        self.personaje.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
                self.personaje.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
                self.personaje.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
                self.personaje.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
                self.personaje.change_y = -MOVEMENT_SPEED

    def on_key_release( self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.personaje.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.personaje.change_y = 0



def main():
    window = MyGame()
    arcade.run()

main()
