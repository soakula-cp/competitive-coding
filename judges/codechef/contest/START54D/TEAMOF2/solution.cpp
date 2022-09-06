// clang-format off
/**
 * COPYRIGHT NOTICE
 *
 * Copyright (c) 2022. Sona Praneeth Akula <soakula.cp@gmail.com>
 *
 * This file is created for CODECHEF Contest(START54D)
 * in competitive programming.
 *
 * This file cannot be copied and/or distributed without the express
 * permission of the copyright owner.
 *
 */

/**
 * FILE DESCRIPTION
 *
 *        Filename: TEAMOF2/solution.cpp
 *      Created on: 04 September 2022
 *   Last modified: 04 September 2022
 *          Author: sonapraneeth_a
 *     Description: CODECHEF submission for 'Team of Two' problem
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
    static void print_answer(bool answer) {
        cout << (answer ? "YES" : "NO") << "\n";
    }

 protected:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Function in which solution for the question is calculated
     *
     * Parameters:
     *  - N: int - Number of students
     *  - K: int - Number of questions attempted by student
     *  - problemsSolvedByEachStudent: vector<vector<int>> - Questions attempted by each student
     *
     * Returns:
     *  - bool - If any team of 2 students can solve all the 5 questions
     */
    // clang-format on
    virtual bool solve(
        int N, int K,
        const vector<vector<int>>& problemsSolvedByEachStudent) = 0;

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
        int                 T = 0, N = 0, K = 0;
        vector<vector<int>> problemsSolvedByEachStudent;
        // Step 1: Read number of test cases from file/console
        cin >> T;
        for (int test_no = 1; test_no <= T; ++test_no) {
            // Step 2.1: Read input for the test case
            cin >> N;
            problemsSolvedByEachStudent.clear();
            problemsSolvedByEachStudent.resize(N);
            for (int s_idx = 0; s_idx < N; ++s_idx) {
                cin >> K;
                problemsSolvedByEachStudent[s_idx].resize(K);
                for (int idx = 0; idx < K; ++idx) {
                    cin >> problemsSolvedByEachStudent[s_idx][idx];
                }
            }
            // Step 2.2: Solve for the given problem
            auto answer = solve(N, K, problemsSolvedByEachStudent);
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
 *  - Submission link: https://www.codechef.com/viewsolution/73065509
 *  - Status: Correct Answer
 *  - Runtime: 0.005707 sec
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
class Solution_01 : public Solution {
 protected:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Time complexity: O(N*K + N*N) ~ O(N*(N+5)) ~ O(N*2) ~ O(400) ~ O(1), where N is the number of students and K is the number of questions (5)
     * Space complexity: O(N) ~ O(20) ~ O(1), where N is the number of students
     * Additional notes
     *  -
     */
    // clang-format on
    bool solve(
        int N, int K,
        const vector<vector<int>>& problemsSolvedByEachStudent) override {
        vector<int> solvedProblemsConfig(N, 0);
        for (int s_idx = 0; s_idx < N; ++s_idx) {
            int solve_config = 0;
            for (int idx = 0; idx < problemsSolvedByEachStudent[s_idx].size();
                 ++idx) {
                solve_config |=
                    (1 << (problemsSolvedByEachStudent[s_idx][idx] - 1));
            }
            solvedProblemsConfig[s_idx] = solve_config;
        }
        for (int p1_idx = 0; p1_idx < N; ++p1_idx) {
            for (int p2_idx = p1_idx + 1; p2_idx < N; ++p2_idx) {
                // 31 -> 11111 which means all questions solved
                if ((solvedProblemsConfig[p1_idx] |
                     solvedProblemsConfig[p2_idx]) == 31) {
                    return true;
                }
            }
        }
        solvedProblemsConfig.clear();
        return false;
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
