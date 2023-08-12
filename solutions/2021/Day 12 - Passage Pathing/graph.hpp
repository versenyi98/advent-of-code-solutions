#pragma once

#include <memory>

#include "node.hpp"

class Graph {
public:
    static Graph parse(const std::vector<std::string> &lines);

    int get_number_of_routes_from_start_to_finish();
    int get_number_of_routes_with_multiple_small_caves();

private:
    explicit Graph(const auto &start, const auto &end);

    int dfs(std::shared_ptr<Node> &node, bool allow_multiple_caves);

    std::shared_ptr<Node> m_start;
    std::shared_ptr<Node> m_end;
};