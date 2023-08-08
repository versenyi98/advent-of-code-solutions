#include <iostream>
#include <string>
#include <algorithm>

#include "seven_segment_display.hpp"

int main() {
    std::string line;

    long long part1 = 0;
    long long part2 = 0;

    while (std::getline(std::cin, line)) {
        SevenSegmentDisplay seven_segment_display = SevenSegmentDisplay::parse(line);
        auto results = seven_segment_display.solve();

        part1 += std::count_if(begin(results), end(results), [](int n) {
            return n == 1 || n == 4 || n == 7 || n == 8;
        });

        part2 += 1000 * results[0] + 100 * results[1] + 10 * results[2] + results[3];
    }

    std::cout << part1 << std::endl;
    std::cout << part2 << std::endl;

    return 0;
}