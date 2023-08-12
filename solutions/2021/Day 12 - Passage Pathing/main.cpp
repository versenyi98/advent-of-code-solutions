#include <iostream>
#include <string>

#include "graph.hpp"

int main() {
    std::string line;
    std::vector<std::string> lines;

    while (std::getline(std::cin, line)) {
        lines.push_back(line);
    }

    Graph graph = Graph::parse(lines);
    std::cout << graph.get_number_of_routes_from_start_to_finish() << std::endl;
    std::cout << graph.get_number_of_routes_with_multiple_small_caves() << std::endl;
    return 0;
}