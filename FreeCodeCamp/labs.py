full_dot = '●'
empty_dot = '○'


def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        print('The character name should be a string')
    elif character_name == "":
        print('The character should have a name')
    elif len(str(character_name)) > 10:
        print('The character name is too long')
    elif character_name.isspace():
        print('The character name should not contain spaces')

    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        print('All stats should be integers')
    elif not (strength >= 1 and intelligence >= 1 and charisma >= 1):
        print('All stats should be no less than 1')
    elif (strength > 4 and intelligence > 4 and charisma > 4):
        print('All stats should be no more than 4')
    elif strength + intelligence + charisma != 7:
        print('The character should start with 7 points')

    info = f"""{character_name}
STR {(strength * full_dot) + ((10 - strength) * empty_dot)}
INT {(intelligence * full_dot) + ((10 - intelligence) * empty_dot)}
CHA {(charisma * full_dot) + ((10 - charisma) * empty_dot)}
"""

    print(info)


create_character(True, 4, 2, 1)
