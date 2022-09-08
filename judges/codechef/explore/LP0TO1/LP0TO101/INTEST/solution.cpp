// clang-format off
/**
 * COPYRIGHT NOTICE
 *
 * Copyright (c) 2022. Sona Praneeth Akula <soakula.cp@gmail.com>
 *
 * This file is created for CODECHEF Explore(LP0TO1/LP0TO101)
 * in competitive programming.
 *
 * This file cannot be copied and/or distributed without the express
 * permission of the copyright owner.
 *
 */

/**
 * FILE DESCRIPTION
 *
 *        Filename: INTEST/solution.cpp
 *      Created on: 05 September 2022
 *   Last modified: 05 September 2022
 *          Author: soakula_cp
 *     Description: CODECHEF submission for 'Enormous Input Test' problem
 * Compile command: g++ solution.cpp -std=c++17 -lm -fomit-frame-pointer -pthread -O2 -o solution.exe
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 05-09-2022               soakula_cp      - Creation of file
 */
// clang-format on

#include <iostream>
#include <memory>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::ios_base;
using std::make_unique;
using std::stoi;
using std::unique_ptr;
using std::vector;

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
     *  - n: int - Number of integers to test
     *  - k: int - Divisor
     *  - t: vector<int> - Integers on which test is to be run
     *
     * Returns:
     *  - int - Number of integers divisible by k
     */
    // clang-format on
    virtual int solve(int n, int k, const vector<int>& t) = 0;

 public:
    virtual ~Solution() = default;

    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Actual run to read input tests, solve problem and print output
     *
     * Solution metadata:
     *  - Time complexity: O(solve), where O(solve) is the time complexity of the solve() function in the specific implementation
     *  - Space complexity: O(solve), where O(solve) is the space complexity of the solve() function in the specific implementation
     * Additional notes
     *  - Input tests are cleared once the output for the test is printed
     *  - Memory created in solution implementation is cleared once solve() is completed
     */
    // clang-format on
    void run() {
        int n = 0, k = 0;
        // Step 1: Read number of test cases from file/console
        cin >> n >> k;
        vector<int> t(n, 0);
        for (int i = 1; i <= n; ++i) {
            // Step 1.1: Read input for the test case
            cin >> t[i - 1];
        }
        // Step 2: Solve for the given problem
        auto answer = solve(n, k, t);
        // Step 3: Print solution in expected format
        print_answer(answer);
    }
};

// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link: https://www.codechef.com/viewsolution/73086553
 *  - Status: Correct Answer
 *  - Runtime: 0.16 sec
 *  - Memory usage: 10.5 M
 * Algorithm metadata:
 *  - Time complexity: O(n), where n is size of t
 *  - Space complexity: O(1)
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
     * Time complexity: O(n), where n is size of t
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    int solve(int n, int k, const vector<int>& t) override {
        int answer = 0;
        for (auto t_i : t) {
            answer += static_cast<int>(t_i % k == 0);
        }
        return answer;
    }
};

int main(int argc, char* argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int solution_no = 1;
    if (argc >= 2) {
        solution_no = stoi(argv[1]);
    }
    unique_ptr<Solution> sol;
    switch (solution_no) {
        case 1:
            sol = make_unique<Solution_01>();
            break;
        default:
            cout << "Solution " << solution_no << " does not exist\n";
            exit(1);
    }
    sol->run();
    return 0;
}
