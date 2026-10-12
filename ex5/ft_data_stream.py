import typing
import random

players = ["bob", "alice", "dylan", "charlie"]

actions = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "use",
    "release"
]


def gen_event() -> typing.Generator[tuple, None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list[tuple]) -> typing.Generator[tuple, None, None]:
    while events:
        el_del = random.choice(events)
        events.remove(el_del)
        yield(el_del)


print("=== Game Data Stream Processor ===")

gen_obj = gen_event()
for i in range(1000):
    pairs = next(gen_obj)
    print(f"Event {i}: Player {pairs[0]} did action {pairs[1]}")

pairs_tup = []
gen_obj = gen_event()
for i in range(10):
    pairs = next(gen_obj)
    pairs_tup.append(pairs)

print(f"Built list of 10 events: {pairs_tup}")

for event in consume_event(pairs_tup):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {pairs_tup}")
