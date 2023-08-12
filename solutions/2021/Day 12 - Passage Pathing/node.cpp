#include "node.hpp"

Node::Node(const std::string &name) : m_name(name), m_is_big(isupper(name[0])), m_visit_count(false) {
}

int Node::get_visit_count() const {
    return m_visit_count;
}

void Node::leave() {
    if (!m_is_big) {
        m_visit_count--;
    }
}

void Node::visit() {
    if (!m_is_big) {
        m_visit_count++;
    }
}

void Node::add_neighbour(std::shared_ptr<Node> node) {
    m_neighbours.push_back(node);
}

std::vector<std::shared_ptr<Node>> Node::get_neighbours() const {
    return m_neighbours;
}
