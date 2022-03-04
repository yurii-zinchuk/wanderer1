"""Module with classes representing objects in the game."""


class Room:
    """
    A class to represent a separate room in the game.

    ...

    Attributes
    ----------
    name : str
        name of the room
    description : str
        description of the room. Defaults to None
    linked_to : list
        list of ther rooms this room is linked to. Defaults to []
    character : object
        character located in the room. Defaults to None
    item : object
        item located int he room. Defaults to None

    Methods
    -------
    set_description(rdescription):
        Set room's description to a passed string.
    link_room(__o, side):
        Add a room this room is linked with.
    get_details():
        Print info about the room.
    set_character(__o):
        Place character inside the room.
    set_item(__o):
        Place item inside the room.
    get_character():
        Retrun character located in the room.
    get_item():
        Return item located in the room.
    move(direction):
        Change rooms in passed direction.
    """

    def __init__(self, rname: str) -> None:
        """Define class instance.

        Args:
            rname (str): Room name.
        """
        self.name = rname
        self.description = None
        self.linked_to = []
        self.character = None
        self.item = None

    def set_description(self, rdescription: str) -> None:
        """Set room's description.

        Args:
            rdescription (str): The description.
        """
        self.description = rdescription

    def link_room(self, __o: object, side: str) -> None:
        """Set room's relations to other rooms in the game.

        Args:
            __o (object): Other room object to
            side (str): Direction where other room is related to the room.
        """
        self.linked_to.append((__o, side))

    def get_details(self) -> None:
        """Print info about the room.
        Includes name, description and all neighbouring
        rooms with their directions.
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for neighbour in self.linked_to:
            print(f'The {neighbour[0].name} is {neighbour[1]}')

    def set_character(self, __o: object) -> None:
        """Set a character inside the room.

        Args:
            __o (object): The character.
        """
        self.character = __o

    def set_item(self, __o: object) -> None:
        """Set an item inside the room.

        Args:
            __o (object): The item.
        """
        self.item = __o

    def get_character(self) -> object:
        """Return character from the room.

        Returns:
            object: Character that was set inside this room.
        """
        return self.character

    def get_item(self) -> object:
        """Return item from the room.

        Returns:
            object: Item that was set inside this room.
        """
        return self.item

    def move(self, direction: str) -> object:
        """Change room where the player is located.

        Args:
            direction (str): Direction of the new room.

        Returns:
            object: New room where the player goes.
        """
        found = False
        for room, side in self.linked_to:
            if side == direction:
                found = True
                return room
        if not found:
            print(f'No room in {direction}')
            return None


class Item:
    """
    A class ot represent an item in the game.

    ...

    Attributes
    ----------
    name : str
        name of the item
    description : str
        description of the item

    Methods
    -------
    set_description(idescription):
        Set item's description to a passed string.
    get_name():
        Return the item's name.
    describe():
        Print info about the item.
    """

    def __init__(self, iname: str) -> None:
        """Define class instance.

        Args:
            iname (str): Item name.
        """
        self.name = iname
        self.description = None

    def set_description(self, idescription: str) -> None:
        """Set item's description.

        Args:
            idescription (str): The description.
        """
        self.description = idescription

    def get_name(self) -> str:
        """Return item's name.

        Returns:
            str: Item name.
        """
        return self.name

    def describe(self) -> None:
        """Print info about the item.
        Includes name and description.
        """
        print(f'The [{self.name}] is here - {self.description}')


class Character:
    """
    A class to represent a character in the game.

    ...

    Attributes
    ----------
    name : str
        name of the character
    description : str
        description of the character
    conversation : str
        lines that character tells when asked to. Defaults to None
    enemy : bool
        whether the character is the enemy. Defaults to False

    Methods
    -------
    set_conversation(cconversation):
        Set what character will say.
    describe():
        Print info about the character.
    talk():
        Print what the character says.
    """

    def __init__(self, cname: str, cdescription: str) -> None:
        """Define class instance.

        Args:
            cname (str): Character name.
            cdescription (str): Character description.
        """
        self.name = cname
        self.description = cdescription
        self.conversation = None
        self.enemy = False

    def set_conversation(self, cconversation: str) -> None:
        """Set what character says to a passed string.

        Args:
            cconversation (str): Character's lines.
        """
        self.conversation = cconversation

    def describe(self) -> None:
        """Print info about the character.
        Includes name and description.
        """
        print(f'{self.name} is here!')
        print(f'{self.description}')

    def talk(self) -> None:
        """Print character's conversation.
        """
        print(f'[{self.name} says]: {self.conversation}')


class Enemy(Character):
    """
    A class to represent an enemy in the game.
    Inherits from Character.

    ...

    Attributes
    ----------
    name : str
        name of the character
    description : str
        description of the character
    conversation : str
        lines that character tells when asked to. Defaults to None
    enemy : bool
        whether the character is the enemy. Defaults to True
    weakness : str
        what can defeat the enemy. Defaults ot None

    Methods
    -------
    set_weakness(cweakness):
        Set weakness of the enemy to a passed string.
    fight(weapon):
        Check if passed item defeats the enemy.
    get_defeated():
        Return amount of defeated enemies.
    """

    victories = 0

    def __init__(self, cname: str, cdescription: str) -> None:
        """Define class instance.

        Args:
            cname (str): Character name.
            cdescription (str): Character description.
        """
        super().__init__(cname, cdescription)
        self.weakness = None
        self.enemy = True

    def set_weakness(self, eweakness: str) -> None:
        """Set enemies weakness. That is the item that defeats the enemy.

        Args:
            eweakness (str): Enemy weakness.
        """
        self.weakness = eweakness

    def fight(self, weapon: str) -> bool:
        """Return True if passed item defeats the enemy, False otherwise.

        Args:
            weapon (str): Item to try.

        Returns:
            bool: Whether defeats.
        """
        if weapon == self.weakness:
            print(f'You fend {self.name} off with the {weapon}')
        else:
            print(f'{self.name} crushes you, puny adventurer!')
        return weapon == self.weakness

    def get_defeated(self) -> int:
        """Increment amount of defeated enemies and return it.

        Returns:
            int: Amount of defeated enemies.
        """
        Enemy.victories += 1
        return Enemy.victories


class Friend(Character):
    """
    A class to represent a Friend in the game.
    Inherits from Character.

    ...

    Attributes
    ----------
    name : str
        name of the character
    description : str
        description of the character
    conversation : str
        lines that character tells when asked to. Defaults to None
    enemy : bool
        whether the character is the enemy. Defaults to False
    """

    def __init__(self, cname: str, cdescription: str) -> None:
        """Define class instance.

        Args:
            cname (str): Character name.
            cdescription (str): Character description.
        """
        super().__init__(cname, cdescription)
