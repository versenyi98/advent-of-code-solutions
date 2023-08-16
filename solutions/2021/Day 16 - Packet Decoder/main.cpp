#include <iostream>
#include <numeric>
#include <string>

#include "packet.hpp"

int main() {
    std::string hex_line;
    std::cin >> hex_line;
    std::cout << hex_line << std::endl;

    std::string bin_line = std::accumulate(begin(hex_line), end(hex_line), std::string(""), [](std::string current, char ch) {
        return current + Packet::hex_char_to_bin(ch);
    });

    std::shared_ptr<Packet> packet = Packet::parse(bin_line);
    std::cout << packet->get_version_number_sum() << std::endl;
    std::cout << packet->get_result() << std::endl;
}
