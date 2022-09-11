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
 *        Filename: 1991__find-the-middle-index-in-array/solution.cpp
 *      Created on: 11 September 2022
 *   Last modified: 11 September 2022
 *          Author: soakula-cp
 *     Description: LEETCODE submission for 'Find the Middle Index in Array' problem
 *     Is Premium?: No
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 11-09-2022                 soakula-cp        - Creation of file
 */
// clang-format on

#include <vector>

using std::vector;

namespace Solution_01 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796885427/
 *  - Status: Accepted. 294 / 205 test cases passed.
 *  - Runtime: 17 ms, faster than 5.85% of C++ online submissions
 *  - Memory usage: 12.3 MB, less than 94.31% of C++ online submissions
 * Algorithm metatdata:
 *  - Time complexity: O(t*n), where t is number of tests and n is size of nums
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
     * Time complexity: O(n+n) ~ O(n), where n is size of nums
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    int findMiddleIndex(vector<int>& nums) {
        int sz       = static_cast<int>(nums.size());
        int left_sum = 0, right_sum = accumulate(begin(nums), end(nums), 0);
        for (int idx = 0; idx < sz; ++idx) {
            right_sum -= nums[idx];
            if (left_sum == right_sum) {
                return idx;
            }
            left_sum += nums[idx];
        }
        return -1;
    }
};
}  // namespace Solution_01
