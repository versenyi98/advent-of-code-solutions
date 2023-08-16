#pragma once

#include <functional>
#include <memory>
#include <numeric>
#include <string>
#include <vector>

typedef unsigned long long int value_t;

value_t binary_string_to_decimal(const std::string &binary, int length);

value_t binary_string_to_decimal(const std::string &binary);

void trim(std::string &packet, int n);

class Packet {
public:
    static std::shared_ptr<Packet> parse(std::string packet);

    Packet(value_t size, value_t version) : m_size(size), m_version(version) {}

    virtual value_t get_result() = 0;

    value_t get_size() const {
        return m_size;
    }

    virtual value_t get_version_number_sum() const {
        return m_version;
    }

    static std::string hex_char_to_bin(char c);

protected:
    value_t m_size;
    value_t m_version;

private:
    static std::shared_ptr<Packet> parse_literal_packet(std::string packet, value_t header_size, value_t packet_version);
    static std::shared_ptr<Packet> parse_operator_packet(std::string packet, value_t header_size, value_t packet_version, int operator_type);
};

class LiteralPacket : public Packet {
public:
    LiteralPacket(value_t size, value_t version, value_t value) : Packet(size, version), m_value(value) {}

    virtual value_t get_result() {
        return m_value;
    }

protected:
    value_t m_value;
};

class OperatorPacket : public Packet {
public:
    OperatorPacket(value_t size, value_t version, const std::vector<std::shared_ptr<Packet>> &packets) : Packet(size, version), m_packets(packets) {}

    virtual value_t get_result() = 0;

    virtual value_t get_version_number_sum() const {
        return m_version + std::accumulate(begin(m_packets), end(m_packets), static_cast<value_t>(0), [](value_t current, const auto &packet) {
                   return current + packet->get_version_number_sum();
               });
    }

protected:
    std::vector<std::shared_ptr<Packet>> m_packets;
};

class SumOperatorPacket : public OperatorPacket {
public:
    using OperatorPacket::OperatorPacket;

    virtual value_t get_result() {
        return std::accumulate(begin(m_packets), end(m_packets), static_cast<value_t>(0), [](value_t current, const auto &packet) {
            return current + packet->get_result();
        });
    }
};

class ProductOperatorPacket : public OperatorPacket {
public:
    using OperatorPacket::OperatorPacket;

    virtual value_t get_result() {
        return std::accumulate(begin(m_packets), end(m_packets), static_cast<value_t>(1), [](value_t current, const auto &packet) {
            return current * packet->get_result();
        });
    }
};

class MinimumOperatorPacket : public OperatorPacket {
public:
    using OperatorPacket::OperatorPacket;

    virtual value_t get_result() {
        std::vector<value_t> values;
        std::transform(begin(m_packets), end(m_packets), std::back_inserter(values), [](const auto &packet) {
            return packet->get_result();
        });

        return *std::min_element(begin(values), end(values));
    }
};

class MaximumOperatorPacket : public OperatorPacket {
public:
    using OperatorPacket::OperatorPacket;

    virtual value_t get_result() {
        std::vector<value_t> values;
        std::transform(begin(m_packets), end(m_packets), std::back_inserter(values), [](const auto &packet) {
            return packet->get_result();
        });

        return *std::max_element(begin(values), end(values));
    }
};

class GreaterThanOperatorPacket : public OperatorPacket {
public:
    using OperatorPacket::OperatorPacket;

    virtual value_t get_result() {
        return m_packets[0]->get_result() > m_packets[1]->get_result();
    }
};

class LessThanOperatorPacket : public OperatorPacket {
public:
    using OperatorPacket::OperatorPacket;

    virtual value_t get_result() {
        return m_packets[0]->get_result() < m_packets[1]->get_result();
    }
};

class EqualToThanOperatorPacket : public OperatorPacket {
public:
    using OperatorPacket::OperatorPacket;

    virtual value_t get_result() {
        return m_packets[0]->get_result() == m_packets[1]->get_result();
    }
};