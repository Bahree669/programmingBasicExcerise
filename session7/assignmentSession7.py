# MADE WITH HEART 💛 BY SAEPUL BAHRI - 202200402277 - TI22I
from sys import platform
from time import sleep
import os


def clear_display():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    else:
        os.system('cls')


def display_menu():
    s = "="
    s_length = 27

    print(s * s_length)
    print('     SIMPLE CALCULATOR     ')
    print(s * s_length)

    print('Menu\n1. Find triangle area\n2. Find rectangle area\n3. Is even or odd?\n4. Clear display\n5. Quit')


def get_user_input():
    while True:
        user_ctrl = input('Enter command: ')

        if user_ctrl.isnumeric() and (int(user_ctrl) > 0 and int(user_ctrl) < 6):
            print('-' * 27)
            return int(user_ctrl)
        else:
            print('Invalid command!\n')


def find_triangle_area():
    print('=== FIND TRIANGLE AREA ===\n')

    base_len = float(input('Base length: '))
    height = float(input('Triangle height: '))

    print('Triangle area:', (base_len * height) / 2)


def find_rectangle_area():
    print('=== FIND RECTANGLE AREA ===\n')

    width = float(input('Rectangle Width: '))
    legnth = float(input('Rectangle length: '))
    print('Rectangle area: ', width * legnth)


def is_even():
    print('=== IS EVEN OR ORDD ===\n')

    num = float(input('Enter a number: '))
    print('Is even: ', num % 2 == 0)


def main():

    while True:
        display_menu()
        user_ctrl = get_user_input()
        clear_display()

        if user_ctrl == 1:
            find_triangle_area()
        elif user_ctrl == 2:
            find_rectangle_area()
        elif user_ctrl == 3:
            is_even()
        elif user_ctrl == 4:
            clear_display()
        else:
            print('Quiting...')
            sleep(1)
            clear_display()
            break

        print('-' * 27)


main()
