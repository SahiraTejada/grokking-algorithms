# Create an empty stack
stack = []

# Push items onto the stack
stack.append('A')   # push A
stack.append('B')   # push B
stack.append('C')   # push C

print("Stack after pushes:", stack)

# Peek at the top item (optional, without removing it)
top = stack[-1]
print("Top of the stack:", top)

# Pop items from the stack (LIFO: last in, first out)
print("Popped:", stack.pop())  # removes 'C'
print("Popped:", stack.pop())  # removes 'B'

# Stack after popping
print("Stack now:", stack)

# Check if the stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
