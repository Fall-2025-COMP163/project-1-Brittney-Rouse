"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Brittney Rouse
Date: October 27th, 2025

AI Usage: I used ChatGPT to help me debug this upon failing the tests in Github. While there are comments showing where and what went wrong, I'll put the gist here as well:
    - Helped with variables not being available outside their local function (forgot to set a variable outside of the function)
    - Helped with arguements being forgotten (my various issues with calling "calculate_stats")
    - Helped with code that was ineffective.
    - MAJOR rework of the save_character() function.
Example: AI helped with file I/O error handling logic in save_character function
"""

import os


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """

    #Removed almost everything in this section due to ChatGPT's suggestions - I forgot that this only needed the user's name and character class, not every other stats.
    #I then forgot, again, that these variables are defined when the function is called. This is the second time I forgot this in this project alone.

    #I, AGAIN, forgot to provide the arguements within the calculate_stats() function.
    #ChatGPT also helped me with calling the stat calculations here (it's simple, but I just did it wrong).
    level = 1
    gold = 100
    strength, magic, health = calculate_stats(character_class, level)
    character_dictionary = {"name": name, "class": character_class, "level": level, "strength": strength, "magic": magic, "health": health, "gold": gold}

    return character_dictionary
    # Remember to use calculate_stats() function for stat calculation


def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    
        #Warrior: High strength, low magic, high health
        #Mage: Low strength, high magic, medium health
        #Rogue: Medium strength, medium magic, low health
        #Cleric: Medium strength, high magic, high health

        #Okay, so ChatGPT helped me do a complete rehaul of this function - I originally had a LOT of nesting if-else statements that would change the amount
        #that the stats were changed by depending on the original level (This was before I realized that it always starts at character level one - oops), and
        #I actually really liked it before realizing it would not work with this project. And so, this was made : Much simpler, does not depened on the starting level
        #(as the starting level is always one), or the current level in general (at least, not in the way it did before). So I definitely understand why it was
        #changed! This is much simpler and better for the project.

    base_strength = 5
    base_magic = 3
    base_health = 15
    
    if character_class == "Warrior":
        strength = base_strength + level * 5
        magic = base_magic + level * 2
        health = base_health + level * 5
    elif character_class == "Mage":
        strength = base_strength + level * 2
        magic = base_magic + level * 5
        health = base_health + level * 3
    elif character_class == "Rogue":
        strength = base_strength + level * 3
        magic = base_magic + level * 3
        health = base_health + level * 2
    elif character_class == "Cleric":
        strength = base_strength + level * 3
        magic = base_magic + level * 5
        health = base_health + level * 5

    return strength, magic, health


def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """

    #Debugging with ChatGPT - put filename = input() before. This is incorrect, since the filename is called in the function.
    #Also misspelled it as "file_name".
    #Also also - formatted better with the help of ChatGPT (previously had the different parts of the sentence on different lines - weird to look
    #at, and this behaves the same, if not better).
    with open(filename, "w") as f:
        f.write(f"Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")
    return True

    if not filename:
        return False

    return
    # Remember to handle file errors gracefully


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """

    #ChatGPT help - previously forgot parenthesees (and contents within them)
    if not os.path.exists(filename):
        return None

    #ChatGPT helped me with this whole little section - it was just NOT working for me! So now, this is written with the help of ChatGPT.
    character = {}
    for line in lines:
        key, value = line.strip().split(": ")
        if key in ["Level", "Strength", "Magic", "Health", "Gold"]:
            value = int(value)
        character[key.lower()] = value

    # Remember to handle file not found errors


def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """

    #HUGE thing I forgot that ChatGPT picked up - I was not using the DICTIONARY ENTRIES when doing this code;
    #I wrote things down as if they were variables - which they are obviously not.
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character["name"}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character["magic"}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """

    #Previously forgot to put the arguments within "calculate_stats". I realized this when debugging with ChatGPT.
    #Same thing that happened in the display_character function - I forgot to use the DICTIONARY entry (I put it as a
    #variable again :(
    character['level'] += 1
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health

    # Remember to recalculate stats for the new level


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
