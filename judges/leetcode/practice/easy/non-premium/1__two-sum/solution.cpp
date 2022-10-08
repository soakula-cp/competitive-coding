// clang-format off
/**
 * COPYRIGHT NOTICE
 *
 * Copyright (c) 2022. Sona Praneeth Akula <sonapraneeth.akula@gmail.com>
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
 *        Filename: 1__two-sum/solution.cpp
 *      Created on: 08 October 2022
 *   Last modified: 08 October 2022
 *          Author: sonapraneeth-a
 *     Description: LEETCODE submission for 'Two Sum' problem
 *     Is Premium?: No
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 08-10-2022               sonapraneeth-a        - Creation of file
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
 *  - Submission link: https://leetcode.com/problems/two-sum/submissions/817873491/
 *  - Status: Accepted.  /  test cases passed.
 *  - Runtime: 759 ms, faster than 21.24% of C++ online submissions
 *  - Memory usage: 10.2 MB, less than 88.96% of C++ online submissions
 * Algorithm metadata:
 *  - Time complexity: O(t*n^2), where t is number of tests and n is size of nums
 *  - Space complexity: O(1)
 *  - Tags:
 *  - Categories: Implementation
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
     * Time complexity: O(n^2), where n is size of nums
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    vector<int> twoSum(vector<int>& nums, int target) {
        int sz = static_cast<int>(nums.size());
        for (int idx1 = 0; idx1 < sz; ++idx1) {
            for (int idx2 = idx1 + 1; idx2 < sz; ++idx2) {
                if (nums[idx1] + nums[idx2] == target) {
                    return {idx1, idx2};
                }
            }
        }
        return {-1, -1};
    }
};
}  // namespace Solution_01
