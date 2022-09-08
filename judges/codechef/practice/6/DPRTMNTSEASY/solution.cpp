// clang-format off
/**
 * COPYRIGHT NOTICE
 *
 * Copyright (c) 2022. Sona Praneeth Akula <soakula.cp@gmail.com>
 *
 * This file is created for CODECHEF Practice in competitive programming.
 *
 * This file cannot be copied and/or distributed without the express
 * permission of the copyright owner.
 *
 */

/**
 * FILE DESCRIPTION
 *
 *        Filename: DPRTMNTSEASY/solution.cpp
 *      Created on: 06 September 2022
 *   Last modified: 06 September 2022
 *          Author: soakula_cp
 *     Description: CODECHEF submission for 'Departments (Easy Version)' problem
 * Compile command: g++ solution.cpp -std=c++17 -lm -fomit-frame-pointer -pthread -O2 -o solution.exe
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 06-09-2022               soakula_cp      - Creation of file
 */
// clang-format on

#include <iostream>
#include <memory>
#include <string>
#include <utility>
#include <vector>

using std::cin;
using std::cout;
using std::ios_base;
using std::make_unique;
using std::pair;
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
     * Time complexity: O(N+M), where N is total number of people and M is number of managers
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    static void print_answer(int M, const vector<int> &D,
                             const vector<int> &H) {
        cout << M << "\n";
        // Employee to department map
        for (auto D_i : D) {
            cout << D_i << " ";
        }
        cout << "\n";
        // Department to manager map
        for (auto H_i : H) {
            cout << H_i << " ";
        }
        cout << "\n";
    }

 protected:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Function in which solution for the question is calculated
     *
     * Parameters:
     *  - N: int -
     *  - K: int -
     *  - contactEmployees: vector<pair<int,int> -
     *
     * Returns:
     *  - bool -
     */
    // clang-format on
    virtual int solve(int N, int K,
                      const vector<pair<int, int>> &contactEmployees,
                      vector<int> &D, vector<int> &H) = 0;

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
        int         T = 0, N = 0, K = 0;
        vector<int> contactEmployees, D, H;
        // Step 1: Read number of test cases from file/console
        cin >> T;
        for (int test_no = 1; test_no <= T; ++test_no) {
            contactEmployees.clear();
            D.clear();
            H.clear();
            // Step 2.1: Read input for the test case
            cin >> N >> K;
            contactEmployees.resize(K, {0, 0});
            for (int pair_idx = 0; pair_idx < K; ++pair_idx) {
                cin >> contactEmployees[pair_idx].first >>
                    contactEmployees[pair_idx].second;
            }
            // Step 2.2: Solve for the given problem
            auto answer = solve(N, K, contactEmployees, D, H);
            // Step 2.3: Print solution in expected format
            print_answer(answer, D, H);
        }
    }
};

// clang-format off
/**
 * CLASS DESCRIPTION
 *
 * Judge metadata:
 *  - Submission link:
 *  - Status: .
 *  - Runtime:  sec
 *  - Memory usage:  M
 * Algorithm metadata:
 *  - Time complexity: O(T*O(solve)), where T is the number of test cases and O(solve) is the time complexity of the solve() function
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
     * Time complexity: O(N), where N is the input
     * Space complexity: O(1)
     * Additional notes
     *  -
     */
    // clang-format on
    int solve(int N, int K, const vector<pair<int, int>> &contactEmployees,
              vector<int> &D, vector<int> &H) override {
        vector<vector<int>> graph(N, {});
        int                 M = 0;
        for (const auto &contactEmployee : contactEmployees) {
            graph[contactEmployee.first].emplace_back(contactEmployee.second);
            graph[contactEmployee.second].emplace_back(contactEmployee.first);
        }
        return M;
    }
};

int main(int argc, char *argv[]) {
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
