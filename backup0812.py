import random
min = 2
max = 12
maxroll = 10
maxboard = 50
player = 0
roll_number = 0


def new_game():
    print('Hope you ready to start!')


def script():
    print(
        "You are the tiniest cat with the biggest problem! "
        "After searching for fun birds and fish outside your comfort zone"
        "you got lost and now you can't find your way home!"
        "You are about to start an adventure to find your way back")
    print("You will begin by rolling a dice...")
    return input('Are you ready?')


def script2():
    print("You are starting {} blocks away from home and have {} days to get home.".format(maxboard, maxroll))
    print(
        "Each roll is one day."
        "Unexpected things may happen along the way..."
        "and while the number you roll will move you closer to home, some rolls may lead to trouble...")
    return input("Still feeling up for it?")


def yn(answer):
    if answer == 'Yes' or answer == 'yes':
        print("Great")
    else:
        print("Goodbye!")
        quit()


def roll_dice():
    global roll_number
    roll = random.randint(min, max)
    roll_number += 1
    if roll in (2, 3, 4, 5, 6, 8, 9, 10, 11):
        print('You rolled a {}'.format(roll))
        return roll
    elif roll == 12 or roll == 7:
        print('Uh oh! You rolled a {}'.format(roll))
        fight()
        return 0
    elif roll == 2:
        print(
            'You rolled a {}! You were attacked and eaten by zombie beavers'
            "That's too bad! Game over!".format(roll))
        return 0
        exit()


def move_player():
    global player
    player += roll_dice()
    if player <= maxboard:
        print('This is day {}. You have traveled {} blocks and you are {} blocks from home'.format(roll_number, player, maxboard-player))
    elif (player > maxboard):
        print(
            'Looks like you made it home safely! Go and have some catnips and'
            'treats! =^._.^=')


def iterate():
    keepgoing = True
    while keepgoing:
        play_again = input("You get to roll again. Ready?")
        if play_again == 'yes':
            move_player()
            keepgoing = (roll_number <= maxroll) and (player <= maxboard)

# negatives possible which is a bug!


def fight():
    global roll_number
    print('You are approached by a mangy cat with a chip on its shoulder.'
        'Roll a die to see what happens next!')
    input('Ready?')
    if 'yes':
        die1 = random.randint(1, 6)
    if die1 == 1:
        print('A tumbleweed tumbles on by and runs right into a cactusself.'
            'Both of you cats decide to back away.')
    elif die1 == 2:
        print('You escape! You are feeling very calm.'
            'You get an extra day to complete your journey!')
        roll_number -= 1
        #not working
    elif die1 == 3:
        print("The other cat wins! You are all scratched up and can't go home.")
        quit()
    elif die1 == 4:
        print('You both decide that you are too cute to fight.'
            'Meow! Meow! Lose a day while you take some beauty rest.')
        roll_number += 1
    elif die1 == 5:
        print(
            "All of a sudden, a giant piece of fish is thrown out a window."
            'You and the other cat decide to share it and part ways.'
            'Lose a day while you enjoy some fish.')
        roll_number += 1
    elif die1 == 6:
        print('This cat decides that it can get you home immediately! You win!')
        quit()


def main():
    new_game()
    answer1 = script()
    yn(answer=answer1)
    answer2 = script2()
    yn(answer=answer2)
    move_player()
    iterate()


if __name__ == '__main__':
    main()
