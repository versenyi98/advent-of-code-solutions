#include "octopus.hpp"

Octopus::Octopus(int energy_level) : m_energy_level(energy_level), m_has_flashed_this_round(false), m_flash_count(0) {
}

void Octopus::add_neighbour(const std::shared_ptr<Octopus> &octopus) {
    m_neighbours.push_back(octopus);
}

void Octopus::start_turn() {
    if (m_has_flashed_this_round) {
        m_has_flashed_this_round = false;
        m_energy_level = 0;
    }
}

void Octopus::increase_energy_level() {
    m_energy_level++;

    if (m_energy_level > 9 && !m_has_flashed_this_round) {
        flash();
    }
}

int Octopus::get_flash_count() const {
    return m_flash_count;
}

int Octopus::get_energy_level() const {
    return m_energy_level;
}

bool Octopus::has_flashed_this_round() const {
    return m_has_flashed_this_round;
}

void Octopus::flash() {
    m_has_flashed_this_round = true;
    m_flash_count++;

    for (auto &neigbour : m_neighbours) {
        neigbour->increase_energy_level();
    }
}
