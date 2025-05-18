# Import the math module to use infinity
import math

# ------------------------------
# Step 1: Define the graph
# ------------------------------

# Create an empty graph represented as a dictionary
graph = {}

# Define edges and weights from 'start' to its neighbors 'a' and 'b'
graph["start"] = {"a": 6, "b": 2}

# Define edge from 'a' to 'fin' with weight 1
graph["a"] = {"fin": 1}

# Define edges from 'b' to 'a' and 'fin'
graph["b"] = {"a": 3, "fin": 5}

# 'fin' has no outgoing edges
graph["fin"] = {}

# ------------------------------
# Step 2: Set up the costs table
# ------------------------------

# Define infinity using math.inf to represent unknown/very high costs
infinity = math.inf

# Create a table (dictionary) to store the cost to reach each node from 'start'
costs = {
    "a": 6,         # initial cost to reach 'a' from 'start' is 6
    "b": 2,         # initial cost to reach 'b' from 'start' is 2
    "fin": infinity # cost to reach 'fin' is unknown, set to infinity
}

# ------------------------------
# Step 3: Set up the parents table
# ------------------------------

# Create a table to keep track of the optimal parent (previous node) for each node
parents = {
    "a": "start",   # 'start' is the parent of 'a'
    "b": "start",   # 'start' is the parent of 'b'
    "fin": None     # we haven't found a path to 'fin' yet
}

# ------------------------------
# Step 4: Track processed nodes
# ------------------------------

# Create a set to keep track of the nodes we've already processed
processed = set()

# ------------------------------
# Step 5: Helper function
# ------------------------------

# This function finds the unprocessed node with the lowest cost
def find_lowest_cost_node(costs):
    lowest_cost = math.inf        # start with the highest possible cost
    lowest_cost_node = None       # no node selected yet
    for node in costs:            # go through each node in the costs table
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]    # found a lower-cost unprocessed node
            lowest_cost_node = node
    return lowest_cost_node       # return the node with the lowest cost

# ------------------------------
# Step 6: Main Dijkstra loop
# ------------------------------

# Find the first node to process (the lowest-cost unprocessed node)
node = find_lowest_cost_node(costs)

# Loop until all nodes are processed
while node is not None:
    cost = costs[node]               # Get the current cost of this node
    neighbors = graph[node]          # Get its neighbors from the graph

    # Loop through all the neighbors of this node
    for n in neighbors:
        new_cost = cost + neighbors[n]   # Calculate new cost to neighbor
        if new_cost < costs[n]:          # If new path is cheaper
            costs[n] = new_cost          # Update the cost to this neighbor
            parents[n] = node            # Update the parent to the current node

    processed.add(node)                  # Mark this node as processed
    node = find_lowest_cost_node(costs)  # Move to the next lowest-cost node

# ------------------------------
# Step 7: Print final results
# ------------------------------

# Print the minimum cost to reach each node from 'start'
print("Shortest cost to each node:")
print(costs)

# Print the parent of each node, showing the optimal path tree
print("\nParent path tree:")
print(parents)


print("💰 Final shortest costs from 'start':")
for k, v in costs.items():
    print(f"{k}: {v}")

print("\n🧭 Shortest path tree (who leads to who):")
for k, v in parents.items():
    print(f"{k}: {v}")