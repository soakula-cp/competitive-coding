// clang-format off
/**
 * COPYRIGHT NOTICE
 *
 * Copyright (c) 2024. Sona Praneeth Akula <sonapraneeth.akula@gmail.com>
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
 *   Last modified: 15 October 2024
 *          Author: sonapraneeth-a
 *     Description: LEETCODE submission for 'Two Sum' problem
 *     Is Premium?: No
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 08-10-2022               sonapraneeth-a        - Creation of file
 * 15-02-2024                 soakula-cp          - Added solutions 2,3,4
 */
// clang-format on

#include <algorithm>
#include <unordered_map>
#include <utility>
#include <vector>

using std::pair;
using std::sort;
using std::unordered_map;
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
        int nums_sz = static_cast<int>(nums.size());
        // 0. Base case
        if (nums_sz < 2) {
            return {};
        }
        // 1. For all pairs of numbers, find that pair which sums to `target`
        for (int nums_i = 0; nums_i < nums_sz; ++nums_i) {
            for (int nums_j = nums_i + 1; nums_j < nums_sz; ++nums_j) {
                if (nums[nums_i] + nums[nums_j] == target) {
                    return {nums_i, nums_j};
                }
            }
        }
        return {};
    }
};
}  // namespace Solution_01

namespace Solution_02 {
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
        int nums_sz = static_cast<int>(nums.size());
        // 0. Base case
        if (nums_sz < 2) {
            return {};
        }
        // 1. Create a map of number and its corresponding index in `nums`
        vector<pair<int, int>> numbers(nums_sz, {-1, -1});
        for (int nums_i = 0; nums_i < nums_sz; ++nums_i) {
            numbers[nums_i] = {nums[nums_i], nums_i};
        }
        // 2. Sort the numbers in ascending order first based on value and then
        //    based on index
        sort(begin(numbers), end(numbers),
             [](const pair<int, int>& lhs, const pair<int, int>& rhs) {
                 if (lhs.first == rhs.first) {
                     return lhs.second < rhs.second;
                 }
                 return lhs.first < rhs.first;
             });
        // 3. Use two pointers, `left_nums_i` (pointing towards the left end of
        //    sorted array) and `right_nums_i` (pointing towards the right end
        //    of sorted array)
        int left_nums_i  = 0;
        int right_nums_i = nums_sz - 1;
        // 4. Calculate the sum of `nums[left_nums_i]` and `nums[right_nums_i]`
        //    Let it be `sum`. Check if the `sum` equals `target`
        //    If yes, we've got the required indices
        //    If no,
        //      (1) If the `sum` > `target`, in order to reached the target
        //          we need to reduce `right_nums_i`, so that the new `sum` can
        //          be reduced
        //      (2) If the `sum` < `target`, in order to reached the target
        //          we need to increase `left_nums_i`, so that the new `sum` can
        //          be increased
        //    Continue this until `left_nums_i` < `right_nums_i`
        while (left_nums_i < right_nums_i) {
            if (numbers[left_nums_i].first + numbers[right_nums_i].first ==
                target) {
                return {numbers[left_nums_i].second,
                        numbers[right_nums_i].second};
            }
            if (numbers[left_nums_i].first + numbers[right_nums_i].first >
                target) {
                --right_nums_i;
            } else {
                ++left_nums_i;
            }
        }
        return {};
    }
};
}  // namespace Solution_02

namespace Solution_03 {
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
        int nums_sz = static_cast<int>(nums.size());
        // 0. Base case
        if (nums_sz < 2) {
            return {};
        }
        // 1. Create a mapping from number to its occurrence in `nums`. Store it
        //    in `vector` as a single number could occur multiple times in
        //    `nums`
        unordered_map<int, vector<int>> num_to_nums_i_map {};
        for (int nums_i = 0; nums_i < nums_sz; ++nums_i) {
            num_to_nums_i_map[nums[nums_i]].emplace_back(nums_i + 1);
        }
        // 2. Loop through map
        //  (1) If `target` == (2 * `key`) and we have atleast two instances of
        //     `key` occurring in `nums`, we've got the required indices
        //  (2) Check if `key` and `target - key` are present in `nums`. If yes,
        //      we've got the required indices
        for (const auto& [key, val] : num_to_nums_i_map) {
            if (target == (key * 2)) {
                if (val.size() >= 2) {
                    return {val[0] - 1, val[1] - 1};
                }
            } else {
                auto itr = num_to_nums_i_map.find(target - key);
                if (itr != num_to_nums_i_map.end()) {
                    return {val[0] - 1, itr->second[0] - 1};
                }
            }
        }
        return {};
    }
};
}  // namespace Solution_03

namespace Solution_04 {
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
        int nums_sz = static_cast<int>(nums.size());
        // 0. Base case
        if (nums_sz < 2) {
            return {};
        }
        // 1. Create a mapping from number to its occurrence in `nums`.
        // 2. For each `value` in `nums`
        //    (1) Check if `target - value` exists in map. If yes, we've got
        //        required indices
        //    (2) Else, add `value` and its corresponding index to map
        unordered_map<int, int> num_to_nums_i_map;
        for (int nums_i = 0; nums_i < nums_sz; ++nums_i) {
            auto itr = num_to_nums_i_map.find(target - nums[nums_i]);
            if (itr == num_to_nums_i_map.end()) {
                num_to_nums_i_map.insert({nums[nums_i], nums_i});
            } else {
                return {itr->second, nums_i};
            }
        }
        return {};
    }
};
}  // namespace Solution_04
