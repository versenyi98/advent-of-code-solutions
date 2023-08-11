#include "octopus_grid.hpp"

#include <algorithm>
#include <numeric>

OctopusGrid OctopusGrid::parse(std::vector<std::string> &lines) {
    std::vector<std::vector<std::shared_ptr<Octopus>>> grid;

    std::vector<std::pair<int, int>> neighbour_positions = {
        {-1, -1}, {-1, 0}, {-1, +1}, {0, -1}};

    for (int row{}; row < 10; row++) {
        grid.push_back(std::vector<std::shared_ptr<Octopus>>());
        auto &octopus_row = grid.back();

        for (int col{}; col < 10; col++) {
            int energy_level = lines[row][col] - '0';
            std::shared_ptr<Octopus> octopus_ptr = std::make_shared<Octopus>(energy_level);

            for (auto [d_row, d_col] : neighbour_positions) {
                int n_row = d_row + row;
                int n_col = d_col + col;

                if (n_row >= 0 && n_row < 10 && n_col >= 0 && n_col < 10) {
                    octopus_ptr->add_neighbour(grid[n_row][n_col]);
                    grid[n_row][n_col]->add_neighbour(octopus_ptr);
                }
            }

            octopus_row.push_back(octopus_ptr);
        }
    }

    return OctopusGrid(std::move(grid));
}

int OctopusGrid::get_number_of_flashes_after_100_turns() {
    return m_number_of_flashes_after_100_rounds;
}

int OctopusGrid::get_turns_after_octopuses_synced() {
    return m_turns_passed;
}

OctopusGrid::OctopusGrid(const std::vector<std::vector<std::shared_ptr<Octopus>>> &&grid) : m_grid(grid), m_number_of_flashes_after_100_rounds(0), m_turns_passed(0) {
}

void OctopusGrid::simulate_until_sync() {
    while (m_turns_passed < 100 || !are_octopuses_synced()) {
        simulate_turn();

        m_turns_passed++;

        if (m_turns_passed == 100) {
            m_number_of_flashes_after_100_rounds = std::accumulate(begin(m_grid), end(m_grid), 0, [](int curr1, const auto &row) {
                return curr1 + std::accumulate(begin(row), end(row), 0, [](int curr2, const auto &ptr) {
                           return curr2 + ptr->get_flash_count();
                       });
            });
        }
    }
}

void OctopusGrid::simulate_turn() {
    for (auto &octopus_row : m_grid) {
        for (auto &octopus : octopus_row) {
            octopus->start_turn();
        }
    }

    for (auto &octopus_row : m_grid) {
        for (auto &octopus : octopus_row) {
            octopus->increase_energy_level();
        }
    }
}

bool OctopusGrid::are_octopuses_synced() const {
    return std::all_of(begin(m_grid), end(m_grid), [](const auto &row) {
        return std::all_of(begin(row), end(row), [](const auto &octopus) {
            return octopus->has_flashed_this_round();
        });
    });
}
