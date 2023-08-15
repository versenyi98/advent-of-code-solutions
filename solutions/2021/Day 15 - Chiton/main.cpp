#include <iostream>

#include <vector>
#include <string>

#include "grid.hpp"

int main() {

    std::string line;
    std::vector<std::string> lines;

    while (std::getline(std::cin, line)) {
        lines.push_back(line);
    }

    Grid grid = Grid::parse(lines);

    std::cout << grid.get_sum_of_risk_levels() << std::endl;
    grid.reset();
    grid.scale_by_5();
    std::cout << grid.get_sum_of_risk_levels() << std::endl;
    
    return 0;
}