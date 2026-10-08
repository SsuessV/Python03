import random

achievements = ['Crafting Genius',
                'World Savior',
                'Master Explorer',
                'Collector Supreme',
                'Untouchable',
                'Boss Slayer',
                'Strategist',
                'Speed Runner',
                'Survivor',
                'Treasure Hunter',
                'First Steps',
                'Sharp Mind',
                'Hidden Path Finder',
                'Unstoppable']


def gen_player_achievements() -> set[str]:
    num = random.randint(5, 10)
    return set(random.sample(achievements, num))


Alice = gen_player_achievements()
Bob = gen_player_achievements()
Charlie = gen_player_achievements()
Dylan = gen_player_achievements()

all_achieves = Alice.union(Bob, Charlie, Dylan)
gyogiphap = Alice.intersection(Bob, Charlie, Dylan)
diff_Alice = Alice.difference(Bob, Charlie, Dylan)
diff_Bob = Bob.difference(Alice, Charlie, Dylan)
diff_Charlie = Charlie.difference(Alice, Bob, Dylan)
diff_Dylan = Dylan.difference(Alice, Bob, Charlie)

missing_Alice = set(achievements).difference(Alice)
missing_Bob = set(achievements).difference(Bob)
missing_Charlie = set(achievements).difference(Charlie)
missing_Dylan = set(achievements).difference(Dylan)

print("=== Achievement Tracker System ===")
print()
print(f"Player Alice: {Alice}")
print(f"Player Bob: {Bob}")
print(f"Player Charlie: {Charlie}")
print(f"Player Dylan: {Dylan}")
print()
print(f"All distinct achievements: {all_achieves}")
print()
print(f"Common achievements: {gyogiphap}")
print()
print(f"Only Alice has: {diff_Alice}")
print(f"Only Bob has: {diff_Bob}")
print(f"Only Charlie has: {diff_Charlie}")
print(f"Only Dylan has: {diff_Dylan}")
print()
print(f"Alice is missing: {missing_Alice}")
print(f"Bob is missing: {missing_Bob}")
print(f"Charlie is missing: {missing_Charlie}")
print(f"Dylan is missing: {missing_Dylan}")
