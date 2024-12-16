## Task 1

### Problem summary
The input is a grid. We start from the position where the letter `S` is located facing East, and we would like to go to position of the letter `E`.

Moving forward costs 1, turning left or right cost 1000. What is the cheapest way to reach the goal?

### Solution approach
Create a weighted graph. Each node denotes 3 values `(row, column, orientation)`. The edges are weighted following the problem statement.

Do a simple **bfs**, to calculate the best possible solution. Store the path as well for the Task #2.

## Task 2

### Problem summary
There are multiple paths for Task #1. Calculate the number of distinct positions, which lie on any optimal path.

### Solution approach
Do another **bfs**, where the targets are the nodes with their corresponding cost from the path retrieved in Task #1. During the **bfs**, if the current node is part of the target, and the current cost also matches, add the current node and its cost to the targets. Return the target.

Do this, until the size of the targets increases.

----
#### Tags
#priority-queue #bfs