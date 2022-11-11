import random

def MonsterGen():
    num = random.randrange(0,100)

    if num <20:
        print("a skeleton appears")

    elif num < 50:
        print("a spider appears")
    elif num <75:
        print("a zombie appears")
    else:
        print("a witch appears")

MonsterGen() #function call
