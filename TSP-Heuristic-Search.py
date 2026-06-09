import heapq
import math

def read_input(filename):

    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])

    names = []
    coords = []

    for i in range(1, n + 1):

        name, x, y = lines[i].split()

        names.append(name)
        coords.append((float(x), float(y)))

    start_name = lines[n + 1]

    start = names.index(start_name)

    return names, coords, start

def build_distance_matrix(coords):

    n = len(coords)

    dist = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):

            x1, y1 = coords[i]
            x2, y2 = coords[j]

            dist[i][j] = math.sqrt(
                (x1 - x2) ** 2 +
                (y1 - y2) ** 2
            )

    return dist

def heuristic(unvisited, dist):

    n = len(dist)

    if not unvisited:
        return 0

    h = 0

    for city in unvisited:

        h += min(
            dist[city][j]
            for j in range(n)
            if j != city
        )

    return h / 2

def tsp_astar(dist, start):

    n = len(dist)

    pq = []

    heapq.heappush(
        pq,
        (
            0,                      # f
            0,                      # g
            [start],                # path
            set(range(n)) - {start}
        )
    )

    best_cost = float("inf")
    best_path = None

    while pq:

        f, g, path, unvisited = heapq.heappop(pq)

        current = path[-1]

        if not unvisited:

            total_cost = g + dist[current][start]

            if total_cost < best_cost:

                best_cost = total_cost
                best_path = path + [start]

            continue

        for city in unvisited:

            new_g = g + dist[current][city]

            if new_g >= best_cost:
                continue

            new_unvisited = unvisited.copy()
            new_unvisited.remove(city)

            h = heuristic(new_unvisited, dist)

            heapq.heappush(
                pq,
                (
                    new_g + h,
                    new_g,
                    path + [city],
                    new_unvisited
                )
            )

    return best_path, best_cost

def write_output(filename, path, cost):

    with open(filename, "w") as f:

        f.write("Best Tour:\n")

        f.write(
            " -> ".join(map(str, path))
        )

        f.write("\n\n")

        f.write(
            f"Total Cost: {cost:.2f}\n"
        )

def main():

    names, coords, start = read_input("input.txt")

    dist = build_distance_matrix(coords)

    best_path, best_cost = tsp_astar(
        dist,
        start
    )

    print("Best Tour:")
    print(best_path)

    print("\nTotal Cost:")
    print(round(best_cost, 2))

    write_output(
        "output.txt",
        best_path,
        best_cost
    )


if __name__ == "__main__":
    main()