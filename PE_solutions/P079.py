# Problem 79
# A common security method used for online banking is to ask the user for three random characters from a passcode.
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
# the expected reply would be: 317.
#
# The text file, P079input.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse the file so as to determine
# the shortest possible secret passcode of unknown length.
from collections import deque

# input from file
triplets = []
with open("P079input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            triplets.append(line)

# graph
nodes = set()
graph = {}

for tri in triplets:
    a, b, c = tri
    nodes.update([a, b, c])
    graph.setdefault(a, set()).add(b)
    graph.setdefault(b, set()).add(c)
    graph.setdefault(c, set())  # end numbers

# in-degree calculation
in_degree = {node: 0 for node in nodes}
for node, successors in graph.items():
    for succ in successors:
        in_degree[succ] += 1

# Kahn algorithm
queue = deque([node for node in nodes if in_degree[node] == 0])
passcode = ""

while queue:
    node = queue.popleft()
    passcode += node
    for succ in graph.get(node, []):
        print(succ)
        in_degree[succ] -= 1
        if in_degree[succ] == 0:
            queue.append(succ)
    print()

print("Shortest passcode is:", passcode)