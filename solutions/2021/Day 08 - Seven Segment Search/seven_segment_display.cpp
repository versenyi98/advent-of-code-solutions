#include "seven_segment_display.hpp"

#include <algorithm>
#include <functional>
#include <iostream>
#include <sstream>

SevenSegmentDisplay::SevenSegmentDisplay(const std::vector<std::string> &&signal_patterns, const std::vector<std::string> &&output_values) : m_signal_patterns(signal_patterns), m_output_values(output_values) {
    sort_elements(m_signal_patterns);
    sort_elements(m_output_values);
}

SevenSegmentDisplay SevenSegmentDisplay::parse(const std::string &line) {
    std::vector<std::string> signal_patterns, output_values;

    std::stringstream ss(line);
    std::string token;
    std::vector<std::string> tokens;

    while (std::getline(ss, token, ' ')) {
        tokens.push_back(token);
    }

    auto delimiter_pos = std::find(begin(tokens), end(tokens), "|");

    std::copy(begin(tokens), delimiter_pos, std::back_inserter(signal_patterns));
    std::copy(delimiter_pos + 1, end(tokens), std::back_inserter(output_values));

    return SevenSegmentDisplay(std::move(signal_patterns), std::move(output_values));
}

const std::string SevenSegmentDisplay::find_signal_with_length(int length) const {
    return *std::find_if(begin(m_signal_patterns), end(m_signal_patterns), [length](const std::string &signal) {
        return signal.length() == length;
    });
}

const char SevenSegmentDisplay::find_first_different_char(const std::string &str, const std::string &pattern) const {
    return *std::find_if(begin(str), end(str), [pattern](char ch) {
        return pattern.find(ch) == std::string::npos;
    });
}

const std::string SevenSegmentDisplay::find_signal_with_length_and_segments(int length, const std::string &segments) const {
    auto is_subset = [](const std::string &first, const std::string &second) {
        return std::includes(begin(first), end(first), begin(second), end(second));
    };

    return *std::find_if(begin(m_signal_patterns), end(m_signal_patterns), [length, is_subset, segments](const std::string &signal) {
        return signal.length() == length && is_subset(signal, segments);
    });
}

std::vector<int> SevenSegmentDisplay::solve() {
    std::vector<std::string> signals(10);

    signals[1] = find_signal_with_length(2);
    signals[4] = find_signal_with_length(4);
    signals[7] = find_signal_with_length(3);
    signals[8] = find_signal_with_length(7);
    signals[9] = find_signal_with_length_and_segments(6, signals[4]);
    signals[3] = find_signal_with_length_and_segments(5, signals[7]);

    char top = find_first_different_char(signals[7], signals[1]);
    char bottom = find_first_different_char(signals[9], signals[4] + top);
    char center = find_first_different_char(signals[3], signals[7] + bottom);
    char b_left = find_first_different_char(signals[8], signals[9]);
    char t_left = find_first_different_char(signals[4], signals[1] + center);

    std::string five_pattern = std::string(1, center) + top + bottom + t_left;
    std::sort(begin(five_pattern), end(five_pattern));

    signals[5] = find_signal_with_length_and_segments(5, five_pattern);

    char b_right = find_first_different_char(signals[5], std::string(1, center) + top + bottom + t_left);
    char t_right = find_first_different_char(signals[8], signals[5] + b_left);

    signals[0] = std::string(1, top) + bottom + t_left + b_left + t_right + b_right;
    signals[2] = std::string(1, top) + bottom + center + b_left + t_right;
    signals[6] = std::string(1, top) + bottom + center + t_left + b_left + b_right;

    sort_elements(signals);

    std::vector<int> result;
    std::transform(begin(m_output_values), end(m_output_values), std::back_inserter(result), [signals](const std::string &output) {
        return std::distance(begin(signals), std::find(begin(signals), end(signals), output));
    });

    return result;
}
