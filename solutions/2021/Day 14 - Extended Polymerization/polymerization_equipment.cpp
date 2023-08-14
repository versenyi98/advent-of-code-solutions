#include "polymerization_equipment.hpp"

#include <algorithm>
#include <iostream>
#include <numeric>

PolymerizationEquipment PolymerizationEquipment::parse(const std::vector<std::string> lines) {
    std::map<std::pair<char, char>, unsigned long long int> pairs_occuring;

    pairs_occuring[{'#', lines[0][0]}]++;
    pairs_occuring[{lines[0].back(), '#'}]++;

    for (int i{}; i < lines[0].length() - 1; i++) {
        pairs_occuring[{lines[0][i], lines[0][i + 1]}]++;
    }

    std::map<std::pair<char, char>, char> insertion_rules;
    std::for_each(begin(lines) + 2, end(lines), [&insertion_rules](const std::string &line) {
        insertion_rules[{line[0], line[1]}] = line.back();
    });

    return PolymerizationEquipment(pairs_occuring, insertion_rules);
}

PolymerizationEquipment::PolymerizationEquipment(const auto &pairs_occuring, const auto &insertion_rules) : m_pairs_occuring(pairs_occuring), m_insertion_rules(insertion_rules) {
}

unsigned long long int PolymerizationEquipment::get_frequency_diff_after_rounds(int rounds) const {
    auto pairs_occuring_copy = m_pairs_occuring;

    for (int i{}; i < rounds; i++) {
        perform_insertion(pairs_occuring_copy);
    }

    std::map<char, unsigned long long int> counter;
    for (auto [pairing, occurance] : pairs_occuring_copy) {
        if (occurance) {
            counter[pairing.first] += occurance;
            counter[pairing.second] += occurance;
        }
    }

    auto value_is_less = [](const auto &a, const auto &b) {
        return a.second < b.second;
    };

    counter.erase(counter.find('#'));
    auto minimum = std::min_element(begin(counter), end(counter), value_is_less);
    auto maximum = std::max_element(begin(counter), end(counter), value_is_less);

    return (maximum->second - minimum->second) / 2;
}

void PolymerizationEquipment::perform_insertion(auto &pairs_occuring) const {
    std::map<std::pair<char, char>, unsigned long long int> new_pairs_occuring;

    for (auto [key, count] : pairs_occuring) {
        auto it = m_insertion_rules.find(key);

        if (it != m_insertion_rules.end()) {
            new_pairs_occuring[{key.first, it->second}] += count;
            new_pairs_occuring[{it->second, key.second}] += count;
        } else {
            new_pairs_occuring[key] += count;
        }
    }

    pairs_occuring = new_pairs_occuring;
}