#dfs traversal printing every child of a node

import queue

def dfsTraversal(arr):
    result = dict()
    for i in range(1, len(arr)+1):
        result[i] = []
    visited = set()
    que = queue.LifoQueue(maxsize=0)
    start = 1
    que.put(start)
    while not que.empty():
        curr = que.get()
        if curr not in visited:
            for j, x in enumerate(arr[curr-1]):
                if x == 1:
                    que.put(j+1)
                    result[curr].append(j+1)
            visited.add(curr)

    print(result)



arr = [[0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 0],
       [0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 1, 0]]
dfsTraversal(arr)