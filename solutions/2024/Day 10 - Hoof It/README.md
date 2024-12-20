| Day | Link to description | Link to solution
|:---|:---|:---:|
| 10 | [Hoof It](https://adventofcode.com/2024/day/10) | [Solution](https://github.com/versenyi98/advent-of-code-solutions/tree/main/solutions/2024/Day%2010%20-%20Hoof%20It)|
### Problem summary
The input is a height map consisting of digits. The task is to get to a peak (9) from a starting position (0). The only allowed move is to step one a vertical or horizontal neighbor, which has 1 more height, than the previous position. These can be interpreted as edges of a graph.

### Solution approach
Get the number of peaks reachable for each starting position for task 1, and get all unique paths for task 2. Both of them can be done with dfs. 

----

#### Tags
#dfs