def roll_call_dwarves(dwarves):
    for x in range(len(dwarves)):
        print(f"{x + 1}. {dwarves[x]}")

def summon_captain_planet(elements):
    new_list = []
    for el in elements:
        new_list.append(el.title() + '!')
    return new_list

def long_planeteer_calls(elements):
    for el in elements:
        if len(el) > 4:
            return True
    return False

def find_the_cheese(elements):
    for el in elements:
        if el == 'cheddar':
            return el
