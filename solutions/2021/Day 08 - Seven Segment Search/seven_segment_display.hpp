#pragma once

#include <set>
#include <string>
#include <vector>

class SevenSegmentDisplay {
public:
    static SevenSegmentDisplay parse(const std::string &line);

    std::vector<int> solve();

private:
    SevenSegmentDisplay(const std::vector<std::string> &&signal_patterns, const std::vector<std::string> &&output_values);

    std::vector<std::string> m_signal_patterns;
    std::vector<std::string> m_output_values;

    const std::string find_signal_with_length(int length) const;
    const char find_first_different_char(const std::string& str, const std::string& pattern) const;
    const std::string find_signal_with_length_and_segments(int length, const std::string& segments) const;

    inline void sort_elements(std::vector<std::string>& v) {
        std::for_each(begin(v), end(v), [](std::string &str) {
            std::sort(begin(str), end(str));
        });
    }
};