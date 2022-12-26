import sys
import time


def get_valve_info(lines):
    info = {}
    for line in lines:
        line = line.replace(",", "")
        valve = line.split()[1]
        flow_rate = int(line.split()[4][5:-1])
        connections = line.split()[9:]
        info[valve] = {"flow": flow_rate, "connections": connections}
    return info


lines = sys.stdin.read().split("\n")

valve_info = get_valve_info(lines)

non_zero_valves = [valve for valve, info in valve_info.items() if info["flow"] != 0]

distance = {}

for start_valve in valve_info:
    queue = [(start_valve, 1)]
    seen = set([start_valve])

    distance[start_valve] = {}

    while queue:
        current_valve, dist = queue.pop(0)
        distance[start_valve][current_valve] = dist
        for connected_valve in valve_info[current_valve]["connections"]:
            if connected_valve not in seen:
                seen.add(connected_valve)
                queue.append((connected_valve, dist + 1))


def part1():
    start_valve = "AA"

    result = 0
    traversals = [[[], start_valve, 0, 0]]
    while traversals:
        valves, current_valve, current_minutes, current_result = traversals.pop(0)

        result = max(result, current_result)

        for non_zero_valve in non_zero_valves:
            if non_zero_valve not in valves:
                total_minutes = current_minutes + distance[current_valve][non_zero_valve]
                total_result = current_result + (30 - total_minutes) * valve_info[non_zero_valve]["flow"]
                if total_minutes < 30:
                    traversals.append([valves + [non_zero_valve], non_zero_valve, total_minutes, total_result])
    return result


def part1_smart():
    start_valve = "AA"
    dp = [[] for _ in range(30)]

    result = 0

    for valve in non_zero_valves:
        dist = distance[start_valve][valve]
        amount = (30 - dist) * valve_info[valve]["flow"]

        entry = ([valve], amount)
        dp[dist].append(entry)

    for idx, entries in enumerate(dp):
        for valve_lst, value in entries:
            for non_zero in non_zero_valves:
                if non_zero in valve_lst:
                    continue
                new_dist = idx + distance[valve_lst[-1]][non_zero]

                if new_dist >= 30:
                    continue

                new_amount = value + (30 - new_dist) * valve_info[non_zero]["flow"]

                result = max(result, new_amount)

                entry = (valve_lst + [non_zero], new_amount)
                dp[new_dist].append(entry)
    return result


def part2_smart():
    start_valve = "AA"
    dp = [[[] for _ in range(26)] for _ in range(26)]

    result = 0
    for valve in non_zero_valves:
        dist = distance[start_valve][valve]
        amount = (26 - dist) * valve_info[valve]["flow"]

        dp[dist][0].append((amount, [valve], []))
        dp[0][dist].append((amount, [], [valve]))

    for row_idx, row in enumerate(dp):
        for col_idx, col in enumerate(row):
            for value, row_valve_list, col_valve_list in col:
                for non_zero in non_zero_valves:
                    if non_zero in row_valve_list or non_zero in col_valve_list:
                        continue
                    row_item = row_valve_list[-1] if row_valve_list else start_valve
                    new_row_dist = row_idx + distance[row_item][non_zero]
                    if new_row_dist < 26:
                        new_row_amount = value + (26 - new_row_dist) * valve_info[non_zero]["flow"]
                        result = max(result, new_row_amount)
                        entry = (new_row_amount, row_valve_list + [non_zero], col_valve_list)
                        dp[new_row_dist][col_idx].append(entry)
                        dp[new_row_dist][col_idx] = sorted(dp[new_row_dist][col_idx], reverse=True)[:50]
                    col_item = col_valve_list[-1] if col_valve_list else start_valve
                    new_col_dist = col_idx + distance[col_item][non_zero]
                    if new_col_dist < 26:
                        new_col_amount = value + (26 - new_col_dist) * valve_info[non_zero]["flow"]
                        result = max(result, new_col_amount)
                        entry = (new_col_amount, row_valve_list, col_valve_list + [non_zero])
                        dp[row_idx][new_col_dist].append(entry)
                        dp[row_idx][new_col_dist] = sorted(dp[row_idx][new_col_dist], reverse=True)[:50]
    return result


start = time.time()
print(part1_smart(), time.time() - start)
start = time.time()
print(part1(), time.time() - start)
start = time.time()
print(part2_smart(), time.time() - start)