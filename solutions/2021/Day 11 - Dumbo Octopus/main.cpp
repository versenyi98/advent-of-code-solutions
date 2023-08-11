#include <iostream>
#include <string>
#include <vector>

#include "octopus_grid.hpp"

int main() {
    std::string line;
    std::vector<std::string> lines;

    for (int i{}; i < 10; i++) {
        std::cin >> line;
        lines.push_back(line);
    }

    OctopusGrid octopus_grid = OctopusGrid::parse(lines);
    octopus_grid.simulate_until_sync();

    std::cout << octopus_grid.get_number_of_flashes_after_100_turns() << std::endl;
    std::cout << octopus_grid.get_turns_after_octopuses_synced() << std::endl;

    return 0;
}