#pragma once

#include <string>
#include <vector>
#include <map>
#include <stack>

class SyntaxScoring {
public:
    explicit SyntaxScoring(const std::vector<std::string> &&lines);

    int calculate_syntax_error_score() const;
    long long calculate_autocomplete_score() const;

private:
    char find_first_corrupted(const std::string &line) const;
    std::stack<char> get_closing_sequence(const std::string &line) const;

    std::vector<std::string> m_lines;

    static const std::map<char, char> character_mapping;
};