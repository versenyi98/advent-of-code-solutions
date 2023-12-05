import sys
import bisect

def convert_to_ranges(section):
    section = section[1:]

    ranges = []

    for [destination, source, range_length] in map(lambda x: x.split(), section):
        source = int(source)
        destination = int(destination)
        range_length = int(range_length)
        ranges.append((source, destination, range_length))

    return sorted(ranges)

def task1(ranges, seed):
    result = seed

    for current_range in ranges:
        range_index = bisect.bisect_right(current_range, result, key=lambda x: x[0])
        if range_index > 0:
            source, destination, range_length = current_range[range_index - 1]
            if result < source + range_length and result >= source:
                result = destination + (result - source)

    return result

def task2_helper(current_ranges, seeds):
    result_seeds = []

    for seed_src, seed_len in seeds:
        while seed_len > 0:
            range_index = bisect.bisect_right(current_ranges, seed_src, key=lambda x: x[0])

            if range_index > 0:
                lower_src, lower_dst, lower_len = current_ranges[range_index - 1]
                diff = lower_dst - lower_src

                in_lower = seed_len - max(0, lower_src - seed_src) - max(0, seed_src + seed_len - lower_src - lower_len)
                in_lower = max(0, in_lower)
                if in_lower:
                    result_seeds.append((max(lower_src, seed_src) + diff, in_lower))
                    seed_len -= in_lower
                    seed_src += in_lower
                    continue

            result_seeds.append((seed_src, seed_len))
            break

    return result_seeds

def task2(ranges, seeds):
    for current_range in ranges:
        seeds = task2_helper(current_range, seeds)
    min_result = min([seed for seed, length in seeds])

    return min_result


def main():
    sections = [section.split('\n') for section in "".join(sys.stdin.readlines()).split('\n\n')]

    initial_seeds = list(map(int, sections[0][0].split(': ')[-1].split()))

    ranges = [convert_to_ranges(sections[i + 1]) for i in range(7)]

    locations = [task1(ranges, seed) for seed in initial_seeds]
    print(min(locations))

    print(task2(ranges, list(zip(*[iter(initial_seeds)] * 2))))

if __name__ == "__main__":
    main()