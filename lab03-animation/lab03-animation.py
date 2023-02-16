import arcade


def dibujar_suelo():
    arcade.draw_lrtb_rectangle_filled(0, 1700, 100, 0, arcade.color.GRAY)


def dibujar_nube(posicion):
    arcade.draw_circle_filled(posicion + 150, 650, 80, arcade.color.WHITE)
    arcade.draw_circle_filled(posicion + 250, 630, 80, arcade.color.WHITE)
    arcade.draw_circle_filled(posicion + 350, 660, 80, arcade.color.WHITE)
    arcade.draw_circle_filled(posicion + 410, 660, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(posicion + 75, 660, 40, arcade.color.WHITE)


def dibujar_persona(posicion, altura):
    arcade.draw_circle_filled(posicion, altura, 30, arcade.color.BLACK)  # cabeza
    arcade.draw_lrtb_rectangle_filled(posicion - 5, posicion + 5, altura, altura - 140, arcade.color.BLACK)  # cuerpo
    arcade.draw_lrtb_rectangle_filled(posicion + 5, posicion + 45, altura - 50, altura - 60, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(posicion - 45, posicion + 15, altura - 50, altura - 60, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(posicion - 7, posicion - 2, altura - 130, altura - 220, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(posicion + 2, posicion + 7, altura - 130, altura - 220, arcade.color.BLACK)
    arcade.draw_circle_filled(posicion - 10, altura, 10, arcade.color.WHITE)  # ojos
    arcade.draw_circle_filled(posicion + 20, altura, 10, arcade.color.WHITE)
    arcade.draw_circle_filled(posicion + 20, altura, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(posicion - 10, altura, 5, arcade.color.BLACK)


def dibujar(tiempo):
    arcade.start_render()

    dibujar_suelo()
    dibujar_persona(dibujar.persona2_x, dibujar.persona2_y)
    dibujar_persona(dibujar.persona1_x, dibujar.persona1_y)
    dibujar.persona1_x += 1
    dibujar.persona2_x += 1.3
    dibujar.persona2_y -= 0.3


dibujar.persona1_x = 150
dibujar.persona1_y = 300
dibujar.persona2_x = 100
dibujar.persona2_y = 700

def ejecutar():
    arcade.open_window(1500, 700, "ANIMACION")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    arcade.schedule(dibujar, 1 / 120)
    arcade.run()


ejecutar()
