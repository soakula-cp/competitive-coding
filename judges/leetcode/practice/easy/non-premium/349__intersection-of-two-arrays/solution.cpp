// clang-format off
/**
 * COPYRIGHT NOTICE
 *
 * Copyright (c) 2022. Jayaprakash Akula <akulajayaprakash@gmail.com>
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
 *        Filename: 349__intersection-of-two-arrays/solution.cpp
 *      Created on: 09 October 2022
 *   Last modified: 09 October 2022
 *          Author: jayaprakash-a
 *     Description: LEETCODE submission for 'Intersection of Two Arrays' problem
 *     Is Premium?: No
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 09-10-2022                jayaprakash-a      - Creation of file
 */
// clang-format on

#include <unordered_set>
#include <vector>

using std::unordered_set;
using std::vector;

namespace Solution_01 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link:
 *  - Status: Accepted. 55 / 55 test cases passed.
 *  - Runtime: 7 ms, faster than % of C++ online submissions
 *  - Memory usage: 10.5 MB, less than % of C++ online submissions
 * Algorithm metadata:
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
     * Time complexity:
     * Space complexity:
     * Additional notes
     *  -
     */
    // clang-format on
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> numSet(nums1.begin(), nums1.end());
        vector<int>        res;
        for (auto num : nums2)
            if (numSet.find(num) != numSet.end()) {
                res.push_back(num);
                numSet.erase(num);
            }
        return res;
    }
};
}  // namespace Solution_01
