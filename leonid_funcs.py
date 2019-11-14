import os

def author_info():
    return 'Leonid Orlov'

def filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    return result

def separator(count=30):
    return '*' * count


def is_correct_choice(choice, menu_items ):
    return choice.isdigit() and int(choice) > 0 and int(choice) <= len(menu_items)
