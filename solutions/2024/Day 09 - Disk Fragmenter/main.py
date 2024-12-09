import sys
from collections import defaultdict
from itertools import accumulate
import heapq

def sum_of_range(start, end):
  n = end - start
  return n * (start + end - 1) // 2

def task1(disk_map):
  left, right, start_index = 0, len(disk_map) // 2 * 2, 0
  result = 0

  while left <= right:
    if left % 2 == 0:
      result += sum_of_range(start_index, start_index + disk_map[left]) * left // 2
      start_index += disk_map[left]
      left += 1
    else:
      to_move = min(disk_map[left], disk_map[right])
      result += sum_of_range(start_index, start_index + to_move) * right // 2
      start_index += to_move
      disk_map[left] -= to_move
      disk_map[right] -= to_move
      if disk_map[left] == 0:
        left += 1
      if disk_map[right] == 0:
        right -= 2
      
  return result

def task2(disk_map):
  right = (len(disk_map) - 1) // 2 * 2
  start_index = [0] + list(accumulate(disk_map))
  
  slot_positions = defaultdict(list)
  
  for slot_pos in range(1, len(disk_map), 2):
    if (slot_size := disk_map[slot_pos]) > 0:
      heapq.heappush(slot_positions[slot_size], slot_pos)

  result = 0

  while right > 0:
    selected_slot_pos = right
    selected_slot_size = 0
    
    for slot_size in range(disk_map[right], 10):
      if len(slot_positions[slot_size]) and slot_positions[slot_size][0] < selected_slot_pos:
        selected_slot_pos = slot_positions[slot_size][0]
        selected_slot_size = slot_size

    slot_start_index = start_index[selected_slot_pos]

    result += sum_of_range(slot_start_index, slot_start_index + disk_map[right]) * right // 2
    if selected_slot_pos != right:
      heapq.heappop(slot_positions[selected_slot_size])
      start_index[selected_slot_pos] += disk_map[right]
      if (remaining_slot_size := selected_slot_size - disk_map[right]) > 0:
        heapq.heappush(slot_positions[remaining_slot_size], selected_slot_pos)
    right -= 2
     
  return result


def main():
  disk_map = list(map(int, sys.stdin.read()))
  print(f"Task1: {task1(disk_map.copy())}")
  print(f"Task2: {task2(disk_map.copy())}")

if __name__ == "__main__":
    main()