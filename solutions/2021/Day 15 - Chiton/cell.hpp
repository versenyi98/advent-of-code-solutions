#pragma once

class Cell {
public:
    explicit Cell(int risk = 0) : m_risk(risk), m_visited(false) {
        
    }

    inline void visit() {
        m_visited = true;
    }
    inline void clear_visited() {
        m_visited = false;
    }
    inline int get_risk() const {
        return m_risk;
    }
    inline bool is_visited() const {
        return m_visited;
    }

private:
    int m_risk;
    bool m_visited;
};