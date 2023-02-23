import arcade


def dibujar_suelo():
    arcade.draw_lrtb_rectangle_filled(0, 1700, 100, 0, arcade.color.GRAY)


def dibujar_luna(altura):
    arcade.draw_circle_filled(750, altura, 200, arcade.color.GRAY)
    arcade.draw_circle_filled(870, altura, 160, arcade.color.DARK_BLUE)


def dibujar_nube(posicion):
    arcade.draw_circle_filled(posicion + 150, 650, 80, arcade.color.WHITE)
    arcade.draw_circle_filled(posicion + 250, 630, 80, arcade.color.WHITE)
    arcade.draw_circle_filled(posicion + 350, 660, 80, arcade.color.WHITE)
    arcade.draw_circle_filled(posicion + 410, 660, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(posicion + 75, 660, 40, arcade.color.WHITE)


def dibujar_sol(altura):
    arcade.draw_circle_filled(750, altura, 200, arcade.color.ORIOLES_ORANGE)


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
    dibujar_luna(dibujar.luna_y)
    dibujar_sol(dibujar.sol_y)
    dibujar_suelo()
    dibujar_persona(dibujar.persona2_x, 240)
    dibujar_persona(dibujar.persona1_x, dibujar.persona1_y)
    dibujar_nube(dibujar.nube1_x)
    dibujar_nube(dibujar.nube2_x)
    dibujar.persona1_x += 1
    dibujar.persona2_x += 1.3
    dibujar.nube1_x -= 0.9
    dibujar.nube2_x -= 1.2
    dibujar.sol_y -= 1.15
    dibujar.luna_y += 0.9


dibujar.sol_y = 360
dibujar.nube2_x = 1200
dibujar.persona1_x = 150
dibujar.persona1_y = 300
dibujar.persona2_x = 100
dibujar.persona2_y = 700
dibujar.nube1_x = 600
dibujar.luna_y = -450


def ejecutar():
    arcade.open_window(1500, 700, "ANIMACION")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    arcade.schedule(dibujar, 1 / 120)
    arcade.run()


ejecutar()
