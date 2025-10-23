from collections import deque
numbers = [1, 2, 3, 4, 5]
step = 1
deq  = deque(numbers)
deq.rotate(step)
numbers[:] = deq
print(numbers)
