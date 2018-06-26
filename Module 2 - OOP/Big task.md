# Big task - end of OOP

## World of Zuul

Implement a command-line interpretation of the game.

The entire game should consist of a player, that has a name and can move around in a maze. The maze consists of rooms with exists. Each room can have multiple exits. The player can go from one room to another.

There could be certain items in each room - a sword, a bomb, a banana etc. The player has a backpack that can contain a certain amount of items depending on the item weight, so the player can pick up an item in each room, but he can also drop one to pick up another.

### General requirements

* Good class hierarchy and application of OO principles.
* Commands:
  * `help` - prints the list of commands
  * `location` - prints out the current player location and the list of exits
  * `go to "room name"` - player will move to the exit that connects the current room with the "room name" and will execute the `location` command
  * `items` - prints out the list of items in the backpack
  * `pick up "item name"` - will pickup the item and execute the `items` command
  * `drop "item name"` - will drop the item and execute the `items` command
  * `quit` - exits the game

### Optional requirements

* The player has a health status and the more he walks around the more he loses
* some rooms contain monsters and player may fight them
* some exits are impossible to pass unless the player has a key
* some exits have to be broken given that the player has a specific item

*Note*: If there is anything open for interpretation you may make a choice.