profession = 0
clicked = False
level = 0

def select_prof(prof):
    global profession, clicked
    profession = prof
    if profession == 1:
        clicked = True
    elif profession == 2:
        clicked = True
    elif profession == 3:
        clicked = True

def select_level(lvl):
    global level, clicked
    level = lvl
    if level == 1:
        clicked = True
    elif level == 2:
        clicked = True

def get_prof():
    return profession

def get_level():
    return level