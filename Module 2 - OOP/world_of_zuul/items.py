class Item:
    """ Represents the base item class """

    def __init__(self, name: str, weight: int):
        """ Constructor """
        self._name = name
        self._weight = weight

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def weight(self):
        return self._weight

    def __str__(self):
        return self.name


class Weapon(Item):
    """ Represents the weapons usable by the player """

    def __init__(self, name: str, weight: int, damage: int):
        """ Constructor """
        super().__init__(name, weight)
        self._damage = damage

    @property
    def damage(self):
        return self._damage


class Key(Item):
    """ Represents the keys, used by the player to open locked doors """

    def __init__(self, name: str, weight: int, unlocks_door=None):
        """ Constructor """
        super().__init__(name, weight)
        self._unlocks_door = unlocks_door

    @property
    def unlocks_door(self):
        return self._unlocks_door

    @unlocks_door.setter
    def unlocks_door(self, value):
        self._unlocks_door = value


class Food(Item):
    """ Represents food objects that player can eat to restore health points """

    def __init__(self, name: str, weight: int, health_points: int=2):
        """ Constructor """
        super().__init__(name, weight)
        self._health_points = health_points

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, points):
        self._health_points = points
