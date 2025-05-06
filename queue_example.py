from collections import deque

cola = deque()

# Add elements to the queue (enqueue)
cola.append("A")
cola.append("B")
cola.append("C")

print("Cola:", cola)  # Cola: queue(['A', 'B', 'C'])

# Remove elements in the queue (dequeue)
first = cola.popleft()
print("remove element:", first)  # A
print("Uptaded queue:", cola)      # queue(['B', 'C'])
print('--------------------')
cola.append("D")
cola.append("E")
print("Uptaded queue:", cola)      # queue(['B', 'C'])
first = cola.popleft()
print("remove element:", first)  # A
