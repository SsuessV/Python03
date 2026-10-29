import random

names = ['Alice', 'bob', 'Charlie', 'dylan',
         'Emma', 'Gregory', 'john', 'kevin', 'Liam']

capitalize_names = [name.capitalize() for name in names]
get_the_capitalized = [name for name in names if name[0].isupper()]

capnames_in_dict = {name: random.randint(1, 1000) for name in capitalize_names}
av_score = round(sum(capnames_in_dict.values()) / len(capnames_in_dict), 2)
abv_av = {name: score for name, score in capnames_in_dict.items()
          if score > av_score}

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {capitalize_names}")
    print(f"New list of capitalized names only: {get_the_capitalized}")
    print()
    print(f"Score dict: {capnames_in_dict}")
    print(f"Score average is {av_score}")
    print(f"High scores: {abv_av}")
