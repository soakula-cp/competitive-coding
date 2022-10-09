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
 *        Filename: 69__sqrtx/solution.cpp
 *      Created on: 09 October 2022
 *   Last modified: 09 October 2022
 *          Author: soakula-cp
 *     Description: LEETCODE submission for 'Sqrt(x)' problem
 *     Is Premium?: No
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 09-10-2022                 soakula-cp       - Creation of file
 */
// clang-format on

namespace Solution_01 {
// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://leetcode.com/problems/sqrtx/submissions/817782501/
 *  - Status: Accepted.  /  test cases passed.
 *  - Runtime: 8 ms, faster than 32.2% of C++ online submissions
 *  - Memory usage: 6 MB, less than 24.9% of C++ online submissions
 * Algorithm metadata:
 *  - Time complexity: O(t*x*log(x)), where t is number of tests and x is input
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
    int mySqrt(int x) {
        long long int low = 0, high = x / 2 + 1;
        int           answer = 0;
        while (low <= high) {
            long long int mid = low + (high - low) / 2;
            if (mid * mid <= x) {
                answer = mid;
                low    = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return answer;
    }
};
}  // namespace Solution_01
