# Problem 68
# https://projecteuler.net/problem=68

from itertools import permutations

NUMS = range(1, 11)

# -------------------------------------------------------------
# Helper functions
# -------------------------------------------------------------
def generate_triplets(target_sum):
    """All ordered triplets (outer, inner, next_inner) that sum to target_sum."""
    return [(a, b, c) for a, b, c in permutations(NUMS, 3) if a + b + c == target_sum]

def group_by_middle(triplets):
    """Dictionary: middle value -> list of triplets with that middle."""
    by_mid = {}
    for t in triplets:
        by_mid.setdefault(t[1], []).append(t)
    return by_mid

def canonicalize_rotation_only(ring):
    """Rotate ring so the smallest outer node is first (remove rotations only)."""
    outers = [t[0] for t in ring]
    min_index = outers.index(min(outers))
    return tuple(ring[min_index:] + ring[:min_index])

def ring_to_string(ring):
    """Flatten ring into concatenated numeric string."""
    return ''.join(str(x) for t in ring for x in t)

def find_rings_for_sum(target_sum):
    """Return all unique (rotation-canonicalized) 5-gon rings with this target sum."""
    triplets = generate_triplets(target_sum)
    by_mid = group_by_middle(triplets)
    found = set()

    def backtrack(path, used):
        if len(path) == 5:
            if path[-1][2] == path[0][1]:
                can = canonicalize_rotation_only(path)
                found.add(can)
            return

        last_end = path[-1][2]
        for t in by_mid.get(last_end, []):
            # only outer and inner are newly used; next_inner links forward
            if t[0] in used or t[1] in used:
                continue
            path.append(t)
            used.update((t[0], t[1]))
            backtrack(path, used)
            used.difference_update((t[0], t[1]))
            path.pop()

    for start in triplets:
        backtrack([start], {start[0], start[1]})

    return found

# -------------------------------------------------------------
# Main routine
# -------------------------------------------------------------
all_results = []  # list of (target_sum, string, int_value)

for target_sum in range(13, 19):
    rings = find_rings_for_sum(target_sum)
    if not rings:
        continue
    strings = [ring_to_string(r) for r in rings]
    strings_int = sorted([(int(s), s) for s in strings])  # numeric sort

    print(f"\nTarget sum {target_sum}: found {len(strings)} rings")
    print("-" * 45)
    for val, s in strings_int:
        print(s)
        all_results.append((target_sum, s, val))

# -------------------------------------------------------------
# Global overview
# -------------------------------------------------------------
if all_results:
    all_results.sort(key=lambda x: x[2])  # sort by numeric value
    print("\n===================================================")
    print("All solutions across all target sums (min → max):")
    print("===================================================\n")
    for target_sum, s, val in all_results:
        print(f"Sum {target_sum}: {s}")
    print("\n---------------------------------------------------")
    print(f"Maximum 16-digit string: {max(result[2] for result in all_results if len(result[1]) == 16)}")

    print("---------------------------------------------------")
else:
    print("No valid rings found in tested range.")
