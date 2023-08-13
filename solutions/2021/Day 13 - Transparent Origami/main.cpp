#include <iostream>
#include <string>
#include <vector>

#include "transparent_paper.hpp"

int main() {
    std::string line;
    std::vector<std::string> lines;

    while (std::getline(std::cin, line)) {
        lines.push_back(line);
    }

    TransparentPaper transparent_paper = TransparentPaper::parse(lines);
    std::vector<int> point_count = transparent_paper.get_number_of_points_after_each_turn();

    std::cout << point_count[0] << std::endl;
    transparent_paper.print();

    return 0;
}