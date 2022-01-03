from art import logo, vs
from game_data import data
import random, os

CURRENT_PAIR = []

def disassembly_dict(dict):
    """
    Unpacks a dictionary, prints values and returns followage_count.
    """
    name = dict["name"]
    desc = dict["description"]
    country = dict["country"]
    count = dict["follower_count"]
    print(f"Compare: {name}, a {desc}, from {country}.")
    return count

def initialize(logo_init, data_init):
    """
    Chooses two random dictionaries from data.py and returns followage_count of both
    as a tuple.
    """
    print(logo)
    random.shuffle(data)
    choice_a = data.pop()
    count_a = disassembly_dict(choice_a)
    print(vs)
    random.shuffle(data)
    choice_b = data.pop()
    count_b = disassembly_dict(choice_b)
    global CURRENT_PAIR
    CURRENT_PAIR.append(choice_a)
    CURRENT_PAIR.append(choice_b)

    return count_a, count_b

def player_choice(pair_tuple):
    """
    Asks user to choose between first and second, who has more followers, returns
    boolean.
    """
    player_answer = "."
    while player_answer != "A" and player_answer != "B":
        player_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if player_answer == "A":
        if pair_tuple[0] > pair_tuple[1]:
            os.system("clear")
            return True
        else:
            return False
    else:
        if pair_tuple[1] > pair_tuple[0]:
            os.system("clear")
            return True
        else:
            return False
    

def next_pair():
    """
    Replaces first dictionary by second* one, and second one by a third**, random from
    data.py. Returns a tuple of followers count of first* and second** dictionary.
    """
    random.shuffle(data)
    choice_c = data.pop()
    global CURRENT_PAIR
    CURRENT_PAIR[0] = CURRENT_PAIR[1]
    CURRENT_PAIR[1] = choice_c
    print(logo)
    new_choice_a = CURRENT_PAIR[0]
    count_a = disassembly_dict(new_choice_a)
    print(vs)
    new_choice_b = CURRENT_PAIR[1]
    count_b = disassembly_dict(new_choice_b)

    return count_a, count_b

pair_tuple_followage = initialize(logo, data)
if player_choice(pair_tuple_followage) == True:
    while player_choice(next_pair()) and len(data) > 0:
        pass
    if len(data) == 0:
        print("you win, no more things to guess/compare")
    else:
        print("wrong answer")