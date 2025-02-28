#pragma once

#ifndef __UTILS_H__
#define __UTILS_H__

#include <chrono>

namespace Utils {
// clang-format off
/**
 * FUNCTION DESCRIPTION
 *
 * @brief Measures the execution time of a given function.
 *
 * This function takes a callable object (function, lambda, etc.) as input,
 * executes it, and measures the time taken for its execution.
 *
 * @tparam Func The type of the callable object.
 * @param func The callable object to be executed.
 * @return int64_t The execution time of the function in microseconds.
 */
// clang-format on
template <typename Func>
int64_t MeasureExecutionTime(Func func) {
    auto start = std::chrono::high_resolution_clock::now();
    func();  // Execute the function
    auto end = std::chrono::high_resolution_clock::now();
    return std::chrono::duration_cast<std::chrono::microseconds>(end - start)
        .count();
}

// clang-format off
/**
 * FUNCTION DESCRIPTION
 *
 * @brief Counts the number of digits in an integer.
 *
 * @param number The integer to count digits from.
 * @return int The number of digits in the integer.
 */
// clang-format on
int CountDigits(int number) {
    if (number == 0) return 1;
    int count = 0;
    number    = std::abs(number);
    while (number != 0) {
        number /= 10;
        ++count;
    }
    return count;
}
}  // namespace Utils

#endif  // __UTILS_H__
