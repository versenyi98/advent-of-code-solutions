import sys
from itertools import combinations
import z3

def point_and_steps_to_slope_intercept(x1, y1, dx, dy):
    m = dy / dx

    b = y1 - m * x1

    return m, b

def find_intersection(line1, line2):
    m1, b1 = point_and_steps_to_slope_intercept(*line1[0], *line1[1])
    m2, b2 = point_and_steps_to_slope_intercept(*line2[0], *line2[1])

    if m1 == m2:
        return None

    x_intersection = (b2 - b1) / (m1 - m2)
    y_intersection = m1 * x_intersection + b1

    if ((x_intersection > line1[0][0]) == (line1[1][0] > 0)) and \
       ((x_intersection > line2[0][0]) == (line2[1][0] > 0)) and \
       ((y_intersection > line1[0][1]) == (line1[1][1] > 0)) and \
       ((y_intersection > line2[0][1]) == (line2[1][1] > 0)):
        return x_intersection, y_intersection

    return None

def main():
    lines = [l.strip('\n').split(' @ ') for l in sys.stdin.readlines()]
    stones = [(list(map(int, pos.split(', '))), list(map(int, velocity.split(', ')))) for [pos, velocity] in lines]

    def task1():
        bl = 200000000000000
        bu = 400000000000000
        count = 0

        for a, b in combinations(stones, 2):
            intersection = find_intersection(((a[0][0], a[0][1]), (a[1][0], a[1][1])), ((b[0][0], b[0][1]), (b[1][0], b[1][1])))
            if intersection:
                x, y = intersection

                if bl <= x <= bu and bl <= y <= bu:
                    count += 1
        print(count)

    def task2():
        r = z3.RealVector('r', 3)
        p = z3.RealVector('p', 3)
        time = z3.RealVector('t', len(stones))

        s = z3.Solver()
        for t, stone in zip(time, stones):
            for i in range(3):
                s.append(r[i] + p[i] * t == stone[0][i] + stone[1][i] * t)
        s.check()
        print(s.model().eval(sum(r)))

    task1()
    task2()

if __name__ == "__main__":
    main()