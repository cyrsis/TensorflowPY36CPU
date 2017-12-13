"""Kafka - the adventure game you cannot win."""


def play():

    position = (0, 0)
    alive = True

    while position:

        if position == (0, 0):
            print("You are in a maze of twisty passages, all alike.")
        elif position == (1, 0):
            print("You are on a road in a dark forest. To the north you can see a tower.")
        elif position == (1, 1):
            print("There is a tall tower here, with no obvious door. A path leads east.")
        else:
            print("There is nothing here.")

        command = input()

        i, j = position
        if command == "N":
            position = (i, j + 1)
        elif command == "E":
            position = (i + 1, j)
        elif command == "S":
            position = (i, j - 1)
        elif command == "W":
            position = (i - 1, j)
        elif command == "L":
            pass
        elif command == "Q":
            position = None
        else:
            print("I don't understand")

    print("Game over")

if __name__ == '__main__':
    play()
