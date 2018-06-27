from items import Food, Weapon


class Room:
    """
    Represents the rooms in the maze
    """

    def __init__(self, name: str, exits: list=None, monsters: list=None, items: list=None, is_end: bool=False):
        self._name = name
        self._exits = exits
        self._monsters = monsters if monsters else []
        self._items = items if items else []
        self._is_end = is_end

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return self._items

    @property
    def monsters(self):
        return self._monsters

    @property
    def exits(self):
        return self._exits

    @property
    def is_end(self):
        return self._is_end

    @is_end.setter
    def is_end(self, value):
        self._is_end = value

    def __str__(self):
        return self.name

    def print_items_in_room(self):
        """ Prints the items in the room """
        if not self.items:
            print('No items in the room.')
            return

        print('Items in room: {items}'.format(items=len(self.items)))
        for index, item in enumerate(self.items):
            print('{index}) {item} (weight - {weight}{health}{damage})'.format(
                index=index+1,
                item=item,
                weight=item.weight,
                health=', health - ' + str(item.health_points) if isinstance(item, Food) else '',
                damage=', bonus damage - ' + str(item.damage) if isinstance(item, Weapon) else ''
                )
            )

    def print_monsters(self):
        """ Prints the monsters in the room """
        if not self.monsters:
            print('There are no monsters in this room.')
            return

        monsters_alive = [monster for monster in self.monsters if not monster.is_dead]

        if not monsters_alive:
            print('All monsters in this room are already dead.')
            return
        else:
            for index, monster in enumerate(monsters_alive):
                print('{index}) {name} (health - {health})'.format(
                    index=index + 1,
                    name=monster.name,
                    health=monster.health,
                ))


class Exit:
    """
    Represents the exit/s from the rooms
    """

    def __init__(self, name: str, goes_to: Room=None, is_locked: bool=False):
        self._name = name
        self._goes_to = goes_to
        self._is_locked = is_locked

    @property
    def name(self):
        return self._name

    @property
    def goes_to(self):
        return self._goes_to

    @goes_to.setter
    def goes_to(self, value):
        self._goes_to = value

    @property
    def is_locked(self):
        return self._is_locked

    @is_locked.setter
    def is_locked(self, value):
        self._is_locked = value

    def __str__(self):
        return self.name
