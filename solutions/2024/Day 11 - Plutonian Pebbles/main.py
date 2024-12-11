import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(stone, rounds):
  if rounds == 0:
    return 1
  if stone == 0:
    return dp(1, rounds - 1)
  elif (digits := len(str(stone))) % 2 == 0:
    return dp(int(str(stone)[:digits//2]), rounds - 1) + dp(int(str(stone)[digits//2:]), rounds - 1)
  else:
    return dp(stone * 2024, rounds - 1)
  
def main():
  stones = list(map(int, sys.stdin.read().split()))
  print(sum(dp(stone, 25) for stone in stones))
  print(sum(dp(stone, 75) for stone in stones))

if __name__ == "__main__":
    main()