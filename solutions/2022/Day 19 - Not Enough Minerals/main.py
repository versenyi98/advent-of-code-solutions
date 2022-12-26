import sys


lines = sys.stdin.read().split("\n")

configuration = []

for line in lines:
    line = line.split()
    ore_cost = int(line[6])
    cla_cost = int(line[12])
    ob_cost1 = int(line[18])
    ob_cost2 = int(line[21])
    ge_cost1 = int(line[27])
    ge_cost2 = int(line[30])

    configuration.append((
        ((ore_cost, 0, 0, 0), (1, 0, 0, 0)),
        ((cla_cost, 0, 0, 0), (0, 1, 0, 0)),
        ((ob_cost1, ob_cost2, 0, 0), (0, 0, 1, 0)),
        ((ge_cost1, 0, ge_cost2, 0), (0, 0, 0, 1)),
        ((0, 0, 0, 0), (0, 0, 0, 0))
    ))


start_state = ((1, 0, 0, 0), (0, 0, 0, 0))


def solve(part):
    result = 1 if part == 2 else 0
    conf = configuration
    if part == 2:
        conf = configuration[:3]
    for idx, config in enumerate(conf):
        print(f"\rConfig {idx + 1}/{len(conf)}", end="")
        queue = [start_state]
        for t in range(24 if part == 1 else 32):
            new_queue = []
            for robots, minerals in queue:
                if all(cost < mineral for cost, mineral in zip(config[3][0], minerals)):
                    new_queue.append((
                        tuple(robot + new_robot for robot, new_robot in zip(robots, new_robots)),
                        tuple(mineral - cost + robot for mineral, cost, robot in zip(minerals, costs, robots))
                    ))
                else:
                    for costs, new_robots in config:
                        if all(cost <= mineral for cost, mineral in zip(costs, minerals)):
                            new_queue.append((
                                tuple(robot + new_robot for robot, new_robot in zip(robots, new_robots)),
                                tuple(mineral - cost + robot for mineral, cost, robot in zip(minerals, costs, robots))
                            ))
            queue = sorted(new_queue, reverse=True, key=lambda e: tuple(zip(e[1][::-1], e[0][::-1])))[:2000 if part == 1 else 10000]
        if part == 1:
            result += max(minerals[3] for _, minerals in queue) * (idx + 1)
        else:
            result *= max(minerals[3] for _, minerals in queue)
    print()
    return result


print(solve(1))
print(solve(2))

