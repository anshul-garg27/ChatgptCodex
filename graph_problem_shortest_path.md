## DSA Problem: Finding the Shortest Route in a City

**Problem Statement:**

Imagine a city with several landmarks interconnected by roads. You are given a map of this city, represented as a graph where landmarks are nodes and roads are edges. All roads are bidirectional and, for simplicity, we assume that traveling along any road takes the same amount of time (i.e., the graph is unweighted).

You are currently at a starting landmark and wish to find the shortest route (in terms of the number of roads traversed) to a specific destination landmark.

**Input:**

*   **Number of Landmarks (N):** An integer representing the total number of landmarks. Landmarks are numbered from 0 to N-1.
*   **Number of Roads (M):** An integer representing the total number of roads connecting the landmarks.
*   **Roads:** A list of M pairs of integers (u, v), where each pair indicates a bidirectional road between landmark `u` and landmark `v`.
*   **Start Landmark (S):** An integer representing the starting landmark.
*   **Destination Landmark (D):** An integer representing the destination landmark.

**Output:**

*   If a path exists, print the minimum number of roads you need to travel to get from landmark S to landmark D.
*   If there is no path between landmark S and landmark D, print -1.

**Example:**

Let's say we have:
*   N = 5 landmarks (0, 1, 2, 3, 4)
*   M = 5 roads
*   Roads: (0,1), (0,2), (1,3), (2,3), (3,4)
*   Start Landmark S = 0
*   Destination Landmark D = 4

The shortest route from 0 to 4 is 0 -> 1 -> 3 -> 4 or 0 -> 2 -> 3 -> 4. Both involve traversing 3 roads.
Output: 3
---

## Algorithm: Breadth-First Search (BFS)

The problem of finding the shortest path in an unweighted graph can be efficiently solved using the Breadth-First Search (BFS) algorithm. BFS explores the graph layer by layer, guaranteeing that the first time we reach the destination node, it will be via the shortest path.

**How BFS Works for Shortest Path:**

1.  **Initialization:**
    *   Create a queue to store the landmarks to visit.
    *   Create a way to keep track of the distance (number of roads) from the start landmark to every other landmark. Initialize all distances to infinity (or a very large number) and the distance to the start landmark as 0.
    *   Create a set or boolean array to keep track of visited landmarks to avoid cycles and redundant computations. Initialize all landmarks as not visited.

2.  **Starting BFS:**
    *   Add the starting landmark `S` to the queue.
    *   Mark `S` as visited.
    *   Set the distance to `S` as 0.

3.  **Processing Landmarks:**
    *   While the queue is not empty:
        *   Dequeue the current landmark, let's call it `u`.
        *   For each landmark `v` that is a neighbor of `u` (i.e., there's a road between `u` and `v`):
            *   If `v` has not been visited:
                *   Mark `v` as visited.
                *   Set the distance to `v` as `distance to u + 1`.
                *   Enqueue `v`.
                *   If `v` is the destination landmark `D`, then the distance calculated for `v` is the shortest path distance. We can stop here or continue if we need to find paths to other nodes as well (though for this specific problem, we can stop).

4.  **Result:**
    *   After the BFS completes (or we stop early at the destination), the calculated distance to the destination landmark `D` is the length of the shortest path.
    *   If the destination landmark `D` was never reached (e.g., its distance remains infinity or it was never marked visited), it means there is no path from `S` to `D`. In this case, the output should be -1.

**Why BFS guarantees the shortest path:**

BFS explores the graph by expanding outwards from the starting node, level by level. This means it finds all paths of length 1, then all paths of length 2, and so on. Therefore, the first time it reaches the destination node, it must have found a path with the minimum number of edges.
---

## Diagram and BFS Walkthrough

Let's use the example from the problem statement:
*   N = 5 landmarks (0, 1, 2, 3, 4)
*   M = 5 roads
*   Roads: (0,1), (0,2), (1,3), (2,3), (3,4)
*   Start Landmark S = 0
*   Destination Landmark D = 4

**Graph Representation (Adjacency List):**

*   0: [1, 2]
*   1: [0, 3]
*   2: [0, 3]
*   3: [1, 2, 4]
*   4: [3]

**BFS Walkthrough (S=0, D=4):**

1.  **Initialization:**
    *   `queue = []`
    *   `distances = {0: infinity, 1: infinity, 2: infinity, 3: infinity, 4: infinity}` (or an array `[inf, inf, inf, inf, inf]`)
    *   `visited = {0:F, 1:F, 2:F, 3:F, 4:F}` (F=False, T=True)

2.  **Start BFS:**
    *   Enqueue 0: `queue = [0]`
    *   Mark 0 as visited: `visited[0] = T`
    *   Set distance: `distances[0] = 0`

3.  **Processing:**

    *   **Dequeue 0:** `u = 0`, `queue = []`
        *   Neighbors of 0 are 1 and 2.
        *   **Neighbor 1:**
            *   Not visited. Mark visited: `visited[1] = T`.
            *   Distance: `distances[1] = distances[0] + 1 = 0 + 1 = 1`.
            *   Enqueue 1: `queue = [1]`.
        *   **Neighbor 2:**
            *   Not visited. Mark visited: `visited[2] = T`.
            *   Distance: `distances[2] = distances[0] + 1 = 0 + 1 = 1`.
            *   Enqueue 2: `queue = [1, 2]`.

    *   **Dequeue 1:** `u = 1`, `queue = [2]`
        *   Neighbors of 1 are 0 and 3.
        *   **Neighbor 0:**
            *   Visited. Skip.
        *   **Neighbor 3:**
            *   Not visited. Mark visited: `visited[3] = T`.
            *   Distance: `distances[3] = distances[1] + 1 = 1 + 1 = 2`.
            *   Enqueue 3: `queue = [2, 3]`.

    *   **Dequeue 2:** `u = 2`, `queue = [3]`
        *   Neighbors of 2 are 0 and 3.
        *   **Neighbor 0:**
            *   Visited. Skip.
        *   **Neighbor 3:**
            *   Visited. Skip. (Note: Landmark 3 was already visited and processed when dequeuing 1. Its distance is already set to 2, which is the shortest from 0).

    *   **Dequeue 3:** `u = 3`, `queue = []`
        *   Neighbors of 3 are 1, 2, and 4.
        *   **Neighbor 1:**
            *   Visited. Skip.
        *   **Neighbor 2:**
            *   Visited. Skip.
        *   **Neighbor 4:**
            *   Not visited. Mark visited: `visited[4] = T`.
            *   Distance: `distances[4] = distances[3] + 1 = 2 + 1 = 3`.
            *   Enqueue 4: `queue = [4]`.
            *   **Destination 4 reached!** The shortest distance is `distances[4] = 3`. We can stop.

4.  **Result:**
    *   The shortest path from landmark 0 to landmark 4 is 3 roads.

This walkthrough shows how BFS explores layer by layer:
*   Layer 0: {0} (distance 0)
*   Layer 1: {1, 2} (distance 1 from 0)
*   Layer 2: {3} (distance 2 from 0, reached via 1 or 2)
*   Layer 3: {4} (distance 3 from 0, reached via 3)
---

## Python Code for the Solution

```python
from collections import deque

def shortest_route(n, m, roads, s, d):
    """
    Calculates the shortest route in a city using BFS.

    Args:
        n (int): Number of landmarks (0 to n-1).
        m (int): Number of roads. (Note: m is not directly used in this BFS implementation
                  once the adjacency list is built, but it's part of the problem's input spec)
        roads (list of tuples): List of (u, v) pairs representing bidirectional roads.
        s (int): Starting landmark.
        d (int): Destination landmark.

    Returns:
        int: The minimum number of roads to travel from s to d, or -1 if no path exists.
    """

    if s == d:
        return 0

    # 1. Build Adjacency List representation of the graph
    adj = [[] for _ in range(n)]
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)

    # 2. Initialization for BFS
    queue = deque()
    # Using an array for distances, initialized to -1 (or infinity)
    # -1 can signify 'not reached yet' and also serve as the answer if destination is unreachable.
    distances = [-1] * n
    # Visited array is implicitly handled by checking if distances[node] == -1

    # 3. Starting BFS
    queue.append(s)
    distances[s] = 0

    # 4. Processing Landmarks
    while queue:
        current_landmark = queue.popleft()

        for neighbor in adj[current_landmark]:
            if distances[neighbor] == -1: # If neighbor has not been visited
                distances[neighbor] = distances[current_landmark] + 1
                queue.append(neighbor)

                if neighbor == d:
                    return distances[d] # Destination reached

    # 5. Result
    return distances[d] # Will be -1 if destination was not reached

# Example Usage (from the problem statement):
if __name__ == '__main__':
    N = 5
    M = 5
    ROADS = [(0,1), (0,2), (1,3), (2,3), (3,4)]
    S = 0
    D = 4
    result = shortest_route(N, M, ROADS, S, D)
    print(f"Shortest route from {S} to {D}: {result}") # Expected: 3

    N2 = 6
    M2 = 5
    ROADS2 = [(0,1), (0,2), (1,3), (2,3), (4,5)] # Landmark 5 is disconnected from 0-3
    S2 = 0
    D2 = 5
    result2 = shortest_route(N2, M2, ROADS2, S2, D2)
    print(f"Shortest route from {S2} to {D2}: {result2}") # Expected: -1

    N3 = 4
    M3 = 3
    ROADS3 = [(0,1), (1,2), (2,3)]
    S3 = 3
    D3 = 0
    result3 = shortest_route(N3, M3, ROADS3, S3, D3)
    print(f"Shortest route from {S3} to {D3}: {result3}") # Expected: 3

    N4 = 2
    M4 = 0 # No roads
    ROADS4 = []
    S4 = 0
    D4 = 1
    result4 = shortest_route(N4, M4, ROADS4, S4, D4)
    print(f"Shortest route from {S4} to {D4}: {result4}") # Expected: -1

    N5 = 1
    M5 = 0
    ROADS5 = []
    S5 = 0
    D5 = 0
    result5 = shortest_route(N5, M5, ROADS5, S5, D5) # Start = Destination
    print(f"Shortest route from {S5} to {D5}: {result5}") # Expected: 0
```

This Python code defines a function `shortest_route` that takes the graph information and start/destination landmarks as input. It uses an adjacency list to represent the graph and a queue for the BFS traversal. The `distances` array keeps track of the shortest distance from the start node and also implicitly marks visited nodes.
