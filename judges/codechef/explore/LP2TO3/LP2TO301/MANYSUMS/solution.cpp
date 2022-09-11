// clang-format off
/**
 * COPYRIGHT NOTICE
 *
 * Copyright (c) 2022. Sona Praneeth Akula <soakula.cp@gmail.com>
 *
 * This file is created for CODECHEF Explore(LP2TO3/LP2TO301)
 * in competitive programming.
 *
 * This file cannot be copied and/or distributed without the express
 * permission of the copyright owner.
 *
 */

/**
 * FILE DESCRIPTION
 *
 *        Filename: MANYSUMS/solution.cpp
 *      Created on: 11 September 2022
 *   Last modified: 11 September 2022
 *          Author: soakula_cp
 *     Description: CODECHEF submission for 'Distinct Pair Sums' problem
 * Compile command: g++ solution.cpp -std=c++17 -lm -fomit-frame-pointer -pthread -O2 -o solution.exe
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 11-09-2022               soakula_cp      - Creation of file
 */
// clang-format on

#include <iostream>
#include <memory>
#include <string>
#include <unordered_set>

using std::cin;
using std::cout;
using std::ios_base;
using std::make_unique;
using std::stoi;
using std::unique_ptr;
using std::unordered_set;

// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Base solution class which needs to be implemented to obtain solution for the
 * question. Each inheritance of this class is unique in terms on approach,
 * time and space complexity.
 */
// clang-format on
class Solution {
 private:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Print solution in expected format
     *
     * Time complexity: O(1)
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    static void print_answer(int answer) { cout << answer << "\n"; }

 protected:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Function in which solution for the question is calculated
     *
     * Parameters:
     *  - L: int - Left end of range
     *  - R: int - Right end of range
     *
     * Returns:
     *  - int - Number of unique sums of any two integers within [L, R]
     */
    // clang-format on
    virtual int solve(int L, int R) = 0;

 public:
    virtual ~Solution() = default;

    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Actual run to read input tests, solve problem and print output
     *
     * Solution metadata:
     *  - Time complexity: O(T*O(solve)), where T is the number of test cases and O(solve) is the time complexity of the solve() function in the specific implementation
     *  - Space complexity: O(solve), where O(solve) is the space complexity of the solve() function in the specific implementation
     * Additional notes
     *  - Input tests are cleared once the output for the test is printed
     *  - Memory created in solution implementation is cleared once solve() is completed
     */
    // clang-format on
    void run() {
        int T = 0, L = 0, R = 0;
        // Step 1: Read number of test cases from file/console
        cin >> T;
        for (int test_no = 1; test_no <= T; ++test_no) {
            // Step 2.1: Read input for the test case
            cin >> L >> R;
            // Step 2.2: Solve for the given problem
            auto answer = solve(L, R);
            // Step 2.3: Print solution in expected format
            print_answer(answer);
        }
    }
};

// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://www.codechef.com/viewsolution/73824179
 *  - Status: Time Limit Exceeded.
 *  - Runtime: 1.01 sec
 *  - Memory usage: 44.8 M
 * Algorithm metadata:
 *  - Time complexity: O(T*O(L*R)) ~ O(T*L*R), where T is the number of test cases, L and R are end of range
 *  - Space complexity: O(solve), where O(solve) is the space complexity of the solve() function
 *  - Tags:
 *  - Categories:
 * Additional notes
 *  -
 */
// clang-format on
class Solution_01 : public Solution {
 protected:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Time complexity: O(L*R), where L and R are end of range
     * Space complexity: O(L*R), where L and R are end of range
     * Additional notes
     *  -
     */
    // clang-format on
    int solve(int L, int R) override {
        unordered_set<int> unique;
        for (int idx1 = L; idx1 <= R; ++idx1) {
            for (int idx2 = idx1; idx2 <= R; ++idx2) {
                unique.emplace(idx1 + idx2);
            }
        }
        return static_cast<int>(unique.size());
    }
};

// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://www.codechef.com/viewsolution/73824776
 *  - Status: Correct Answer.
 *  - Runtime: 0.02 sec
 *  - Memory usage: 5.3 M
 * Algorithm metadata:
 *  - Time complexity: O(T*O(1)) ~ O(T), where T is the number of test cases
 *  - Space complexity: O(1)
 *  - Tags:
 *  - Categories:
 * Additional notes
 *  -
 */
// clang-format on
class Solution_02 : public Solution {
 protected:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Time complexity: O(1)
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    int solve(int L, int R) override { return (R << 1) - (L << 1) + 1; }
};

int main(int argc, char* argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int solution_no = 2;
    if (argc >= 2) {
        solution_no = stoi(argv[1]);
    }
    unique_ptr<Solution> sol;
    switch (solution_no) {
        case 1:
            sol = make_unique<Solution_01>();
            break;
        case 2:
            sol = make_unique<Solution_02>();
            break;
        default:
            cout << "Solution " << solution_no << " does not exist\n";
            exit(1);
    }
    sol->run();
    return 0;
}
