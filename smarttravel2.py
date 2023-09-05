def tsp_held_karp(graph, start):
    n = len(graph)
    dp = {}

    # Helper function to generate the key for the dp dictionary
    def get_key(visited, last):
        return tuple([last] + sorted(visited))

    # Base case for the recursion
    def held_karp_helper(visited, last):
        if len(visited) == n:
            return graph[last][start], [start]

        key = get_key(visited, last)

        if key in dp:
            return dp[key]

        min_distance = float('inf')
        min_path = []

        for location in graph[last]:
            if location not in visited and location != last:
                visited.add(location)
                distance, path = held_karp_helper(visited, location)
                distance += graph[last][location]
                if distance < min_distance:
                    min_distance = distance
                    min_path = [last] + path
                visited.remove(location)

        dp[key] = min_distance, min_path
        return min_distance, min_path

    # Starting the recursion from the given start location
    min_distance, min_path = held_karp_helper(set(), start)

    return min_distance, min_path


# Sample graph representing distances between locations for Visitor 1
graph_visitor1 = {
    'Brigham': {'Brigham': 0, 'Harvard': 2.7, 'MIT': 2.2, 'MFA': 0.6, 'Chinatown': 2.6},
    'Harvard': {'Brigham': 2.7, 'Harvard': 0, 'MIT': 1.1, 'MFA': 3.8, 'Chinatown': 4.8},
    'MIT': {'Brigham': 2.2, 'Harvard': 1.1, 'MIT': 0, 'MFA': 2.1, 'Chinatown': 2.8},
    'MFA': {'Brigham': 0.6, 'Harvard': 3.8, 'MIT': 2.1, 'MFA': 0, 'Chinatown': 2.4},
    'Chinatown': {'Brigham': 2.6, 'Harvard': 4.8, 'MIT': 2.8, 'MFA': 2.4, 'Chinatown': 0}
}

# Graph for Visitor 2
graph_visitor2 = {
    'Malden Center': {'Malden Center': 0, 'Boston Commons': 6.0, 'Seaport': 7.2, 'Isabella Museum': 8.8},
    'Boston Commons': {'Malden Center': 6.0, 'Boston Commons': 0, 'Seaport': 1.3, 'Isabella Museum': 2.7},
    'Seaport': {'Malden Center': 7.2, 'Boston Commons': 1.3, 'Seaport': 0, 'Isabella Museum': 4.3},
    'Isabella Museum': {'Malden Center': 8.8, 'Boston Commons': 2.7, 'Seaport': 4.3, 'Isabella Museum': 0}
}

# Graph for Visitor 3
graph_visitor3 = {
    'Downtown Crossing': {'Downtown Crossing': 0, 'Northeastern': 2.8, 'Prudential': 1.7, 'Seaport': 1.1, 'Boston Commons': 0.7},
    'Northeastern': {'Downtown Crossing': 2.8, 'Northeastern': 0, 'Prudential': 0.7, 'Seaport': 3.0, 'Boston Commons': 1.3},
    'Prudential': {'Downtown Crossing': 1.7, 'Northeastern': 0.7, 'Prudential': 0, 'Seaport': 2.9, 'Boston Commons': 0.7},
    'Seaport': {'Downtown Crossing': 1.1, 'Northeastern': 3.0, 'Prudential': 2.9, 'Seaport': 0, 'Boston Commons': 1.5},
    'Boston Commons': {'Downtown Crossing': 0.7, 'Northeastern': 1.3, 'Prudential': 0.7, 'Seaport': 1.5, 'Boston Commons': 0}
}

# Calculate the minimum distance and path for Visitor 1, starting from 'Brigham'
min_distance_visitor1, path_visitor1 = tsp_held_karp(graph_visitor1, 'Brigham')

# Remove the duplicate 'Brigham' at the end of the path
path_visitor1.pop()

print("Visitor 1: Minimum distance = {:.2f} miles".format(min_distance_visitor1))
print("Visitor 1: Visited places in order =", path_visitor1)

# Calculate the minimum distance and path for Visitor 2, starting from 'Malden Center'
min_distance_visitor2, path_visitor2 = tsp_held_karp(graph_visitor2, 'Malden Center')

# Remove the duplicate 'Malden Center' at the end of the path
path_visitor2.pop()

print("Visitor 2: Minimum distance = {:.2f} miles".format(min_distance_visitor2))
print("Visitor 2: Visited places in order =", path_visitor2)

# Calculate the minimum distance and path for Visitor 3, starting from 'Downtown Crossing'
min_distance_visitor3, path_visitor3 = tsp_held_karp(graph_visitor3, 'Downtown Crossing')

# Remove the duplicate 'Downtown Crossing' at the end of the path
path_visitor3.pop()

print("Visitor 3: Minimum distance = {:.2f} miles".format(min_distance_visitor3))
print("Visitor 3: Visited places in order =", path_visitor3)
