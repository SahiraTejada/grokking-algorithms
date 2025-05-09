# Importing deque from collections to use as a queue
from collections import deque

# Defining the graph as an adjacency list (dictionary of lists) [img\graph-example.png]
graph = {}
graph["you"] = ["alice", "bob", "claire"]  # "you" is connected to alice, bob, and claire
graph["bob"] = ["anuj", "peggy"]           # bob is connected to anuj and peggy
graph["alice"] = ["peggy"]                 # alice is connected to peggy
graph["claire"] = ["thom", "jonny"]        # claire is connected to thom and jonny
graph["anuj"] = []                         # anuj has no connections
graph["peggy"] = []                        # peggy has no connections
graph["thom"] = []                         # thom has no connections
graph["jonny"] = []                        # jonny has no connections

# Function to check if a person is a mango seller
def person_is_seller(name):
    return name[-1] == 'm'

# Breadth-First Search function to find the mango seller
def search(name):
    # Create a queue and enqueue all of 'name's neighbors (friends)
    search_queue = deque()
    search_queue += graph[name]

    # This set keeps track of people already checked
    searched = set()

    # Continue the search while the queue is not empty
    while search_queue:
        # Dequeue the first person in the queue
        person = search_queue.popleft()

        # Only search this person if they haven't been searched already
        if not person in searched:
            # Check if this person is a mango seller
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True  # Stop the search as we found a seller
            else:
                # If not a seller, enqueue all of their friends (neighbors)
                search_queue += graph[person]

                # Mark this person as searched
                searched.add(person)
        
        # Print current state of the queue (for debugging/visualization)
        print(f"people to search: {search_queue}")

    # If no seller is found after checking everyone
    return False

# Start the search from "you"
search("you")
