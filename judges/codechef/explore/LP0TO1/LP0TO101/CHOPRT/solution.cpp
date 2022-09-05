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
 *        Filename: CHOPRT/solution.cpp
 *      Created on: 04 September 2022
 *   Last modified: 04 September 2022
 *          Author: sonapraneeth_a
 *     Description: CODECHEF submission for 'Chef And Operators' problem
 * Compile command: g++ solution.cpp -std=c++17 -lm -fomit-frame-pointer -pthread -O2 -o solution.exe
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 04-09-2022               sonapraneeth_a      - Creation of file
 */
// clang-format on

#include <iostream>
#include <memory>
#include <string>

using std::cin;
using std::cout;
using std::ios_base;
using std::make_unique;
using std::stoi;
using std::unique_ptr;

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
    static void print_answer(char answer) { cout << answer << "\n"; }

 protected:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Function in which solution for the question is calculated
     *
     * Parameters:
     *  - A: int - Integer 1
     *  - B: int - Integer 2
     *
     * Returns:
     *  - char - Comparison operation between A and B.
     */
    // clang-format on
    virtual char solve(int A, int B) = 0;

 public:
    virtual ~Solution() = default;

    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Actual run to read input tests, solve problem and print output
     *
     * Time complexity: O(T*O(solve)), where T is the number of test cases and O(solve) is the time complexity of the solve() function in the specific implementation
     * Space complexity: O(solve), where O(solve) is the space complexity of the solve() function in the specific implementation
     * Additional notes
     *  - Input tests are cleared once the output for the test is printed
     *  - Memory created in solution implementation is cleared once solve() is completed
     */
    // clang-format on
    void run() {
        int T = 0, A = 0, B = 0;
        // Step 1: Read number of test cases from file/console
        cin >> T;
        for (int test_no = 1; test_no <= T; ++test_no) {
            // Step 2.1: Read input for the test case
            cin >> A >> B;
            // Step 2.2: Solve for the given problem
            auto answer = solve(A, B);
            // Step 2.3: Print solution in expected format
            print_answer(answer);
        }
    }
};

// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge:
 *  - Submission link: https://www.codechef.com/viewsolution/73066779
 *  - Status: Correct Answer
 *  - Runtime: 0.00 sec
 *  - Memory usage: 5.3 M
 * Time complexity: O(T*O(1)), where T is the number of test cases
 * Space complexity: O(1)
 * Tags:
 * Categories:
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
     * Time complexity: O(1)
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    char solve(int A, int B) override {
        return ((A > B) ? '>' : ((A < B) ? '<' : '='));
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