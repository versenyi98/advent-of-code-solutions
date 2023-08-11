#pragma once

#include <memory>
#include <vector>

class Octopus {
public:
    explicit Octopus(int energy_level);

    void add_neighbour(const std::shared_ptr<Octopus> &octopus);
    void start_turn();
    void increase_energy_level();

    int get_flash_count() const;
    int get_energy_level() const;
    bool has_flashed_this_round() const;

private:
    void flash();

    std::vector<std::shared_ptr<Octopus>> m_neighbours;
    int m_energy_level;
    bool m_has_flashed_this_round;
    int m_flash_count;
};