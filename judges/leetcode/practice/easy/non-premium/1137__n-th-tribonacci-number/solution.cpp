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
 *        Filename: 1137__n-th-tribonacci-number/solution.cpp
 *      Created on: 11 September 2022
 *   Last modified: 11 September 2022
 *          Author: soakula-cp
 *     Description: LEETCODE submission for 'N-th Tribonacci Number' problem
 *     Is Premium?: No
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 11-09-2022               soakula-cp      - Creation of file
 */
// clang-format on

namespace Solution_01 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796835392/
 *  - Status: Accepted. 39 / 39 test cases passed.
 *  - Runtime: 4 ms, faster than 22.22% of C++ online submissions
 *  - Memory usage: 6 MB, less than 53.38% of C++ online submissions
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
    int tribonacci(int n) {
        if (n <= 1) {
            return n;
        }
        if (n == 2) {
            return 1;
        }
        int answer, prev = 1, prev_prev = 1, prev_prev_prev = 0;
        for (int idx = 3; idx <= n; ++idx) {
            answer         = prev + prev_prev + prev_prev_prev;
            prev_prev_prev = prev_prev;
            prev_prev      = prev;
            prev           = answer;
        }
        return answer;
    }
};
}  // namespace Solution_01
