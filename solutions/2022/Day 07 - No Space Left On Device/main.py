import sys

lines = [line.split() for line in sys.stdin.read().split("\n")]

directories = []
size_of_directory = {}

for idx, line in enumerate(lines):
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                directories.pop(-1)
            elif line[2] == "/":
                directories = [line[2]]
            else:
                directories.append(line[2])
    else:
        if line[0].isnumeric():
            for i, directory in enumerate(directories):
                full_path = '/'.join(directories[:i + 1])
                if full_path not in size_of_directory:
                    size_of_directory[full_path] = 0
                size_of_directory[full_path] += int(line[0])

sizes = filter(lambda x: x <= 100000, size_of_directory.values())
print(sum(sizes))

remaining_space = 70000000 - size_of_directory['/']
space_to_free = 30000000 - remaining_space
sizes = filter(lambda x: x >= space_to_free, size_of_directory.values())
print(sorted(sizes)[0])