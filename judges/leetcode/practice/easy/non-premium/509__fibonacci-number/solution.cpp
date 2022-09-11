// clang-format off
/**
 * COPYRIGHT NOTICE
 *
 * Copyright (c) 2022. Sona Praneeth Akula <soakula.cp@gmail.com>
 *
 * This file is created for LEETCODE Practice in competitive programming.
 *
 * This file cannot be copied and/or distributed without the express
 * permission of the copyright owner.
 *
 */

/**
 * FILE DESCRIPTION
 *
 *        Filename: 509__fibonacci-number/solution.cpp
 *      Created on: 10 September 2022
 *   Last modified: 10 September 2022
 *          Author: soakula-cp
 *     Description: LEETCODE submission for 'Fibonacci Number' problem
 *     Is Premium?: No
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 10-09-2022               soakula-cp      - Creation of file
 */
// clang-format on

#include <functional>
#include <vector>

using std::function;
using std::vector;

namespace Solution_01 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796394609/
 *  - Status: Accepted. 31 / 31 test cases passed.
 *  - Runtime: 35 ms, faster than 5.77% of C++ online submissions
 *  - Memory usage: 5.8 MB, less than 78.78% of C++ online submissions
 * Algorithm metatdata:
 *  - Time complexity: O(t*2^n), where t is number of tests and n is input
 *  - Space complexity: O(t*2^n), where t is number of tests and n is input
 *  - Tags:
 *  - Categories:
 * Additional notes:
 *  -
 */
// clang-format on
class Solution {
 public:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Time complexity: O(2^n), where n is input
     * Space complexity: O(2^n), where n is input (stack space)
     * Additional notes
     *  -
     */
    // clang-format on
    int fib(int n) { return n <= 1 ? n : fib(n - 1) + fib(n - 2); }
};
}  // namespace Solution_01

namespace Solution_02 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796826967/
 *  - Status: Accepted. 31 / 31 test cases passed.
 *  - Runtime: 0 ms, faster than 100% of C++ online submissions
 *  - Memory usage: 6.2 MB, less than 9.22% of C++ online submissions
 * Algorithm metatdata:
 *  - Time complexity: O(t*n), where t is number of tests and n is input
 *  - Space complexity: O(t*n), where t is number of tests and n is input
 *  - Tags:
 *  - Categories:
 * Additional notes:
 *  -
 */
// clang-format on
class Solution {
 public:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Time complexity: O(n), where n is input
     * Space complexity: O(n), where n is input (cache space)
     * Additional notes
     *  -
     */
    // clang-format on
    int fib(int n) {
        vector<int>        cache(n + 1, -1);
        function<int(int)> fibHelper = [&](int x) {
            if (cache[x] != -1) {
                return cache[x];
            }
            return cache[x] = x <= 1 ? x : fibHelper(x - 1) + fibHelper(x - 2);
        };
        return fibHelper(n);
    }
};
}  // namespace Solution_02

namespace Solution_03 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796456820/
 *  - Status: Accepted. 31 / 31 test cases passed.
 *  - Runtime: 4 ms, faster than 55.18% of C++ online submissions
 *  - Memory usage: 6.1 MB, less than 9.20% of C++ online submissions
 * Algorithm metatdata:
 *  - Time complexity: O(t*n), where t is number of tests and n is input
 *  - Space complexity: O(t*n), where t is number of tests and n is input
 *  - Tags:
 *  - Categories:
 * Additional notes:
 *  -
 */
// clang-format on
class Solution {
 public:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Time complexity: O(n), where n is input
     * Space complexity: O(n), where n is input (cache space)
     * Additional notes
     *  -
     */
    // clang-format on
    int fib(int n) {
        if (n <= 1) {
            return n;
        }
        vector<int> cache(n + 1, -1);
        cache[0] = 0, cache[1] = 1;
        for (int idx = 2; idx <= n; ++idx) {
            cache[idx] = cache[idx - 1] + cache[idx - 2];
        }
        return cache[n];
    }
};
}  // namespace Solution_03

namespace Solution_04 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796821197/
 *  - Status: Accepted. 31 / 31 test cases passed.
 *  - Runtime: 0 ms, faster than 100% of C++ online submissions
 *  - Memory usage: 5.9 MB, less than 40.12% of C++ online submissions
 * Algorithm metatdata:
 *  - Time complexity: O(t*n), where t is number of tests and n is input
 *  - Space complexity: O(1)
 *  - Tags:
 *  - Categories:
 * Additional notes:
 *  -
 */
// clang-format on
class Solution {
 public:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Time complexity: O(n), where n is input
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    int fib(int n) {
        if (n <= 1) {
            return n;
        }
        int answer, prev = 1, prev_prev = 0;
        for (int idx = 2; idx <= n; ++idx) {
            answer    = prev + prev_prev;
            prev_prev = prev;
            prev      = answer;
        }
        return answer;
    }
};
}  // namespace Solution_04
