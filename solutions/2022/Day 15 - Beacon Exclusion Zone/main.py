import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches


lines = sys.stdin.read().split("\n")
sensor_beacon_mapping = {}

for line in lines:
    line_split = line.split()

    sensor_x = int(line_split[2][2:-1])
    sensor_y = int(line_split[3][2:-1])

    beacon_x = int(line_split[-2][2:-1])
    beacon_y = int(line_split[-1][2:])

    sensor_beacon_mapping[(sensor_x, sensor_y)] = (beacon_x, beacon_y)

beacons = set(sensor_beacon_mapping.values())
sensors = set(sensor_beacon_mapping.keys())


def get_segments(line_to_watch):
    segments = []
    for (sensor_x, sensor_y), (beacon_x, beacon_y) in sensor_beacon_mapping.items():
        radius = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        dist = abs(sensor_y - line_to_watch)
        length = radius - dist

        if sensor_y - radius < line_to_watch < sensor_y + radius:
            segments.append([sensor_x - length, sensor_x + length])

    return sorted(segments)


def part1():
    line_to_watch = 2_000_000

    segments = get_segments(line_to_watch)

    covered = 0
    current_begin = None
    current_end = None

    for begin, end in segments:
        if current_begin is None:
            current_begin = begin
        if current_end is None:
            current_end = end

        if begin > current_end:
            covered += end - begin + 1
            current_begin = begin
        current_end = max(end, current_end)
    covered += current_end - current_begin + 1 - len([beacon for beacon in beacons if beacon[1] == line_to_watch])
    return covered


def part2():
    for line_to_watch in range(4_000_000, -1, -1):
        segments = get_segments(line_to_watch)

        current_end = None

        for begin, end in segments:
            if current_end is None:
                current_end = end

            if 0 < current_end < begin < 4_000_000:
                return (current_end + 1) * 4_000_000 + line_to_watch
            current_end = max(current_end, end)


def part2_fun():
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')

    plt.xlim([0, 4_000_000])
    plt.ylim([0, 4_000_000])

    #plt.xlim([3_446_135, 3_446_140])
    #plt.ylim([3_204_477, 3_204_482])
    for idx, ((sensor_x, sensor_y), (beacon_x, beacon_y)) in enumerate(sensor_beacon_mapping.items()):
        radius = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        color = ['b', 'g', 'r', 'c', 'm', 'y', 'k'][idx % 7]
        x = [sensor_x - radius, sensor_x, sensor_x + radius, sensor_x]
        y = [sensor_y, sensor_y + radius, sensor_y, sensor_y - radius]
        ax.add_patch(patches.Polygon(xy=list(zip(x, y)), fill=True, color=color))
        plt.show(block=False)
        plt.pause(0.1)
    plt.show()

    x = 3_446_137
    y = 3_204_480

    return x * 4_000_000 + y


print(part1())
print(part2())
print(part2_fun())

