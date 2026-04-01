# Problem 83
# In the  by  matrix below, the minimal path sum from the top left to the bottom right,
# by moving left, right, up, and down, is indicated in bold red and is equal to .
#
#      .131  673 .234  .103  .18
#      .201 .96  .342   965  .150
#       630  803  746  .422  .111
#       537  699  497  .121   956
#       805  732  524   .37  .331
#
# Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down
# in p081input.txt text file containing an 80 by 80 matrix.

import heapq
FILE_NAME = "P081input.txt"

def load_data(file_name):
    lines = []
    with open(file_name, "r") as f:
        for line in f:
            lines.append(list(map(int, line.strip().split(","))))
        return lines


def shortest_path(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Vzdialenosti
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = matrix[0][0]

    # Priority queue: (cena, riadok, stĺpec)
    pq = [(matrix[0][0], 0, 0)]

    # Rodič pre rekonštrukciu cesty
    parent = [[None] * m for _ in range(n)]

    # Možné pohyby: hore, dole, vpravo, vľavo
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while pq:
        cost, r, c = heapq.heappop(pq)

        # Ak sme už našli lepšiu cestu, preskočíme
        if cost > dist[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                new_cost = cost + matrix[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    parent[nr][nc] = (r, c)
                    heapq.heappush(pq, (new_cost, nr, nc))

    # Rekonštrukcia cesty
    path = []
    r, c = n - 1, m - 1
    while r is not None and c is not None:
        path.append((r, c))
        r, c = parent[r][c] if parent[r][c] else (None, None)
    path.reverse()

    return dist[n - 1][m - 1], path

if __name__ == '__main__':
    matrix = load_data(FILE_NAME)
    cost, path = shortest_path(matrix)
    print("Najnižšia suma:", cost)
    print("Cesta:", path)