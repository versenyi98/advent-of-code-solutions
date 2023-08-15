#include "grid.hpp"

#include <queue>
#include <iostream>

Grid Grid::parse(const std::vector<std::string> &lines) {
    std::map<std::pair<int, int>, Cell> cells;

    for (int row{}; row < lines.size(); row++) {
        for (int col{}; col < lines[row].size(); col++) {
            cells[{row, col}] = Cell(lines[row][col] - '0');
        }
    }

    return Grid(cells, lines[0].size(), lines.size());
}

Grid::Grid(const std::map<std::pair<int, int>, Cell> &cells, int width, int height) : m_cells(cells), m_width(width), m_height(height) {
}

void Grid::reset() {
    for (auto &[position, cell] : m_cells) {
        cell.clear_visited();
    }
}

void Grid::scale_by_5() {
    for (int row{}; row < m_height; row++) {
        for (int col{}; col < m_width; col++) {
            int original_risk_value = m_cells[{row, col}].get_risk();
            for (int tile_diff_row{0}; tile_diff_row < 5; tile_diff_row++) {
                for (int tile_diff_col{0}; tile_diff_col < 5; tile_diff_col++) {
                    if (tile_diff_col == 0 && tile_diff_row == 0) {
                        continue;
                    }

                    int new_risk_value = original_risk_value + tile_diff_col + tile_diff_row;
                    if (new_risk_value > 9) {
                        new_risk_value = new_risk_value % 9;
                    }

                    m_cells[{row + tile_diff_row * m_height, col + tile_diff_col * m_width}] = Cell(new_risk_value);
                }
            }
        }
    }

    m_width *= 5;
    m_height *= 5;
}

int Grid::get_sum_of_risk_levels() {
    std::priority_queue<WeightedRouteNode> pq;
    pq.push(WeightedRouteNode({0, 0}, 0));

    std::vector<std::pair<int, int>> neighbours = {
        {+1, 0}, {-1, 0}, {0, -1}, {0, +1}};

    while (pq.size()) {
        WeightedRouteNode top = pq.top();
        pq.pop();

        Cell &cell = m_cells[top.m_position];

        if (cell.is_visited()) {
            continue;
        }

        if (top.m_position.first == m_height - 1 && top.m_position.second == m_width - 1) {
            return top.m_weight;
        }

        cell.visit();

        for (auto [d_row, d_col] : neighbours) {
            int new_row = d_row + top.m_position.first;
            int new_col = d_col + top.m_position.second;

            if (new_row >= m_height || new_row < 0 || new_col >= m_width || new_col < 0) {
                continue;
            }

            Cell &neighbour = m_cells[{new_row, new_col}];

            if (neighbour.is_visited()) {
                continue;
            }

            pq.push(WeightedRouteNode({new_row, new_col}, top.m_weight + neighbour.get_risk()));
        }
    }

    return 0;
}