votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Bob", "Alice"]

counts = {}
for name in votes:
    counts[name] = counts.get(name, 0) + 1

for name, cnt in counts.items():
    print(f"{name}: {cnt} votes")

max_votes = max(counts.values())

winners = [name for name, cnt in counts.items() if cnt == max_votes]
winner = min(winners)

print(f"\nWinner: {winner}")
