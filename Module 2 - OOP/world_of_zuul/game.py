from collections import OrderedDict
from creature import Player, Monster
from rooms import Room, Exit
from items import Key, Food, Weapon

PLAYER = None

COMMANDS = OrderedDict(
    [
        ('help', '- help - prints the list of commands'),
        ('location', '- location - prints your current location and possible exits'),
        ('status', '- status - prints player\'s health'),
        ('go to', '- go to "Room name" - you\'ll go through the exit that connects the current room with the "Room name" and will execute the \'location\' command. Each time you move, you lose health.'),
        ('items', '- items - prints out a list of items in the backpack'),
        ('pick up', '- pick up "item name" - you will pick up the item and execute the \'items\' command'),
        ('drop', '- drop "item name" - you will drop or unequip the item and execute the \'items\' command'),
        ('unlock', '- unlock "exit name" - unlocks the exit if you have the respective key'),
        ('eat', '- eat "item name" - you will eat the food, restore health and execute the \'items\' command'),
        ('equip', '- equip "item name" - you will equip the item and will be able to cause more damage to monsters'),
        ('monsters', '- monsters - prints out a list of alive monsters in the room'),
        ('attack', '- attack "monster name" - you will attack the monster'),
        ('quit', '- quit - exits the game'),
    ]
)

ROOMS = {
    'dark_room': Room(name='Dark room',
                      exits=[Exit(name='Wooden door', goes_to=None, is_locked=False)],
                      monsters=None,
                      items=[Food(name='Half-rotten apple', weight=1, health_points=1)]),
    'long_hall': Room(name='Long hall',
                      exits=[
                          Exit(name='Wooden door', goes_to=None, is_locked=False),
                          Exit(name='Prison cell door', goes_to=None, is_locked=True),
                          Exit(name='Rusty iron gate', goes_to=None, is_locked=True)
                      ],
                      monsters=[
                          Monster(name='Venomous spider', health=5, damage=1)
                      ],
                      items=[Key(name='Prison key', weight=1, unlocks_door=None)]),
    'prison_cell': Room(name='Prison cell',
                        exits=[Exit(name='Prison cell door', goes_to=None, is_locked=False)],
                        monsters=[
                            Monster(name='Frenzied boar', health=6, damage=2),
                            Monster(name='Ferocious wolf', health=4, damage=2),
                        ],
                        items=[
                            Key(name='Rusty iron key', weight=1, unlocks_door=None),
                            Weapon(name='Sharp axe', weight=6, damage=2),
                            Food(name='Leftovers', weight=2, health_points=2),
                        ]),
    'stairway': Room(name='Stairway',
                     exits=[
                         Exit(name='Rusty iron gate', goes_to=None, is_locked=False),
                         Exit(name='Terrace stairs', goes_to=None, is_locked=True)
                     ],
                     monsters=[
                         Monster(name='Bloodfury harpy', health=4, damage=2),
                         Monster(name='Killer croc', health=5, damage=3)
                     ],
                     items=[
                         Key(name='Terrace key', weight=1, unlocks_door=None),
                     ]),
    'terrace': Room(name='Terrace',
                    exits=[Exit(name='Terrace stairs', goes_to=None, is_locked=False)],
                    monsters=None,
                    items=None,
                    is_end=True)
}


def print_help():
    """ Prints help with all available commands """
    for help_msg in COMMANDS.values():
        print(help_msg)


def print_start_msg():
    """ Prints start message """
    msg = """
        You wake up in a dark room...
        All you can see is an empty backpack and a door.
        You equip the backpack and you're ready for the adventure.
        (If you're stuck, type "help" to get a list of commands)
        (Hint: All commands and names in the game are case-insensitive)
        """
    print(msg)


def init_world():
    """
    Initializes the player and connects game objects
    :return: None 
    """
    global PLAYER, ROOMS

    PLAYER = Player(name='Player', location=ROOMS['dark_room'])

    ROOMS['dark_room'].exits[0].goes_to = ROOMS['long_hall']

    ROOMS['long_hall'].exits[0].goes_to = ROOMS['dark_room']
    ROOMS['long_hall'].exits[1].goes_to = ROOMS['prison_cell']
    ROOMS['long_hall'].exits[2].goes_to = ROOMS['stairway']
    ROOMS['long_hall'].items[0].unlocks_door = ROOMS['long_hall'].exits[1]

    ROOMS['prison_cell'].exits[0].goes_to = ROOMS['long_hall']
    ROOMS['prison_cell'].items[0].unlocks_door = ROOMS['long_hall'].exits[2]

    ROOMS['stairway'].exits[0].goes_to = ROOMS['long_hall']
    ROOMS['stairway'].exits[1].goes_to = ROOMS['terrace']
    ROOMS['stairway'].items[0].unlocks_door = ROOMS['stairway'].exits[1]

    ROOMS['terrace'].exits[0].goes_to = ROOMS['stairway']


def get_user_command():
    """
    Handles the user input
    :return: Tuple - command, item 
    """
    command = ''
    item = ''
    user_input = input('Enter a command: ')
    user_input = user_input.lower().strip()

    if user_input:
        for key in COMMANDS.keys():
            if key in user_input:
                command = key
                rest_input = user_input[len(key):].strip().strip('"').strip("'")
                if rest_input:
                    item = rest_input

    return command, item


def execute_command(command: str='', item: str=''):
    """
    Executes the command, entered by the user
    :param command: the command, entered by the user 
    :param item: the item, entered by the user
    :return: None 
    """
    if command == 'help':
        print_help()
    elif command == 'location':
        PLAYER.print_location_and_exits()
    elif command == 'status':
        PLAYER.status()
    elif command == 'go to':
        PLAYER.go_to_room(item)
    elif command == 'items':
        PLAYER.print_currently_equipped_item()
        PLAYER.backpack.print_items_in_backpack()
        PLAYER.location.print_items_in_room()
    elif command == 'pick up':
        PLAYER.pick_up_item(item)
    elif command == 'drop':
        PLAYER.drop_item(item)
    elif command == 'eat':
        PLAYER.eat(item)
    elif command == 'equip':
        PLAYER.equip(item)
    elif command == 'unlock':
        PLAYER.unlock_door(item)
    elif command == 'monsters':
        PLAYER.location.print_monsters()
    elif command == 'attack':
        PLAYER.attack(item)
    elif command == 'quit':
        print('Thank you for playing! See you soon!')
        exit(0)
    else:
        print("Unknown command. You can type 'help' for a list of commands.")


def start():
    """
    Starts and runs the game, according to the user's actions
    :return: None 
    """
    init_world()
    print_start_msg()

    while True:
        command, item = get_user_command()
        execute_command(command, item)
