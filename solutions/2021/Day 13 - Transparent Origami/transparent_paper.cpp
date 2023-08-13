#include "transparent_paper.hpp"

#include <algorithm>
#include <iostream>

TransparentPaper TransparentPaper::parse(const std::vector<std::string> &lines) {
    auto separator = std::find(begin(lines), end(lines), "");

    std::map<std::pair<int, int>, int> points;
    std::for_each(begin(lines), separator, [&points](const std::string &line) {
        auto comma_pos = line.find(',');
        int x = std::stoi(line.substr(0, comma_pos));
        int y = std::stoi(line.substr(comma_pos + 1));

        points[{x, y}] = 1;
    });

    std::vector<int> instructions;
    std::for_each(separator + 1, end(lines), [&instructions](const std::string &line) {
        auto equal_pos = line.find('=');
        int factor = line[equal_pos - 1] == 'x' ? 1 : -1;
        int value = std::stoi(line.substr(equal_pos + 1));

        instructions.push_back(factor * value);
    });

    return TransparentPaper(std::move(points), std::move(instructions));
}

std::vector<int> TransparentPaper::get_number_of_points_after_each_turn() {
    std::vector<int> result;

    std::transform(begin(m_instructions), end(m_instructions), std::back_insert_iterator(result), [this](int instruction) {
        fold(instruction);

        return std::count_if(begin(m_points), end(m_points), [](const auto entry) {
            return entry.second > 0;
        });
    });

    return result;
}

TransparentPaper::TransparentPaper(const auto &&points, const auto &&instructions) : m_points(points), m_instructions(instructions) {
}

void TransparentPaper::fold(int coord) {
    if (coord < 0) {
        fold_up(-coord);
    } else {
        fold_left(coord);
    }
}

void TransparentPaper::fold_up(int coord) {
    m_height = coord;
    for (auto entry : m_points) {
        auto [point, valid] = entry;
        auto [x, y] = point;

        if (valid && y > coord) {
            m_points[point] = 0;
            m_points[{x, coord + coord - y}] = 1;
        }
    }
}

void TransparentPaper::fold_left(int coord) {
    m_width = coord;
    for (auto entry : m_points) {
        auto [point, valid] = entry;
        auto [x, y] = point;

        if (valid && x > coord) {
            m_points[point] = 0;
            m_points[{coord + coord - x, y}]++;
        }
    }
}

void TransparentPaper::print() const {
    for (int row{}; row < m_height; row++) {
        for (int col{}; col < m_width; col++) {
            if (auto it = m_points.find({col, row}); it != m_points.end() && it->second > 0) {
                std::cout << "#";
            } else {
                std::cout << " ";
            }
        }
        std::cout << std::endl;
    }
}