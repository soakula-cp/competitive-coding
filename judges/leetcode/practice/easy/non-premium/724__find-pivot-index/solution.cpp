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
 *        Filename: 724__find-pivot-index/solution.cpp
 *      Created on: 10 September 2022
 *   Last modified: 10 September 2022
 *          Author: soakula-cp
 *     Description: LEETCODE submission for 'Find Pivot Index' problem
 *     Is Premium?: No
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 10-09-2022               soakula-cp      - Creation of file
 */
// clang-format on

#include <algorithm>
#include <numeric>
#include <vector>

using std::accumulate;
using std::copy;
using std::partial_sum;
using std::vector;

namespace Solution_01 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796343225/
 *  - Status: Accepted. 745 / 745 test cases passed.
 *  - Runtime: 896 ms, faster than 5% of C++ online submissions
 *  - Memory usage: 31.2 MB, less than 52.07% of C++ online submissions
 * Algorithm metatdata:
 *  - Time complexity: O(t*n^2), where t is number of tests and n is size of nums
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
     * Time complexity: O(n*(n+n)) ~ O(n^2), where n is size of nums
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    int pivotIndex(vector<int>& nums) {
        int sz = static_cast<int>(nums.size());
        for (int idx = 0; idx < sz; ++idx) {
            int left_sum  = accumulate(begin(nums), begin(nums) + idx, 0);
            int right_sum = accumulate(begin(nums) + idx + 1, end(nums), 0);
            if (left_sum == right_sum) {
                return idx;
            }
        }
        return -1;
    }
};
}  // namespace Solution_01

namespace Solution_02 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796323944/
 *  - Status: Accepted. 745 / 745 test cases passed.
 *  - Runtime: 62 ms, faster than 12.4% of C++ online submissions
 *  - Memory usage: 32.2 MB, less than 11.28% of C++ online submissions
 * Algorithm metatdata:
 *  - Time complexity: O(t*n), where t is number of tests and n is size of nums
 *  - Space complexity: O(n), where n is size of nums
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
     * Time complexity: O(n+n+n+n+n) ~ O(n), where n is size of nums
     * Space complexity: O(n+n) ~ O(n) where n is size of nums
     * Additional notes
     *  -
     */
    // clang-format on
    int pivotIndex(vector<int>& nums) {
        int         sz = static_cast<int>(nums.size());
        vector<int> left_sum(sz + 2, 0), right_sum(sz + 2, 0);
        copy(begin(nums), end(nums), begin(left_sum) + 1);
        copy(begin(nums), end(nums), begin(right_sum) + 1);
        partial_sum(begin(left_sum), end(left_sum), begin(left_sum));
        partial_sum(rbegin(right_sum), rend(right_sum), rbegin(right_sum));
        for (int idx = 1; idx <= sz; ++idx) {
            if (left_sum[idx - 1] == right_sum[idx + 1]) {
                return idx - 1;
            }
        }
        return -1;
    }
};
}  // namespace Solution_02

namespace Solution_03 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796332258/
 *  - Status: Accepted. 745 / 745 test cases passed.
 *  - Runtime: 29 ms, faster than 81.63% of C++ online submissions
 *  - Memory usage: 31.7 MB, less than 15.62% of C++ online submissions
 * Algorithm metatdata:
 *  - Time complexity: O(t*n), where t is number of tests and n is size of nums
 *  - Space complexity: O(n), where n is size of nums
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
     * Time complexity: O(n+n+n) ~ O(n), where n is size of nums
     * Space complexity: O(n) ~ O(n) where n is size of nums
     * Additional notes
     *  -
     */
    // clang-format on
    int pivotIndex(vector<int>& nums) {
        int         sz = static_cast<int>(nums.size());
        vector<int> right_sum(nums);
        partial_sum(rbegin(right_sum), rend(right_sum), rbegin(right_sum));
        int left_sum = 0, r_sum = 0;
        for (int idx = 0; idx < sz; ++idx) {
            r_sum = idx == sz - 1 ? 0 : right_sum[idx + 1];
            if (left_sum == r_sum) {
                return idx;
            }
            left_sum += nums[idx];
        }
        return -1;
    }
};
}  // namespace Solution_03

namespace Solution_04 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/submissions/detail/796339569/
 *  - Status: Accepted. 745 / 745 test cases passed.
 *  - Runtime: 59 ms, faster than 14.97% of C++ online submissions
 *  - Memory usage: 31 MB, less than 98.99% of C++ online submissions
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
    int pivotIndex(vector<int>& nums) {
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
}  // namespace Solution_04
