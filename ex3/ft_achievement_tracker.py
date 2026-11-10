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
    num = random.randint(7, 14)
    return set(random.sample(achievements, num))


Alice = gen_player_achievements()
Bob = gen_player_achievements()
Charlie = gen_player_achievements()
Dylan = gen_player_achievements()

hapgyiphap = Alice.union(Bob, Charlie, Dylan)
gyogyiphap = Alice.intersection(Bob, Charlie, Dylan)
only_Alice = Alice.difference(Bob, Charlie, Dylan)
only_Bob = Bob.difference(Alice, Charlie, Dylan)
only_Charlie = Charlie.difference(Alice, Bob, Dylan)
only_Dylan = Dylan.difference(Alice, Bob, Charlie)

missing_Alice = set(achievements).difference(Alice)
missing_Bob = set(achievements).difference(Bob)
missing_Charlie = set(achievements).difference(Charlie)
missing_Dylan = set(achievements).difference(Dylan)

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")
    print()
    print(f"All distinct achievements: {hapgyiphap}")
    print()
    print(f"Common achievements: {gyogyiphap}")
    print()
    print(f"Only Alice has: {only_Alice}")
    print(f"Only Bob has: {only_Bob}")
    print(f"Only Charlie has: {only_Charlie}")
    print(f"Only Dylan has: {only_Dylan}")
    print()
    print(f"Alice is missing: {missing_Alice}")
    print(f"Bob is missing: {missing_Bob}")
    print(f"Charlie is missing: {missing_Charlie}")
    print(f"Dylan is missing: {missing_Dylan}")
