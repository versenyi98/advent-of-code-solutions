#include "graph.hpp"

#include <map>
#include <string>

Graph Graph::parse(const std::vector<std::string> &lines) {
    std::map<std::string, std::shared_ptr<Node>> nodes_by_name;

    auto get_ptr_of_node = [&nodes_by_name](const std::string &name) {
        if (nodes_by_name.find(name) == nodes_by_name.end()) {
            nodes_by_name[name] = std::make_shared<Node>(name);
        }

        return nodes_by_name[name];
    };

    for (auto &line : lines) {
        auto dash_pos = line.find('-');
        std::string src_name = line.substr(0, dash_pos);
        std::string dst_name = line.substr(dash_pos + 1);

        std::shared_ptr<Node> src_node = get_ptr_of_node(src_name);
        std::shared_ptr<Node> dst_node = get_ptr_of_node(dst_name);

        src_node->add_neighbour(dst_node);
        dst_node->add_neighbour(src_node);
    }

    return Graph(nodes_by_name["start"], nodes_by_name["end"]);
}

int Graph::dfs(std::shared_ptr<Node> &node, bool allow_multiple_caves) {
    NodeVisitor visitor(node);

    int result = 0;

    for (auto &neighbour : node->get_neighbours()) {
        if (neighbour == m_start) {
            continue;
        }

        if (neighbour == m_end) {
            result++;
            continue;
        }

        if (neighbour->get_visit_count() == 0) {
            result += dfs(neighbour, allow_multiple_caves);
        } else if (allow_multiple_caves) {
            result += dfs(neighbour, false);
        }
    }

    return result;
}

int Graph::get_number_of_routes_from_start_to_finish() {
    return dfs(m_start, false);
}

int Graph::get_number_of_routes_with_multiple_small_caves() {
    return dfs(m_start, true);
}

Graph::Graph(const auto &start, const auto &end) : m_start(start), m_end(end) {
}
