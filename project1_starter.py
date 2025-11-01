"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Brittney Rouse
Date: October 27th, 2025

AI Usage: [Document any AI assistance used] 
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

    name = input("Enter your name: ")
    character_class = input("Enter your character class: ")
    character_level = int(input("Enter your character's level: "))
    strength_level = int(input("Enter your strength level: "))
    magic_level = int(input("Enter your magic level: "))
    health_points = int(input("Enter your health points: "))
    amount_of_gold = int(input("Enter your amount of gold: "))
    character = create_character(name, character_class)
    calculate_stats()
    character_dictionary = {"name": name, "class": character_class, "level": character_level, "strength": strength_level, "magic": magic_level, "health": health_points, "gold": amount_of_gold}

    return character_dictionary
    # Remember to use calculate_stats() function for stat calculation
    pass


def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    
        #Warrior: High strength, low magic, high health
        #Mage: Low strength, high magic, medium health
        #Rogue: Medium strength, medium magic, low health
        #Cleric: Medium strength, high magic, high health

    if character_level >= 90 and character_class == "Rogue":
        strength_level += 85
        magic_level += 45
        health += 50
        elif character_level >= 90 and character_class == "Cleric":
            strength_level += 50
            magic_level += 90
            health += 100
            elif character_level >= 90 and character_class == "Warrior":
                strength_level += 110
                magic_level += 10
                health += 140
                elif character_level >= 90 and character_class == "Mage":
                    strength_level += 40
                    magic_level += 80
                    health += 80
    elif character_level >= 70 and character_class == "Rogue":
        strength_level += 75
        magic_level += 35
        health += 45
        elif character_level >= 70 and character_class == "Cleric":
            strength_level += 40
            magic_level += 80
            health += 90
            elif character_level >= 70 and character_class == "Warrior":
                strength_level += 100
                magic_level += 8
                health += 130
                elif character_level >= 70 and character_class == "Mage":
                    strength_level += 35
                    magic_level += 70
                    health += 70
    elif character_level >= 50 and character_class == "Rogue":
        strength_level += 65
        magic_level += 25
        health += 40
        elif character_level >= 50 and character_class == "Cleric":
            strength_level += 30
            magic_level += 70
            health += 80
            elif character_level >= 50 and character_class == "Warrior":
                strength_level += 90
                magic_level += 6
                health += 120
                elif character_level >= 50 and character_class == "Mage":
                    strength_level += 30
                    magic_level += 60
                    health += 60
    elif character_level >= 30 and character_class == "Rogue":
        strength_level += 55
        magic_level += 15
        health += 35
        elif character_level >= 30 and character_class == "Cleric":
            strength_level += 20
            magic_level += 60
            health += 70
            elif character_level >= 30 and character_class == "Warrior":
                strength_level += 80
                magic_level += 4
                health += 110
                elif character_level >= 30 and character_class == "Mage":
                    strength_level += 25
                    magic_level += 50
                    health += 50
    elif character_level >= 10 and character_class == "Rogue":
        strength_level += 45
        magic_level += 5
        health += 30
        elif character_level >= 10 and character_class == "Cleric":
            strength_level += 5
            magic_level += 50
            health += 60
            elif character_level >= 10 and character_class == "Warrior":
                strength_level += 70
                magic_level += 2
                health += 100
                elif character_level >= 10 and character_class == "Mage":
                    strength_level += 20
                    magic_level += 40
                    health += 40
    elif character_level >= 1 and character_class == "Rogue":
        strength_level += 35
        magic_level += 0
        health += 25
        elif character_level >= 1 and character_class == "Cleric":
            strength_level += 1
            magic_level += 40
            health += 50
            elif character_level >= 1 and character_class == "Warrior":
                strength_level += 60
                magic_level += 0
                health += 90
                elif character_level >= 1 and character_class == "Mage":
                    strength_level += 15
                    magic_level += 30
                    health += 30
    elif character_level >= 1 and character_class == "Rogue":
        strength_level += 35
        magic_level += 0
        health += 25
        elif character_level >= 1 and character_class == "Cleric":
            strength_level += 1
            magic_level += 40
            health += 50
            elif character_level >= 1 and character_class == "Warrior":
                strength_level += 60
                magic_level += 0
                health += 90
                elif character_level >= 1 and character_class == "Mage":
                    strength_level += 10
                    magic_level += 20
                    health += 30
    elif character_level == 0 and character_class == "Rogue":
        strength_level += 30
        magic_level += 0
        health += 15
        elif character_level == 0 and character_class == "Cleric":
            strength_level += 0
            magic_level += 30
            health += 40
            elif character_level == 0 and character_class == "Warrior":
                strength_level += 50
                magic_level += 0
                health += 80
                elif character_level == 0 and character_class == "Mage":
                    strength_level += 5
                    magic_level += 10
                    health += 20

    stats = (strength_level, magic_level, health_points)
    return stats
    
    pass


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

    file_name = input()

    with open(file_name, "w") as filename:
    f.write("Character Name: ")
    f.write(character_name)
    f.write("\n")
    f.write("Class: ")
    f.write(character_class)
    f.write("\n")
    f.write("Level: ")
    f.write(str(character_level))
    f.write("\n")
    f.write("Strength: ")
    f.write(str(strength_level))
    f.write("\n")
    f.write("Magic: ")
    f.write(str(magic_level))
    f.write("\n")
    f.write("Health: ")
    f.write(str(health_points))
    f.write("\n")
    f.write("Gold: ")
    f.write(str(amount_of_gold))
    return True

    if not filename:
        return False

    return
    # Remember to handle file errors gracefully
    pass


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """

    if not os.path.exists:
        return None

    f = open(filename, "r")
    lines = f.readlines()
    character_dictionary = {}
    return character_dictionary

    # Remember to handle file not found errors
    pass


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

    print("=== CHARACTER SHEET ===")
    print(f"Name:" name)
    print(f"Class:" character_class)
    print(f"Level:" character_level)
    print(f"Strength:" strength_level)
    print(f"Magic:" magic_level)
    print(f"Health:" health_points)
    print(f"Gold:" amount_of_gold)
    
    pass


def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """

    character_level += 1
    calculate_stats()

    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
