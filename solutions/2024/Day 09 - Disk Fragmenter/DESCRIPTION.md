## Task 1

### Problem summary
The input is a large number describing a disk. Starting with index 0, every digit at an **even** index describes **the size of a file on the disk**, and every digit at an **odd** index describes **the size of an empty slot on the disk**.

The task is to move all of the files from the right side of the disk, to the left side, so the left side is of the disk has no empty slots, and calculate a **checksum**, which will be the answer. A single file doesn't have to be contiguous. The rules of calculating the checksum are not that interesting. 

### Solution approach
Start to go through the disk map from left and right at the same time.
- If the value on the left is describing a files size, increase the result.
- Otherwise, move as much from right to left as possible and increase the result.
  - Decrease both the left and the right items by the size of the moved object.
  - If any of the left or right items become 0, move to the next item.

The `sum_of_range` function and the `start_index` is used to calculate, how much the result should be increased by.

## Task 2

### Problem summary
The task is basically the as the first task, but after moving the files from right to left starting with the rightmost one, the **files must be contiguous**. Files can only be moved to left, or not at all. The **checksum** calculation is the same.

### Solution approach
The `start_index` variable contains a "prefix sum", that shows the starting index for each block. **The size of an empty block can only be between 1-9**. 

- Create one priority queue for each slot size, and store the index of the empty blocks in the corresponding priority queue. 
- Start from the right side of the disc map, and search for the leftmost empty block which is big enough.
- Move the file to the empty block.
- Update the result with the checksum of the moved block.
- Decrease the size of the block, and insert the index of the block to the priority queue corresponding to the remaining size of the block.

----
#### Tags
#priority-queue #two-pointer