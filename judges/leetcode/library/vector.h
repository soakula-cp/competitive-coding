#pragma once

#ifndef __VECTOR_H__
#define __VECTOR_H__

#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>

// clang-format off
/**
 * FUNCTION DESCRIPTION
 *
 * @brief Reads a vector of elements from an input stream.
 *
 * This function reads a vector of elements of type T from the given input
 * stream. It expects the input to be in the format of a list enclosed in
 * square brackets, with elements separated by commas (e.g., "[1,2,3,4]").
 *
 * @param in The input stream to read from.
 * @param container The vector to store the read elements.
 */
template <typename T>
void ReadVector(std::istream& in, std::vector<T>& container) {
    container.clear();
    std::string line;
    std::getline(in, line);
    if (line.empty() || line == "[]") {
        return;
    }
    if (line.front() == '[' && line.back() == ']') {
        line = line.substr(1, line.size() - 2);
        std::stringstream ss(line);
        std::string       token;
        while (std::getline(ss, token, ',')) {
            std::stringstream token_ss(token);
            T                 value;
            token_ss >> value;
            container.emplace_back(value);
        }
    }
}

// clang-format off
/**
 * FUNCTION DESCRIPTION
 *
 * @brief Writes a vector of elements to an output stream.
 *
 * This function writes a vector of elements of type T to the given output
 * stream. It formats the output as a list enclosed in square brackets, with
 * elements separated by commas (e.g., "[1,2,3,4]").
 *
 * @param out The output stream to write to.
 * @param container The vector to write.
 */
template <typename T>
void WriteVector(std::ostream& out, const std::vector<T>& container) {
    std::stringstream ss;
    ss << "[";
    std::copy(container.begin(), container.end(),
              std::ostream_iterator<T>(ss, ","));
    std::string result = ss.str();
    if (!container.empty())
        result.pop_back();  // Remove trailing comma if not empty
    out << result << "]\n";
}

#endif  // __VECTOR_H__
