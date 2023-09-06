def roll_call_dwarves(dwarves):
    i=1
    for dwarf in dwarves:
        print(f"{i}. {dwarf}")
        i += 1

def summon_captain_planet(calls):
    capitalized_calls = []
    for call in calls:
        capitalized_call = call.capitalize() + "!"
        capitalized_calls.append(capitalized_call)
    return capitalized_calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(ingredients):
    for ingredient in ingredients:
        if ingredient == ("cheddar" or "gouda" or "camembert"):
            return ingredient
    return None
