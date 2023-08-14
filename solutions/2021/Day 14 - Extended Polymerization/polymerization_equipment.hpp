#pragma once

#include <map>
#include <string>
#include <vector>

class PolymerizationEquipment {
public:
    static PolymerizationEquipment parse(const std::vector<std::string> lines);

    unsigned long long int get_frequency_diff_after_rounds(int rounds) const;

private:
    void perform_insertion(auto &pairs_occuring) const;

    PolymerizationEquipment(const auto &pairs_occuring, const auto &insertion_rules);

    std::map<std::pair<char, char>, char> m_insertion_rules;
    std::map<std::pair<char, char>, unsigned long long int> m_pairs_occuring;
};