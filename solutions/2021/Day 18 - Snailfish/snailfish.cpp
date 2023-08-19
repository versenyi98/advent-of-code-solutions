#include "snailfish.hpp"
#include "literal_snailfish.hpp"

#include <algorithm>
#include <iostream>

std::shared_ptr<Snailfish> Snailfish::parse(const std::string &line) {
    if (std::all_of(begin(line), end(line), [](char ch) { return isdigit(ch); })) {
        return std::make_shared<SnailfishLiteral>(std::stoi(line));
    }

    int bracket_count = 0;
    auto comma = std::find_if(begin(line), end(line), [&bracket_count](char ch) {
        if (ch == '[') {
            bracket_count++;
        } else if (ch == ']') {
            bracket_count--;
        }

        return bracket_count == 1 && ch == ',';
    });

    int comma_pos = std::distance(begin(line), comma);
    std::shared_ptr<Snailfish> left = Snailfish::parse(line.substr(1, comma_pos - 1));
    std::shared_ptr<Snailfish> right = Snailfish::parse(line.substr(comma_pos + 1, line.size() - comma_pos - 2));

    std::shared_ptr<Snailfish> result = std::make_shared<Snailfish>(left, right);
    left->set_parent(result);
    right->set_parent(result);

    return result;
}

std::string Snailfish::inorder() const {
    return "[" + m_left->inorder() + "," + m_right->inorder() + "]";
}

int Snailfish::get_magnitude() const {
    return 3 * m_left->get_magnitude() + 2 * m_right->get_magnitude();
}

std::shared_ptr<Snailfish> Snailfish::split(const std::shared_ptr<Snailfish> &snailfish) {
    std::shared_ptr<SnailfishLiteral> snailfish_literal = std::static_pointer_cast<SnailfishLiteral>(snailfish);

    int left_value = snailfish_literal->get_value() / 2;
    int right_value = snailfish_literal->get_value() - left_value;
    return std::make_shared<Snailfish>(
        std::make_shared<SnailfishLiteral>(left_value),
        std::make_shared<SnailfishLiteral>(right_value));
}

void Snailfish::reduce() {
    while (apply_single_explode() || apply_single_split()) {
    }
}

bool Snailfish::apply_single_split() {
    if (!m_right && !m_left) {
        return false;
    }

    if (m_left->should_split()) {
        auto new_left = Snailfish::split(m_left);
        new_left->set_parent(shared_from_this());
        m_left = new_left;
        return true;
    }

    if (m_left->apply_single_split()) {
        return true;
    }

    if (m_right->should_split()) {
        auto new_right = Snailfish::split(m_right);
        new_right->set_parent(shared_from_this());
        m_right = new_right;
        return true;
    } else if (m_right->apply_single_split()) {
        return true;
    }

    return false;
}

bool Snailfish::apply_single_explode(int depth) {
    if (m_left && m_left->apply_single_explode(depth + 1)) {
        return true;
    }

    if (m_right && m_right->apply_single_explode(depth + 1)) {
        return true;
    }

    if (should_explode(depth)) {
        auto right_neighbour = get_neighbour_to_right();
        if (right_neighbour) {
            auto right = std::static_pointer_cast<SnailfishLiteral>(m_right);
            right_neighbour->increase_value(right->get_value());
        }

        auto left_neighbour = get_neighbour_to_left();
        if (left_neighbour) {
            auto left = std::static_pointer_cast<SnailfishLiteral>(m_left);
            left_neighbour->increase_value(left->get_value());
        }

        std::shared_ptr<SnailfishLiteral> new_value = std::make_shared<SnailfishLiteral>(0);
        new_value->set_parent(m_parent.lock());

        if (m_parent.lock()->m_left.get() == this) {
            m_parent.lock()->m_left = new_value;
        } else {
            m_parent.lock()->m_right = new_value;
        }

        return true;
    }

    return false;
}

bool Snailfish::should_split() const {
    return false;
}

bool Snailfish::should_explode(int depth) const {
    return depth >= 4;
}

std::shared_ptr<SnailfishLiteral> Snailfish::get_neighbour_to_right() {
    std::shared_ptr<Snailfish> current = m_parent.lock();
    std::shared_ptr<Snailfish> previous = shared_from_this();

    while (current && current->m_right == previous) {
        previous = current;
        current = current->m_parent.lock();
    }

    if (!current) {
        return std::shared_ptr<SnailfishLiteral>();
    }

    current = current->m_right;

    while (current->m_left) {
        current = current->m_left;
    }

    return std::static_pointer_cast<SnailfishLiteral>(current);
}

std::shared_ptr<SnailfishLiteral> Snailfish::get_neighbour_to_left() {
    std::shared_ptr<Snailfish> current = m_parent.lock();
    std::shared_ptr<Snailfish> previous = shared_from_this();

    while (current && current->m_left == previous) {
        previous = current;
        current = current->m_parent.lock();
    }

    if (!current) {
        return std::shared_ptr<SnailfishLiteral>();
    }

    current = current->m_left;

    while (current->m_right) {
        current = current->m_right;
    }

    return std::static_pointer_cast<SnailfishLiteral>(current);
}

std::shared_ptr<Snailfish> operator+(const std::shared_ptr<Snailfish> &lhs, const std::shared_ptr<Snailfish> &rhs) {
    auto result = std::make_shared<Snailfish>(lhs, rhs);
    lhs->set_parent(result);
    rhs->set_parent(result);

    result->reduce();

    return result;
}
