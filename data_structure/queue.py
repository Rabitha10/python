from collections import deque

queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue element
item = queue.popleft()
print("Removed:", item)

print("Queue after removal:", queue)