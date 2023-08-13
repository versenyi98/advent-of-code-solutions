#pragma once

#include <map>
#include <string>
#include <vector>

class TransparentPaper {
public:
    static TransparentPaper parse(const std::vector<std::string> &lines);

    std::vector<int> get_number_of_points_after_each_turn();
    void print() const;

private:
    explicit TransparentPaper(const auto &&points, const auto &&instructions);

    void fold(int coord);
    void fold_up(int coord);
    void fold_left(int coord);

    std::map<std::pair<int, int>, int> m_points;
    std::vector<int> m_instructions;

    int m_width;
    int m_height;
};