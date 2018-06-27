from rooms import Room
from backpack import Backpack
from items import Weapon, Food, Key


class Creature:
    """
    Represents a base class for both players and monsters
    """

    def __init__(self, name: str, health: int, damage: int):
        """ Constructor """
        self._name = name
        self._health = health
        self._damage = damage
        self._is_dead = False

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if 0 < self._health <= 3 and isinstance(self, Player):
            print('Low health! You better find something to eat or you will die...')
        if self._health <= 0:
            self.is_dead = True

    @property
    def is_dead(self):
        return self._is_dead

    @is_dead.setter
    def is_dead(self, value):
        self._is_dead = value
        if self._is_dead and isinstance(self, Player):
            print('You died...')
            exit(0)

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    def attack(self, creature):
        """
        Attack given creature
        :param creature: target creature
        :return: None 
        """
        if isinstance(creature, Monster) and creature.is_dead:
            print('The monster is already dead.')
            return

        creature.health -= self.damage
        print('You hit the monster for {damage} damage.'.format(damage=self.damage))
        if creature.is_dead:
            if isinstance(creature, Player):
                print('You died...')
                exit(0)
            elif isinstance(creature, Monster):
                print('You killed the monster.')
        else:
            if isinstance(creature, Player):
                print('You still have {hp} health left.'.format(hp=creature.health))
            elif isinstance(creature, Monster):
                print('{monster} still has {hp} health left.'.format(monster=creature.name, hp=creature.health))


class Player(Creature):
    """
    Represents the player object, used by the actual player during the game
    """

    def __init__(self, name: str, health: int=10, damage: int=1, location: Room=None):
        """ Constructor """
        super().__init__(name, health, damage)
        self._location = location
        self._backpack = Backpack()
        self._equipped_item = None

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location
        if self._location.is_end:
            print('Well done! You survived and made your way out...')
            exit(0)

    @property
    def backpack(self):
        return self._backpack

    @property
    def equipped_item(self):
        return self._equipped_item

    @equipped_item.setter
    def equipped_item(self, value):
        self._equipped_item = value
        if self._equipped_item:
            self.damage += self._equipped_item.damage
        else:
            self.damage -= self._equipped_item.damage

    def eat(self, item: str=''):
        """
        Eats given food
        :param item: food to be eaten
        :return: None
        """
        if not item:
            print('Please, select food to eat.')
            return

        food = next(filter(lambda f: f.name.lower() == item, self.backpack.items), None)

        if not food:
            print('Specified food is not in your backpack.')
            return

        if not isinstance(food, Food):
            print('Specified item is not food.')
            return

        self.health += food.health_points
        self.backpack.drop_item(item=food, report=False)
        print('{food} consumed.'.format(food=food.name))
        self.status()

    def print_location_and_exits(self):
        """ Prints current location and possible exits """
        print('Current location: {location}'.format(location=self.location))
        print('Available exits:')
        for idx, ext in enumerate(self.location.exits):
            print('{idx}) {exit} leads to {room} - {is_locked}'.format(
                idx=idx + 1,
                exit=ext,
                room=ext.goes_to,
                is_locked='locked' if ext.is_locked else 'unlocked')
            )

    def pick_up_item(self, item: str=''):
        """
        Pick up an item
        :param item: item to be picked up
        :return: None
        """
        if not item:
            print('Please, choose an item to pick up.')
            return

        room_item = next(filter(lambda itm: itm.name.lower() == item, self.location.items), None)

        if not room_item:
            print('Specified item is not in the current room.')
            return

        if self.backpack.add_item(room_item):
            self.location.items.remove(room_item)

    def drop_item(self, item: str=''):
        """
        Drops or unequips an item
        :param item: item to be dropped / unequipped
        :return: None
        """
        if not item:
            print('Please, select an item from your backpack to drop.')
            return

        backpack_item = next(filter(lambda bp_item: bp_item.name.lower() == item, self.backpack.items), None)

        if not backpack_item:
            print('Specified item is not in your backpack.')
            return

        if self.equipped_item == backpack_item:
            self.equipped_item = None
            print('Item unequipped.')
            return

        self.backpack.drop_item(backpack_item)
        self.location.items.append(backpack_item)

    def equip(self, item: str=''):
        """
        Equips a weapon
        :param item: item to be equipped
        :return: None 
        """
        if not item:
            print('Please, select an item from your backpack to equip.')
            return

        backpack_item = next(filter(lambda bp_item: bp_item.name.lower() == item, self.backpack.items), None)

        if not backpack_item:
            print('Specified item is not in your backpack.')
            return

        if not isinstance(backpack_item, Weapon):
            print('Specified item is not a weapon.')
            return

        self.equipped_item = backpack_item
        print('{item} equipped.'.format(item=self.equipped_item.name))

    def print_currently_equipped_item(self):
        """ Prints the currently equipped item if any """
        if not self.equipped_item:
            print('No currently equipped item.')
            return

        print('Currently equipped item: {item}.'.format(item=self.equipped_item))

    def attack(self, monster):
        """
        Attacks given monster
        :param monster: monster to be attacked
        :return: None
        """
        if not monster:
            print('Please, select a monster to attack.')
            return

        monster_in_room = next(filter(lambda mon: mon.name.lower() == monster, self.location.monsters), None)

        if not monster_in_room:
            print('There is no such monster in the room.')
            return

        super(Player, self).attack(monster_in_room)

    def unlock_door(self, door: str=''):
        """
        Unlocks the door if the player has a suitable key in the backpack 
        :param door: door to be unlocked
        :return: None
        """
        if not door:
            print('Please, select a door to unlock.')
            return

        if self.__check_for_monsters():
            return

        door_in_room = next(filter(lambda dr: dr.name.lower() == door, self.location.exits), None)

        if not door_in_room:
            print('There is no such door in the current room.')
            return

        has_key = next(filter(lambda k: isinstance(k, Key) and k.unlocks_door == door_in_room, self.backpack.items), None)

        if not has_key:
            print('You do not have the key for that door.')
            return

        if not door_in_room.is_locked:
            print('The door is not locked.')
            return

        door_in_room.is_locked = False
        print('Door unlocked.')

    def go_to_room(self, room: str=''):
        """
        Changes player's current location to the given one
        :param room: target location
        :return: None
        """
        if not room:
            print('Please, select a room to go to.')
            return

        if self.__check_for_monsters():
            return

        target_exit = next(filter(lambda ext: ext.goes_to.name.lower() == room, self.location.exits), None)

        if not target_exit:
            print('None of the exists in the current room leads to {room}.'.format(room=room))
            return

        if target_exit.is_locked:
            print('The exit to the room is locked.')
            return

        self.health -= 1
        self.location = target_exit.goes_to
        self.print_location_and_exits()

    def __check_for_monsters(self):
        """ Check if there are still monsters in the current location """
        if any(not monster.is_dead for monster in self.location.monsters):
            number_of_monsters = len(list(filter(lambda mon: not mon.is_dead, self.location.monsters)))
            if number_of_monsters == 1:
                print('There is still one monster on your way. You need to kill it before you can proceed.')
            else:
                print('There are still {monsters} monsters on your way.'.format(monsters=number_of_monsters))

            return True
        return False

    def status(self):
        """ Reports player's current health """
        print('Health: {hp}.'.format(hp=self.health))


class Monster(Creature):
    """
    Represents the monsters that the player will have to fight during the game
    """

    def __init__(self, name: str, health: int=5, damage: int=1):
        """ Constructor """
        super().__init__(name, health, damage)
