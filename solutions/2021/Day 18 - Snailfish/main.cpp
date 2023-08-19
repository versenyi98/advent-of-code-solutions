#include <iostream>
#include <vector>

#include "snailfish.hpp"

int main() {
    std::string line;

    std::vector<std::string> lines;

    std::shared_ptr<Snailfish> sum = nullptr;

    while (std::getline(std::cin, line)) {
        lines.push_back(line);
    }

    for (auto line : lines) {
        if (sum) {
            sum = sum + Snailfish::parse(line);
        } else {
            sum = Snailfish::parse(line);
        }
    }

    std::cout << sum->get_magnitude() << std::endl;

    int maximum = 0;

    for (auto line1 : lines) {
        for (auto line2 : lines) {
            if (line1 == line2) {
                continue;
            }

            auto sum1 = Snailfish::parse(line1) + Snailfish::parse(line2);
            auto sum2 = Snailfish::parse(line2) + Snailfish::parse(line1);

            maximum = std::max(maximum, std::max(sum1->get_magnitude(), sum2->get_magnitude()));
        }
    }

    std::cout << maximum << std::endl;

    return 0;
}