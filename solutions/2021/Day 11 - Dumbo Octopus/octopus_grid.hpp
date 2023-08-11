#pragma once

#include <memory>
#include <string>
#include <vector>

#include "octopus.hpp"

class OctopusGrid {
public:
    static OctopusGrid parse(std::vector<std::string> &lines);

    int get_number_of_flashes_after_100_turns();
    int get_turns_after_octopuses_synced();
    void simulate_until_sync();

private:
    explicit OctopusGrid(const std::vector<std::vector<std::shared_ptr<Octopus>>> &&grid);

    void simulate_turn();

    bool are_octopuses_synced() const;

    std::vector<std::vector<std::shared_ptr<Octopus>>> m_grid;

    int m_number_of_flashes_after_100_rounds;
    int m_turns_passed;
};