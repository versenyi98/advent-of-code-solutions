#include <iostream>
#include <string>
#include <vector>

#include "polymerization_equipment.hpp"

int main() {
    std::string line;
    std::vector<std::string> lines;

    while (std::getline(std::cin, line)) {
        lines.push_back(line);
    }

    PolymerizationEquipment polymerization_equipment = PolymerizationEquipment::parse(lines);

    std::cout << polymerization_equipment.get_frequency_diff_after_rounds(10) << std::endl;
    std::cout << polymerization_equipment.get_frequency_diff_after_rounds(40) << std::endl;

    return 0;
}