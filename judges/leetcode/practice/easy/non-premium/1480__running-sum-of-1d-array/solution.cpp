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
 *        Filename: 1480__running-sum-of-1d-array/solution.cpp
 *      Created on: 10 September 2022
 *   Last modified: 10 September 2022
 *          Author: soakula-cp
 *     Description: LEETCODE submission for 'Running Sum of 1d Array' problem
 *     Is Premium?: No
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 10-09-2022                 soakula-cp         - Creation of file
 */
// clang-format on

#include <numeric>
#include <vector>

using std::partial_sum;
using std::vector;

namespace Solution_01 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796293832/
 *  - Status: Accepted. 53 / 53 test cases passed.
 *  - Runtime: 11 ms, faster than 10.48% of C++ online submissions
 *  - Memory usage: 8.6 MB, less than 37.34% of C++ online submissions
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
     * Time complexity: O(n), where n is size of nums
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    vector<int> runningSum(vector<int>& nums) {
        vector<int> answer(nums);
        for (int idx = 1; idx < static_cast<int>(nums.size()); ++idx) {
            answer[idx] += answer[idx - 1];
        }
        return answer;
    }
};
}  // namespace Solution_01

namespace Solution_02 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796305198/
 *  - Status: Accepted. 53 / 53 test cases passed.
 *  - Runtime: 9 ms, faster than 19.04% of C++ online submissions
 *  - Memory usage: 8.3 MB, less than 93.87% of C++ online submissions
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
     * Time complexity: O(n), where n is size of nums
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    vector<int> runningSum(vector<int>& nums) {
        // In-place prefix sum
        vector<int> answer(nums);
        partial_sum(begin(answer), end(answer), begin(answer));
        /*
        // New array prefix-sum
        vector<int> answer(nums.size(), 0);
        partial_sum(begin(nums), end(nums), begin(answer));
        */
        return answer;
    }
};
}  // namespace Solution_02
