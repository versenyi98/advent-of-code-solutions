#pragma once

#include "snailfish.hpp"

class SnailfishLiteral : public Snailfish {
public:
    explicit SnailfishLiteral(int value) : Snailfish(), m_value(value) {}

    virtual std::string inorder() const;
    virtual int get_magnitude() const;

    int get_value() const {
        return m_value;
    }

    void increase_value(int increment) {
        m_value += increment;
    }

protected:
    virtual bool should_split() const;
    virtual bool should_explode(int depth) const;

private:
    int m_value;
};
