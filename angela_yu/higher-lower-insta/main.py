from art import logo, vs
from game_data import data
import random

def initialize():
    """
    Function chooses two random individuals and returns a tuple
    with indA_followers_count and indB_followers_count.
    """
    print(logo)

    random.shuffle(data)
    choice_a = data.pop()
    # print(choice_a)
    name_a = choice_a["name"]
    desc_a = choice_a["description"]
    country_a = choice_a["country"]
    count_a = choice_a["follower_count"]
    print(f"Compare A: {name_a}, a {desc_a}, from {country_a}.")

    print(vs)

    random.shuffle(data)
    choice_b = data.pop()
    # print(choice_b)
    name_b = choice_b["name"]
    desc_b = choice_b["description"]
    country_b = choice_b["country"]
    count_b = choice_b["follower_count"]
    print(f"Against B: {name_b}, a {desc_b}, from {country_b}.")

    return count_a, count_b

def player_choice():
    player_answer = input("Who has more followers? Type 'A' or 'B': ")

initialize()
