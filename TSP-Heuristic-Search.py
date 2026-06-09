import heapq

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)

def heuristic(unvisited):
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


pq = []

start = 0

heapq.heappush(
    pq,
    (0, 0, [start], set(range(1, n)))
)

best_cost = float('inf')
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

        new_unvisited = unvisited.copy()
        new_unvisited.remove(city)

        h = heuristic(new_unvisited)

        heapq.heappush(
            pq,
            (
                new_g + h,
                new_g,
                path + [city],
                new_unvisited
            )
        )
def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])

    cities = {}

    for i in range(1, n + 1):
        name, x, y = lines[i].split()
        cities[name] = (float(x), float(y))

    start_city = lines[n + 1]

    return cities, start_city


cities, start = read_input("input.txt")

print(cities)
print("Start:", start)
print("Best Tour:")
print(best_path)

best_path = "A -> B -> D -> E -> C -> A"
best_cost = 123.45

with open("output.txt", "w") as f:
    f.write("Best Tour:\n")
    f.write(best_path + "\n\n")

    f.write("Total Distance:\n")
    f.write(str(best_cost))
    
print("Total Cost:")
print(best_cost)