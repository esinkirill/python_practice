import random
import time

candidates = ["Alice", "Bob", "Charlie"]
num_votes = 100

votes = [random.choice(candidates) for _ in range(num_votes)]

counts = {}

for idx, vote in enumerate(votes):
    counts.setdefault(vote, 0)
    counts[vote] += 1
    print(f"Голос №{idx+1}: {vote} + 1 голос")
    time.sleep(0.15)
print("-" * 30)
for name, cnt in counts.items():
    print(f"{name}: {cnt} votes")

max_votes = max(counts.values())
winners = [name for name, cnt in counts.items() if cnt == max_votes]
winner = min(winners)

print(f"\nWinner: {winner}")
