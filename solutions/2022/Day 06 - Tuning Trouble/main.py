import sys

line = sys.stdin.read()

for window_size in [4, 14]:
    for window_begin in range(len(line) - window_size):
        if len(set(line[window_begin:window_begin + window_size])) == window_size:
            print(window_size + window_begin)
            break
