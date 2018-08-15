import random
min = 2
max = 12
maxroll = 10
maxboard = 50
player = 0
roll_number = 0
event_blocks = (5, 10, 15, 20, 25, 30, 35, 40, 45)
roll_dict = {
    'normal': [3, 4, 5, 6, 8, 9, 10, 11],
    'fight': [7, 12],
    'death': [2]
}
bad_input = ('Hmm...maybe something is lost in CATranslation? Type quit if you'
             ' want to exit or yes (or y) if you want to continue\n')
# script function


def script():
    print(
        "\nYou are the tiniest cat with the biggest problem!\n"
        "You just got lost after chasing butterflies far from home!\n"
        "You are about to start an adventure to find your way back.\n")
    print("You will begin by rolling dice (rolling 2 - 12!)...")
    print(
         "You are starting {} blocks away from home and have {} days to get "
         "back.\n".format(maxboard, maxroll))
    print(
        "Each roll is one day.\n"
        "Beware: unexpected things may happen along the way."
        " While the number you roll will likely move you closer to home,"
        " some numbers you roll may lead to trouble...\n "
        "...AND you also want to watch out for busy blocks!\n")
    answer_script = input("Are you ready? (For this game, enter y or yes"
                          " to keep playing and quit or no to leave. Meow.\n")
    if answer_script.lower() in ('yes', 'y'):
        print("Great")
    elif answer_script.lower() in ('no', 'n', 'quit', 'q'):
        quit_game()
    else:
        print(bad_input)
        script()

# quit function


def quit_game():
    print('Okay! Hope you play again sometime! Goodbye! Meow Meow')
    quit()

# roll dice function - used to roll but also to set certain numbers as fights


def roll_dice():
    global roll_number
    roll = random.randint(min, max)
    roll_number += 1
    if roll in roll_dict['normal']:
        print('You rolled a {}'.format(roll))
        return roll
    elif roll in roll_dict['fight']:
        print('Uh oh! You rolled a {}'.format(roll))
        fight()
        return 0
    elif roll in roll_dict['death']:
        print(
            'You rolled a {}! You were attacked and eaten by zombie beavers\n '
            "That's too bad! Game over!".format(roll))
        quit()

# function to move player


def move_player():
    global player
    player += roll_dice()
    if player < maxboard and (player not in event_blocks):
        print("This is day {}. You have traveled {} blocks and you are {}"
              " blocks from home".format(roll_number, player, maxboard-player))
    elif player < maxboard and (player in event_blocks):
        print('You just stumbeled on to block {}!'.format(player))
        print('\nReminder: this is day {}. You are {} blocks from home'.format(
            roll_number, maxboard-player))
        event_block()
    elif (player >= maxboard):
        print(
            'Looks like you made it home safely! Go and have some catnips and '
            'treats! =^._.^=')
        quit_game()

# function to iterate through move player - move dice


def iterate():
    keepgoing = True
    while keepgoing:
        play_again = input("You get to roll again. Ready?\n")
        if play_again.lower() in ('yes', 'y'):
            move_player()
            keepgoing = (roll_number < maxroll) and (player < maxboard)
        elif play_again.lower() in ('no', 'n', 'quit', 'q'):
            quit_game()
        else:
            print(bad_input)
            iterate()
    print("You didn't make it home in time! Meeeorrrwwww =^x.x^=")
    quit()
# okay to call function in function?

# two fuctions below - fight and event define what happens with specific rolls
# and when you land on specific blocks


def fight():
    global roll_number
    print('You are approached by a mangy cat with a chip on its shoulder. '
          'Roll a die to see what happens next!')
    response_fight = input('Ready?\n')
    if response_fight.lower() in ('yes', 'y'):
        die1 = random.randint(1, 6)
        if die1 == 1:
            print('A tumbleweed tumbles on by and runs right into a cactus.'
                  ' Both of you cats decide to back away.')
        elif die1 == 2:
            print('You escape! You are feeling very calm.'
                  ' You get an extra day to complete your journey!')
            roll_number -= 1
        elif die1 == 3:
            print("The other cat wins! You are all scratched up and can't"
                  " go home. You lose!")
            quit()
        elif die1 == 4:
            print('You both decide that you are too cute to fight.'
                  ' Meow! Meow! Lose a day while you take some beauty rest.')
            roll_number += 1
        elif die1 == 5:
            print(
                "All of a sudden, a giant fish is thrown out a window."
                ' You and the other cat decide to share it and part ways.'
                ' Lose a day while you enjoy a tasty treat.')
            roll_number += 1
        elif die1 == 6:
                print('This cat decides that it can get you home immediately!'
                      ' You win!')
                quit()
    elif response_fight.lower() in ('no', 'n', 'quit', 'q'):
        quit_game()
    else:
        print(bad_input)
        fight()


def event_block():
    global player
    print('On this block, there are many stores and humans.'
          ' Who knows what can happen in this choas!'
          ' Try your luck with a roll of a die\n')
    event_response = input('Ready?\n')
    if event_response.lower() in ('yes', 'y'):
        die2 = random.randint(1, 6)
        if die2 == 1:
            print('A helpful human shows you a shortcut - move 3 additional'
                  ' blocks immediately')
            player += 3
        elif die2 == 2:
            print('Dog herd!! You are chased back 5 blocks!')
            player -= 5
        elif die2 == 3:
            print('Elmyra Duff finds you so cute and decides to take you home.'
                  ' Sorry you lose!!')
            quit_game()
        elif die2 == 4:
            print('Nothing happens')
        elif die2 == 5:
            print('With many humans in your way you get lost! Lose 3 blocks')
            player -= 3
        elif die2 == 6:
            print("Someone gave you some cat treats!"
                  " This won't help you get home, but you sure feel better")
    elif event_response.lower() in ('no', 'n', 'quit', 'q'):
        quit_game()
    else:
        print(bad_input)
        event_block()


def main():
    script()
    move_player()
    iterate()


if __name__ == '__main__':
    main()
