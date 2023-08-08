#include "cave_heightmap.hpp"

#include <algorithm>
#include <queue>

CaveHeightMap::CaveHeightMap(std::vector<std::vector<int>> &&heightmap) : m_heightmap(heightmap), m_rows(heightmap.size()), m_cols(heightmap[0].size()) {
}

bool CaveHeightMap::in_bounds(int row, int col) const {
    return row >= 0 && row < m_rows && col >= 0 && col < m_cols;
}

CaveHeightMap CaveHeightMap::parse(const std::vector<std::string> &lines) {
    std::vector<std::vector<int>> heightmap(lines.size());

    std::transform(begin(lines), end(lines), begin(heightmap), begin(heightmap), [](const std::string &line, std::vector<int> &v) {
        std::for_each(begin(line), end(line), [&v](char ch) {
            v.push_back(static_cast<int>(ch - '0'));
        });

        return v;
    });

    return CaveHeightMap(std::move(heightmap));
}

int CaveHeightMap::get_risk_level() const {
    std::vector<std::pair<int, int>> neighbours = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int risk_level = 0;

    for (int row{}; row < m_rows; row++) {
        for (int col{}; col < m_cols; col++) {
            bool is_low_point = std::all_of(begin(neighbours), end(neighbours), [this, row, col](const std::pair<int, int> &neighbour) {
                auto [d_row, d_col] = neighbour;
                int new_row = row + d_row;
                int new_col = col + d_col;

                return !in_bounds(new_row, new_col) || m_heightmap[row][col] < m_heightmap[new_row][new_col];
            });

            if (is_low_point) {
                risk_level += m_heightmap[row][col] + 1;
            }
        }
    }

    return risk_level;
}

std::vector<int> CaveHeightMap::get_largest_basins(int n) const {
    std::vector<int> basin_sizes;
    std::vector<int> result;

    std::vector<std::pair<int, int>> neighbours = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    std::vector<std::vector<int>> heightmap_copy;
    std::copy(begin(m_heightmap), end(m_heightmap), std::back_inserter(heightmap_copy));

    for (int row{}; row < m_rows; row++) {
        for (int col{}; col < m_cols; col++) {
            if (heightmap_copy[row][col] == 9) {
                continue;
            }

            int basin_size = 0;
            std::queue<std::pair<int, int>> q;

            q.push({row, col});

            while (q.size()) {
                basin_size++;

                std::pair<int, int> front = q.front();
                q.pop();

                auto [f_row, f_col] = front;
                heightmap_copy[f_row][f_col] = 9;

                std::for_each(begin(neighbours), end(neighbours), [this, &heightmap_copy, f_row, f_col, &q](const std::pair<int, int> &neighbour) {
                    auto [d_row, d_col] = neighbour;
                    int new_row = f_row + d_row;
                    int new_col = f_col + d_col;

                    if (in_bounds(new_row, new_col) && heightmap_copy[new_row][new_col] != 9) {
                        heightmap_copy[new_row][new_col] = 9;
                        q.push({new_row, new_col});
                    }
                });
            }
            basin_sizes.push_back(basin_size);
        }
    }

    std::partial_sort(begin(basin_sizes), begin(basin_sizes) + n, end(basin_sizes), std::greater<int>());
    std::copy_n(begin(basin_sizes), n, std::back_inserter(result));

    return result;
}
