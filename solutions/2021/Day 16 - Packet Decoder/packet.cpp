#include "packet.hpp"

value_t binary_string_to_decimal(const std::string &binary, int length) {
    return std::stoll(binary.substr(0, length), nullptr, 2);
}

value_t binary_string_to_decimal(const std::string &binary) {
    return std::stoll(binary, nullptr, 2);
}

void trim(std::string &packet, int n) {
    packet = packet.substr(n);
}

std::shared_ptr<Packet> Packet::parse(std::string packet) {
    value_t packet_size = 0;

    int packet_version = binary_string_to_decimal(packet, 3);
    trim(packet, 3);
    packet_size += 3;

    int packet_typeid = binary_string_to_decimal(packet, 3);
    trim(packet, 3);
    packet_size += 3;

    if (packet_typeid == 4) {
        return Packet::parse_literal_packet(packet, packet_size, packet_version);
    }

    return Packet::parse_operator_packet(packet, packet_size, packet_version, packet_typeid);
}

std::shared_ptr<Packet> Packet::parse_literal_packet(std::string packet, value_t header_size, value_t packet_version) {
    value_t size = header_size;
    std::string literal_value_bin = "";

    while (true) {
        std::string five_bits = packet.substr(0, 5);
        trim(packet, 5);
        size += 5;

        literal_value_bin += five_bits.substr(1);

        if (five_bits[0] == '0') {
            break;
        }
    }

    return std::make_shared<LiteralPacket>(size, packet_version, binary_string_to_decimal(literal_value_bin));
}

std::shared_ptr<Packet> Packet::parse_operator_packet(std::string packet, value_t header_size, value_t packet_version, int operator_type) {
    value_t size = header_size;

    int length_type_id = binary_string_to_decimal(packet, 1);
    trim(packet, 1);
    size += 1;

    std::vector<std::shared_ptr<Packet>> packets;

    if (length_type_id == 0) {
        int total_length_in_bits = binary_string_to_decimal(packet, 15);
        trim(packet, 15);
        size += 15;

        int sub_packet_size = 0;
        while (sub_packet_size != total_length_in_bits) {
            packets.push_back(Packet::parse(packet));
            sub_packet_size += packets.back()->get_size();

            trim(packet, packets.back()->get_size());
        }
        size += sub_packet_size;
    } else {
        int total_numbers_of_subpackets = binary_string_to_decimal(packet, 11);
        trim(packet, 11);
        size += 11;

        for (int i = 0; i < total_numbers_of_subpackets; i++) {
            packets.push_back(Packet::parse(packet));
            trim(packet, packets.back()->get_size());

            size += packets.back()->get_size();
        }
    }

    switch (operator_type) {
    case 0:
        return std::make_shared<SumOperatorPacket>(size, packet_version, packets);
    case 1:
        return std::make_shared<ProductOperatorPacket>(size, packet_version, packets);
    case 2:
        return std::make_shared<MinimumOperatorPacket>(size, packet_version, packets);
    case 3:
        return std::make_shared<MaximumOperatorPacket>(size, packet_version, packets);
    case 5:
        return std::make_shared<GreaterThanOperatorPacket>(size, packet_version, packets);
    case 6:
        return std::make_shared<LessThanOperatorPacket>(size, packet_version, packets);
    default:
        return std::make_shared<EqualToThanOperatorPacket>(size, packet_version, packets);
    }
}

std::string Packet::hex_char_to_bin(char c) {
    switch (toupper(c)) {
    case '0':
        return "0000";
    case '1':
        return "0001";
    case '2':
        return "0010";
    case '3':
        return "0011";
    case '4':
        return "0100";
    case '5':
        return "0101";
    case '6':
        return "0110";
    case '7':
        return "0111";
    case '8':
        return "1000";
    case '9':
        return "1001";
    case 'A':
        return "1010";
    case 'B':
        return "1011";
    case 'C':
        return "1100";
    case 'D':
        return "1101";
    case 'E':
        return "1110";
    case 'F':
        return "1111";
    }
    return "";
}