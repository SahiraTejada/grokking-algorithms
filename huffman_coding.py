""" import heapq: This imports Python's built-in heapq module, which provides an implementation of a heap queue (priority queue). 
It will be used to build the Huffman tree efficiently.

from collections import  Counter

Counter: A dictionary subclass used to count occurrences of elements in an iterable.
It's used to count the frequency of characters in the input text.

 """

import heapq
from collections import Counter

# Step 1: Create a Node class for the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char      # Character stored in the node (None for internal nodes)
        self.freq = freq      # Frequency of the character
        self.left = None      # Left child of the node
        self.right = None     # Right child of the node

    # Needed for heapq to compare nodes
    def __lt__(self, other):
        return self.freq < other.freq  # Compare nodes based on frequency for heap operations

# Step 2: Build the Huffman Tree
def build_huffman_tree(text):
    freq_map = Counter(text)  # Count frequency of each character in the input text
    # Create a list of Node objects for each character and its frequency
    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)  # Convert the list into a min-heap based on frequency

    # Build the Huffman tree by combining the two nodes with the lowest frequency
    while len(heap) > 1:
        node1 = heapq.heappop(heap)  # Pop the node with the smallest frequency
        node2 = heapq.heappop(heap)  # Pop the next node with the second smallest frequency
        merged = Node(None, node1.freq + node2.freq)  # Create a new internal node with combined frequency
        merged.left = node1  # Assign node1 as the left child
        merged.right = node2  # Assign node2 as the right child
        heapq.heappush(heap, merged)  # Push the merged node back into the heap

    return heap[0]  # The remaining node in the heap is the root of the Huffman tree

# Step 3: Generate Huffman codes from the tree
def generate_codes(root, prefix="", code_map={}):
    if root is None:  # Base case: if node is None, return (stop recursion)
        return
    if root.char is not None:  # If it's a leaf node (contains a character)
        code_map[root.char] = prefix  # Assign the current prefix as the Huffman code for the character
    # Recursively generate codes for the left and right children
    generate_codes(root.left, prefix + "0", code_map)  # Left child gets "0" appended to the prefix
    generate_codes(root.right, prefix + "1", code_map)  # Right child gets "1" appended to the prefix
    return code_map  # Return the final code map with Huffman codes for each character

# Step 4: Encode the text
def encode(text, code_map):
    # Convert each character in the input text to its corresponding Huffman code and join them
    return ''.join(code_map[char] for char in text)

# Step 5: Decode the binary string
def decode(encoded_text, root):
    decoded = []  # List to hold the decoded characters
    current = root  # Start at the root of the Huffman tree
    for bit in encoded_text:  # Traverse the encoded binary string
        # Move left for "0" and right for "1"
        current = current.left if bit == '0' else current.right
        if current.char:  # If a leaf node is reached (contains a character)
            decoded.append(current.char)  # Add the character to the decoded list
            current = root  # Reset to the root for decoding the next character
    return ''.join(decoded)  # Join and return the decoded characters as a string

# Example usage
text = "radar"  # Example input text
root = build_huffman_tree(text)  # Build the Huffman tree from the text
code_map = generate_codes(root)  # Generate Huffman codes for each character
encoded = encode(text, code_map)  # Encode the text using the Huffman codes
decoded = decode(encoded, root)  # Decode the encoded text back to the original text
freq = Counter(text)
# Print the results
print("Original:", text)  # Print the original input text
print("Frecuency of each letter:", freq)
print("Huffman Codes:", code_map)  # Print the Huffman codes for each character
print("Encoded:", encoded)  # Print the encoded binary string
print("Decoded:", decoded)  # Print the decoded text (should match the original text)
