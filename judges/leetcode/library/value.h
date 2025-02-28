#pragma once

#ifndef __VALUE_H__
#define __VALUE_H__

#include <iostream>
#include <sstream>
#include <string>
#include <type_traits>

// clang-format off
/**
 * FUNCTION DESCRIPTION
 *
 * @brief Reads a single value of type T from an input stream.
 *
 * This function reads a single value of type T from the given input
 * stream. It supports integral types, floating-point types, and strings.
 *
 * @tparam T The type of the value to read.
 * @param in The input stream to read from.
 * @param value The variable to store the read value.
 */
// clang-format on
template <typename T, typename = std::enable_if<std::is_integral_v<T> ||
                                                std::is_floating_point_v<T> ||
                                                std::is_same_v<std::string, T>>>
void ReadValue(std::istream& in, T& value) {
    std::string line;
    if (std::getline(in, line)) {
        std::stringstream ss(line);
        ss >> value;
    }
}

// clang-format off
/**
 * FUNCTION DESCRIPTION
 *
 * @brief Writes a single value of type T to an output stream.
 *
 * @tparam T The type of the value to write.
 * @param out The output stream to write to.
 * @param value The value to write.
 */
// clang-format on
template <typename T, typename = std::enable_if<std::is_integral_v<T> ||
                                                std::is_floating_point_v<T> ||
                                                std::is_same_v<std::string, T>>>
void WriteValue(std::ostream& out, T& value) {
    out << value;
}

#endif  // __VALUE_H__
