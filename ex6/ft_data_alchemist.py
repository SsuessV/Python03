import random

print("=== Game Data Alchemist ===")

names = ["Alice", "Bob", "Charlie", "Dylan", "emma", "gregory", "john", "kevin", "liam"]
capitalize = [name.capitalize() for name in names]
capitalized_names = [name for name in names if name[0].isupper()]