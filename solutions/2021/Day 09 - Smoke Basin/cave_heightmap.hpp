#pragma once

#include <string>
#include <vector>

class CaveHeightMap {
public:
    static CaveHeightMap parse(const std::vector<std::string> &lines);
    int get_risk_level() const;
    std::vector<int> get_largest_basins(int n) const;

private:
    CaveHeightMap(std::vector<std::vector<int>> &&heightmap);

    bool in_bounds (int row, int col) const;

    std::vector<std::vector<int>> m_heightmap;
    int m_rows;
    int m_cols;
};