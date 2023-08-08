#include <iostream>

#include <numeric>
#include <string>
#include <vector>

#include "cave_heightmap.hpp"

int main() {

    std::string line;
    std::vector<std::string> lines;

    while (std::getline(std::cin, line)) {
        lines.push_back(line);
    }

    CaveHeightMap heightmap = CaveHeightMap::parse(lines);

    std::cout << heightmap.get_risk_level() << std::endl;

    std::vector<int> top_3_basins = heightmap.get_largest_basins(3);

    std::cout << std::accumulate(begin(top_3_basins), end(top_3_basins), 1, std::multiplies<int>()) << std::endl;

    return 0;
}