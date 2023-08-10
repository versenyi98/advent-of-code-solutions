#include <iostream>
#include <string>
#include <vector>

#include "syntax_scoring.hpp"

int main() {

    std::string line;
    std::vector<std::string> lines;

    while (std::getline(std::cin, line)) {
        lines.push_back(line);
    }

    SyntaxScoring syntax_scoring(std::move(lines));

    std::cout << syntax_scoring.calculate_syntax_error_score() << std::endl;
    std::cout << syntax_scoring.calculate_autocomplete_score() << std::endl;

    return 0;
}