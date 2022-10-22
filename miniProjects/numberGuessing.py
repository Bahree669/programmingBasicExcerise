from random import choice, randint
from sys import platform
import os
from time import sleep


general_commands = [
    {'name': '-h', 'func': 'open help menu'},
    {'name': 'play', 'func': 'play the game'},
    {'name': 'close', 'func': 'close the game'},
    {'name': 'clear', 'func': 'clear display'},
]


# =================== UTILITIES FUNCTIONS
def clear_display():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('cls')
    elif platform == "win32":
        os.system('cls')


def display_help(commands):
    display_format = "{:<15} {:<20}"

    print('----------------------------------')
    print(display_format.format(
        '| Command', '| Functions'
    ))
    print('----------------------------------')

    for cmd in commands:
        print(display_format.format(
            f"| {cmd['name']}", f"| {cmd['func'].capitalize()}"
        ))
    print('----------------------------------\n')


# =================== GAME UTILS
def get_random_number():
    return randint(1, 20)


def game_over_msg(msg):
    print(msg)
    sleep(.5)
    print('Returning to home...')
    sleep(1.5)
    clear_display()


def display_bar(bar_name, amnt, style):
    bar = ''
    for _ in range(amnt):
        bar += style
    print('----------------------------------')
    print(bar_name, bar)
    print('----------------------------------')


def display_clue(n):
    clues = ['m', 'a', 's', 'd']
    picked_clues = choice(clues)

    print('----------------------------------')
    rndm_num = get_random_number()
    if picked_clues == 'm':
        print(f"NUM x {rndm_num} = {n * rndm_num}")
    elif picked_clues == 'a':
        print(f"NUM + {rndm_num} = {n + rndm_num}")
    elif picked_clues == 's':
        print(f"NUM - {rndm_num} = {n - rndm_num}")
    else:
        print(f"NUM / {rndm_num} = {n / rndm_num}")
    print('----------------------------------')


def play():
    guess_left = 3
    score = 0

    while True:
        # get random number each iteration
        rndm_num = get_random_number()

        # display the bar
        print('🔢 MAKE A GUESS 🔢')
        display_bar(amnt=guess_left, style='🧡', bar_name='Guess left:')
        display_bar(amnt=score, style='⭐', bar_name='Score:')

        display_clue(rndm_num)

        user_guess = input('Your guess: ')

        # end the game
        if user_guess == 'end':
            game_over_msg('Closing game...')
            break
        if int(user_guess) == rndm_num:
            score += 1
            print('🎉 Congrats! you guessed the right number 🎉')
            sleep(1)
            clear_display()
        else:
            # everytime the user guessed the wrong number
            # decrement the guess_left by 1 and display clue
            guess_left -= 1

            print('You guessed the wrong number, please try again!\n')
            sleep(1.5)
            clear_display()

            # end the game if user live is 0
            if guess_left == 0:
                game_over_msg(
                    msg='😢😢😢 Sorry you run out of guess! 💔💔💔')
                break


def main():
    # only show the 'help' menu on the first time the app is opened
    first_opening_game = True
    if first_opening_game:
        display_help(general_commands)
        first_opening_game = False

    while True:
        print('🔢 NUMBER GUESSING GAME 🔢\n')
        user_ctrl = input('> ').lower()

        clear_display()

        if user_ctrl == 'close':
            clear_display()
            break
        elif user_ctrl == 'play':
            play()
        elif user_ctrl == 'clear':
            clear_display()
        elif user_ctrl == '-h':
            display_help(general_commands)
        else:
            print(f'{user_ctrl} is unrecognized by the system, enter -h for help!')


main()
