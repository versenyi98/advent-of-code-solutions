#include "literal_snailfish.hpp"

bool SnailfishLiteral::should_split() const {
    return m_value >= 10;
}

bool SnailfishLiteral::should_explode(int depth) const {
    return false;
}

std::string SnailfishLiteral::inorder() const {
    return std::to_string(m_value);
}

int SnailfishLiteral::get_magnitude() const {
    return m_value;
}