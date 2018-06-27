from items import Item, Food, Weapon


class Backpack:
    """
    The backpack is used by the player to store found items
    """

    def __init__(self, max_slots: int=5, max_weight: int=10):
        """ Constructor """
        self._max_slots = max_slots
        self._max_weight = max_weight
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item: str=''):
        """
        Adds the item to the backpack
        :param item: item to be added to the backpack
        :return: True on success / False on failure
        """
        if len(self.items) >= self._max_slots:
            print("Inventory is full. You can't pick up more items.")
            return False

        if sum([item.weight for item in self._items]) + item.weight > self._max_weight:
            print("Backpack is too heavy. You can't pick up more items.")
            return False

        self._items.append(item)
        print('Item picked up: {item}'.format(item=item.name))
        self.__report_space_and_weight_left()
        return True

    def drop_item(self, item: Item='', report: bool=True):
        """
        Drops the item from the backpack or unequips an equipped item
        :param item: item to be dropped or unequipped
        :param report: reports available backpack space
        :return: None
        """
        self._items.remove(item)
        if report:
            print("Item dropped: {item}".format(item=item.name))
            self.__report_space_and_weight_left()

    def __item_can_fit(self, item: str=''):
        """
        Checks if the item can fit inside the backpack
        :param item: item to be checked
        :return: True / False
        """

        has_available_slots = len(self._items) < self._max_slots
        current_weight = sum((item.weight for item in self._items))
        weight_fits = current_weight + item.weight <= self._max_weight

        if not has_available_slots:
            print('Inventory is full.')
            return False
        elif not weight_fits:
            print('Backpack is too heavy. You need to drop something.')
            return False

        return True

    def __report_space_and_weight_left(self):
        """
        Reports the currently available number of slots in the backpack
        and available weight left
        :return: None 
        """
        slots_left = self._max_slots - len(self._items)
        weight = self._max_weight - sum((item.weight for item in self._items))
        print('Backpack slots available: {slots}'.format(slots=slots_left))
        print('Available weight: {weight}'.format(weight=weight))

    def print_items_in_backpack(self):
        """ Prints the items in the backpack """
        if not self.items:
            print('No items in the backpack.')
            return

        print('Items in backpack: {items}'.format(items=len(self.items)))
        for index, item in enumerate(self.items):
            print('{index}) {item} (weight - {weight}{health}{damage})'.format(
                index=index + 1,
                item=item,
                weight=item.weight,
                health=', health - ' + str(item.health_points) if isinstance(item, Food) else '',
                damage=', bonus damage - ' + str(item.damage) if isinstance(item, Weapon) else ''
                )
            )
