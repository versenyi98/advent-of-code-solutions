#pragma once

#include <map>
#include <string>
#include <vector>

#include "cell.hpp"

class Grid {
public:
    static Grid parse(const std::vector<std::string> &lines);

    int get_sum_of_risk_levels();
    void reset();

    void scale_by_5();
private:
    explicit Grid(const std::map<std::pair<int, int>, Cell> &cells, int width, int height);

    std::map<std::pair<int, int>, Cell> m_cells;
    int m_width;
    int m_height;

    struct WeightedRouteNode {
        explicit WeightedRouteNode(const std::pair<int, int> position, int weight) : m_position(position), m_weight(weight) {
        }

        bool operator<(const WeightedRouteNode& other) const {
            return m_weight > other.m_weight;
        }

        std::pair<int, int> m_position;
        int m_weight;
    };
};