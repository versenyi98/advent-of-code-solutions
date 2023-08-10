#include "syntax_scoring.hpp"

#include <iostream>

#include <algorithm>
#include <numeric>

const std::map<char, char> SyntaxScoring::character_mapping = {
    {'(', ')'},
    {'[', ']'},
    {'<', '>'},
    {'{', '}'}};

SyntaxScoring::SyntaxScoring(const std::vector<std::string> &&lines) : m_lines(lines) {
}

int SyntaxScoring::calculate_syntax_error_score() const {
    std::map<char, int> points = {
        {')', 3},
        {']', 57},
        {'}', 1197},
        {'>', 25137}};

    std::vector<std::string> corrupted;
    std::copy_if(m_lines.cbegin(), m_lines.cend(), std::back_inserter(corrupted), [this](const std::string &line) {
        return this->find_first_corrupted(line) != ' ';
    });

    int result = std::accumulate(corrupted.begin(), corrupted.end(), 0, [this, points](int current, const std::string &line) {
        auto it = points.find(this->find_first_corrupted(line));
        return current += it->second;
    });

    return result;
}

long long SyntaxScoring::calculate_autocomplete_score() const {
    std::map<char, long long> points = {
        {')', 1ll},
        {']', 2ll},
        {'}', 3ll},
        {'>', 4ll}};

    std::vector<std::string> incomplete;
    std::copy_if(m_lines.cbegin(), m_lines.cend(), std::back_inserter(incomplete), [this](const std::string &line) {
        return this->find_first_corrupted(line) == ' ';
    });


    std::vector<long long> scores;
    std::transform(incomplete.cbegin(), incomplete.cend(), std::back_inserter(scores), [this, points](const std::string& line) {
        std::stack<char> closing_sequence = this->get_closing_sequence(line);
        long long score = 0;

        while (closing_sequence.size()) {
            char top = closing_sequence.top();
            closing_sequence.pop();

            score *= 5ll;
            score += points.at(top);
        }

        return score;
    });

    int middle = scores.size() / 2ll;
    std::nth_element(begin(scores), begin(scores) + middle, end(scores));

    return scores[middle];
}

char SyntaxScoring::find_first_corrupted(const std::string &line) const {
    std::stack<char> stack;

    for (char ch : line) {
        auto it = character_mapping.find(ch);
        bool is_closing = it == character_mapping.end();

        if (is_closing) {
            if (stack.size() > 0 && stack.top() == ch) {
                stack.pop();
            } else {
                return ch;
            }
        } else {
            stack.push(it->second);
        }
    }

    return ' ';
}

std::stack<char> SyntaxScoring::get_closing_sequence(const std::string &line) const {
    std::stack<char> stack;

    for (char ch : line) {
        auto it = character_mapping.find(ch);
        bool is_closing = it == character_mapping.end();

        if (is_closing) {
            stack.pop();
        } else {
            stack.push(it->second);
        }
    }

    return stack;
}
