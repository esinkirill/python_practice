import random
import time

candidates = ["Alice", "Bob", "Charlie"]
num_votes = 10
counts = {}

for i in range(num_votes):
    vote = random.choice(candidates)
    counts.setdefault(vote, 0)
    counts[vote] += 1
    print(f"{vote} + 1 голос")
    time.sleep(0.15)
print('-'*30)
for name, cnt in counts.items():
    print(f"{name}: {cnt} votes")

max_votes = max(counts.values())

winners = [name for name, cnt in counts.items() if cnt == max_votes]
winner = min(winners)

print(f"\nWinner: {winner}")


