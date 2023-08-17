#include <iostream>
#include <map>
#include <set>

class Rectangle {
public:
    Rectangle(int x, int y, int width, int height) : m_x(x), m_y(y), m_width(width), m_height(height) {}

    int x() const {
        return m_x;
    }

    int y() const {
        return m_y;
    }

    int width() const {
        return m_width;
    }

    int height() const {
        return m_height;
    }

private:
    int m_x;
    int m_y;
    int m_width;
    int m_height;
};

int sum_of_numbers_from_1_to_n(int n) {
    return n * (n + 1) / 2;
}

int main() {
    Rectangle target(57, -148, 59, 50);
    // Rectangle target(20, -5, 10, 5);

    std::cout << sum_of_numbers_from_1_to_n(abs(target.y() - target.height()) - 1) << std::endl;

    std::map<int, std::set<int>> possibe_x_power_per_second;
    std::map<int, std::set<int>> possibe_y_power_per_second;

    int max_seconds = 0;

    for (int start_power = abs(target.y() - target.height()) - 1; start_power >= target.y() - target.height(); start_power--) {
        int seconds = 1;
        int power = start_power;
        int current_height = 0;

        while (current_height + power >= target.y() - target.height()) {
            current_height += power;
            if (current_height <= target.y()) {
                possibe_y_power_per_second[seconds].insert(start_power);
                max_seconds = std::max(seconds, max_seconds);
            }
            seconds++;
            power--;
        }
    }

    for (int start_power = target.x() + target.width(); start_power > 0; start_power--) {
        int seconds = 1;
        int current_distance = 0;

        for (int power = start_power; seconds <= max_seconds; power = std::max(0, power - 1), seconds++) {
            current_distance += power;

            if (current_distance >= target.x() && current_distance <= target.x() + target.width()) {
                possibe_x_power_per_second[seconds].insert(start_power);
            }
        }
    }

    std::set<std::pair<int, int>> possible_forces;
    for (auto [second, y_values] : possibe_y_power_per_second) {
        auto x_values = possibe_x_power_per_second[second];

        for (auto x : x_values) {
            for (auto y : y_values) {
                possible_forces.insert({x, y});
            }
        }
    }
    std::cout << possible_forces.size() << std::endl;

}