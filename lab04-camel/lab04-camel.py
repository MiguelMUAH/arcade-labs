class Room:
    """
    Una sala.

    """

    def __init__(self, description, norte, sur, este, oeste):
        self.description = description
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste


def main():
    """
    Function main
    """
    room_list = []
    room0 = Room(
        "Apareces literalmente en una sala en medio de la nada sin ningún tipo de contexto ni información de como has acabado ahí.Puedes ir hacia cualquier dirección.",
        2, 4, 3, 1)
    room_list.append(room0)
    room1 = Room("Habitación curiosa", None, 9, 0, 5)
    room_list.append(room1)
    room2 = Room("Vestíbulo", None, 0, None, 10)
    room_list.append(room2)
    room3 = Room("Pasillo increiblemente corto", None, None, 6, 0)
    room_list.append(room3)
    room4 = Room("Habitación con cofre", 0, None, 7, None)
    room_list.append(room4)
    room5 = Room("Salón de actos", 10, None, 1, None)
    room_list.append(room5)
    room6 = Room("Cuarto de J", None, 8, None, 3)
    room_list.append(room6)
    room7 = Room("Camino tétrico", None, None, 8, 4)
    room_list.append(room7)
    room8 = Room("Armería", 6, None, None, 7)
    room_list.append(room8)
    room9 = Room("Sala con pasadizo", 1, None, None, 2)
    room_list.append(room9)
    room10 = Room("Sala túnel", None, 5, None, None)
    room_list.append(room10)
    current_room = 0
    next_room = 0
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        respuesta = input("Para moverte , escriba N para norte , S para sur , E para este , W para oeste o salir para cerrar el juego")
        if respuesta.lower() == "salir":
            done = True
        elif respuesta.lower() == "n":
            next_room = room_list[current_room].norte
        elif respuesta.lower() == "s":
            next_room = room_list[current_room].sur
        elif respuesta.lower() == "e":
            next_room = room_list[current_room].este
        elif respuesta.lower() == "o":
            next_room = room_list[current_room].oeste
        if next_room is None:
            print("No puedes ir por ahí")
        else:
            current_room = next_room


main()
