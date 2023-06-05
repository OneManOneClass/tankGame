from tankas import Tankas
from time import sleep
from enemy import Enemy
from arena import Arena
from random import randrange
import os
import pickle

INSTRUCTIONS = '''++++++++++++++Sveiki atvykę į karo lauką!++++++++++++++\n
Tanko judėjimui kuras. Kiekvienas judesys atima 10 kuro taškų, o nepataikytas
šūvis atima 20 kuro taškų. Už pataikymą į priešą gaunate 20 kuro taškų. Kiekvienas
žaidėjas (X) pradeda žaidimą su 150 kuro taškų.\n
Norėdami pataikyti į priešą turite būti vienoje ašyje ir atsisukę į taikinį (O).'''

MENU_STRING = "1. Pradėti naują žaidimą \n2. TOP žaidėjai \n3. Žaidimo taisyklės\n4. Išeiti \n"
OUT_OF_BOUNDS_STRING = "Generolo įsakymu palikti mūšio lauką griežtai draudžiama!"
EXIT_STRING = "Viso gero!"
OUT_OF_FUEL_STRING = "Jums pasibaigė kuras! Žaidimas baigtas."
CONTROLS_STRING = "Judėti: W,A,S,D     Šauti: P    Info: I     Išeiti (Meniu): Q  "

ARENA_WIDTH = 10
ARENA_HEIGHT = 10

top_players = []


def menu():
    while True:
        menu_action = input(MENU_STRING)
        match menu_action:
            case ("1"):
                game()
            case ("2"):
                if top_players:
                    os.system('cls')
                    print_top_players()
                else:
                    print("Mušio lauke dar nebuvo nei vieno žaidėjo... Būk pirmas!")
            case ("3"):
                os.system('cls')
                print(INSTRUCTIONS)
            case ("4"):
                print(EXIT_STRING)
                break


def game():
    player = Tankas()
    enemy = Enemy({'X': coordinate_generator(), 'Y': coordinate_generator()})
    arena = Arena(ARENA_WIDTH, ARENA_HEIGHT, player.position, enemy.position)
    os.system('cls')
    while True:
        if player.fuel == 0:
            os.system('cls')
            print(OUT_OF_FUEL_STRING)
            add_score(player)
            del player
            break
        print(player)
        arena.draw()
        action = (input(CONTROLS_STRING)).upper()
        match action:
            case ("W"):
                if player.position['Y'] < arena.height / 2:
                    player.move_up()
                    os.system('cls')
                else:
                    print(OUT_OF_BOUNDS_STRING)
            case ("S"):
                if player.position['Y'] > -arena.height / 2:
                    player.move_down()
                    os.system('cls')
                else:
                    print(OUT_OF_BOUNDS_STRING)
            case ("A"):
                if player.position['X'] > -arena.width / 2:
                    player.move_left()
                    os.system('cls')
                else:
                    print(OUT_OF_BOUNDS_STRING)
            case ("D"):
                if player.position['X'] < arena.width / 2:
                    player.move_right()
                    os.system('cls')
                else:
                    print(OUT_OF_BOUNDS_STRING)
            case ("P"):
                if player.shoot(enemy.position):
                    enemy = Enemy({'X': coordinate_generator(), 'Y': coordinate_generator()})
                    arena = Arena(ARENA_WIDTH, ARENA_HEIGHT, player.position, enemy.position)
                    os.system('cls')
                    print("Pataikei!")
                else:
                    os.system('cls')
                    print("Nepataikei!")
            case ("I"):
                print(player.info())
            case ("Q"):
                del player
                print(EXIT_STRING)
                break


def coordinate_generator():
    return randrange(int(ARENA_HEIGHT / 2) * -1, int(ARENA_HEIGHT / 2) + 1)


def print_top_players():
    i = 1
    print('**************************TOP  5**************************')
    for score in top_players:
        print(f'#{i} Vardas: {score[0]:<22} Sunaikinti taikiniai: {score[1]}')
        i += 1
    print('*' * 58)


def add_score(player):
    sleep(1)
    top_players.append((input("Įveskite žaidėjo vardą: "), player.score))
    top_players.sort(key=lambda s: s[1], reverse=True)
    if len(top_players) > 5:
        top_players.pop(5)
    with open("top_players.pkl", 'wb') as top_players_file:
        pickle.dump(top_players, top_players_file)


def main():
    menu()


if __name__ == '__main__':
    try:
        with open("top_players.pkl", 'rb') as top_players_file:
            top_players = pickle.load(top_players_file)
    except FileNotFoundError:
        pass
    except EOFError:
        pass
    main()
