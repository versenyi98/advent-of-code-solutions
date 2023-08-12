#pragma once

#include <memory>
#include <string>
#include <vector>

class Node {
public:
    Node(const std::string &name);

    int get_visit_count() const;
    void leave();
    void visit();

    void add_neighbour(std::shared_ptr<Node> node);

    std::vector<std::shared_ptr<Node>> get_neighbours() const;

private:
    std::vector<std::shared_ptr<Node>> m_neighbours;
    std::string m_name;
    bool m_is_big;
    int m_visit_count;
};

class NodeVisitor {
public:
    explicit NodeVisitor(std::shared_ptr<Node> &node) : m_node(node) {
        m_node->visit();
    }

    ~NodeVisitor() {
        m_node->leave();
    }

private:
    std::shared_ptr<Node> &m_node;
};