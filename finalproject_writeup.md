# Final Project

## You should include a markdown file with a one page write up how you made your game. This should include anything you might have struggled with and how you overcame these challenges as well as what you are most proud of from a technical standpoint. Also be sure to include instructions for the users for how to play your game.

I created my final project to rely heavily on the concepts/tools that we learned in class. 
Since I wanted to make it light and fun, I decided to make a “board game” of a cat that needs to find its way home. 
To keep an element of surprise in the game, the game would revolve around dice – and that:
1) rolls would move a player along a board (like in Candy Land!)
2) specific rolls would lead to fights (involving a die)
3) landing on a specific “board square” would lead to events (also involving a die)

Once I had the basic framework of the game in mind, I went about mapping out the functions that I would need to create the game. 
The first function I created was a simple dice function, but then added a “while loop” to keep it running until specific conditions were met. 
Obviously, when I ran this on the terminal, it kept running until it reached those conditions. 
This made me quickly realize that I needed to add in a user-controlled prompt to stop/begin this loop. 
I then created the player variable, which functions as the board – the player is essentially “zero”; 
dice rolls are added to the player so that the player "moves" along the "board" to reach home. 
Since I needed other conditions to make the game interesting, I decided that each roll needed to be a day – so I added that variable as well. 
After that, I spent much time adding in conditionals for fights/events, and breaking up one bigger function into the ‘move_player’ and ‘iterate’ functions to accommodate the many conditionals! 
The bulk of my code is comprised of the ‘roll_dice’, ‘move_player’, and ‘iterate’ functions – and they all build off one another.
I then spent time cleaning up my code by moving most numbers to the top and setting them as variables. This made changing the conditions of the game easier. 
Finally, my last step was making everything look prettier – I added in “/n” and tried to get rid of all the red dots in my code.

My proudest technical achievement was navigating the functions within functions so that the game ran smoothly. 
However, my functions definitely could have been simpler—this is just how I got the game to work! 

Overall, creating this game was an iterative process. 
It now seems pretty simple and straightforward, but I had to spend much time thinking through and executing the logic. 
Often, I would open a Jupyter notebook to run a function to test through mistakes. 
(Example: I spent ~ one ~ hour discovering that if I had ‘Return’ in part of a conditional (after an if), I would need it after the other part of the conditional (after an elif).)
At times, when I wanted to test the logic, I made the maxboard equal 10 (or something small) or the max days equal 2 (or something small).

It's fun to create games!

