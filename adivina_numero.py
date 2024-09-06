import random

# This game just works for numbers between 1 and 10(eventually)

print('\n======================================')
print(' WELCOME TO THE GUESS THE NUMBER GAME')
print('======================================\n')

answer_user = input('Do you want to play?(Y/N)\n')

while True:

    if answer_user.upper() == 'Y':

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random_number = random.choice(numbers)
        lives = 3

        print('\nAll right! Let\'s get started!\n'.upper())
        print('You\'ll have three lives, so choose wisely')
        print('I\'m gonna give you a clue.\nI\'m thinking in a number between 1 and 10\n')

        while lives != 0:

            choice = int(input('Enter a number:'))

            if choice == random_number:
                print('You got this')
                answer_user = input('Do you want to try another one?(Y/N)\n')
                break
            else:
                print('You\'re wrong')
                lives -= 1
        else:
            print('You have no lives')
            answer_user = input('Do you want to try again?(Y/N)\n')
    else:
        print('Thanks for playing')
        break
