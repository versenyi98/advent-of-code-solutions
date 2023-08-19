#pragma once

#include <memory>
#include <string>

class SnailfishLiteral;

class Snailfish : public std::enable_shared_from_this<Snailfish> {
public:
    static std::shared_ptr<Snailfish> parse(const std::string &line);
    explicit Snailfish() : m_left(nullptr), m_right(nullptr) {}
    explicit Snailfish(const std::shared_ptr<Snailfish> &left, const std::shared_ptr<Snailfish> &right) : m_left(left), m_right(right) {}

    void set_parent(const std::shared_ptr<Snailfish> &parent) {
        m_parent = parent;
    }

    virtual std::string inorder() const;
    virtual int get_magnitude() const;

    friend std::shared_ptr<Snailfish> operator+(const std::shared_ptr<Snailfish> &lhs, const std::shared_ptr<Snailfish> &rhs);

protected:
    void reduce();

    bool apply_single_split();
    bool apply_single_explode(int depth = 0);

    virtual bool should_split() const;
    virtual bool should_explode(int depth = 0) const;

    std::shared_ptr<SnailfishLiteral> get_neighbour_to_right();
    std::shared_ptr<SnailfishLiteral> get_neighbour_to_left();

private:
    static std::shared_ptr<Snailfish> split(const std::shared_ptr<Snailfish> &snailfish);

    std::weak_ptr<Snailfish> m_parent;
    std::shared_ptr<Snailfish> m_left;
    std::shared_ptr<Snailfish> m_right;
};