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
 *        Filename: EQDIS/solution.cpp
 *      Created on: 04 September 2022
 *   Last modified: 04 September 2022
 *          Author: soakula_cp
 *     Description: CODECHEF submission for 'Equal Distinct' problem
 * Compile command: g++ solution.cpp -std=c++17 -lm -fomit-frame-pointer -pthread -O2 -o solution.exe
 */

/**
 * CHANGELOG
 *
 * Date (DD-MM-YYYY)            Author               Update
 * 04-09-2022               soakula_cp      - Creation of file
 */
// clang-format on

#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>
#include <vector>

using std::cin;
using std::cout;
using std::ios_base;
using std::make_unique;
using std::stoi;
using std::unique_ptr;
using std::unordered_map;
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
     *  - N: int - Size of A
     *  - A: vector<int> - Array which needs to assessed on given conditions
     *
     * Returns:
     *  - bool - true if conditions are satisfied else false
     */
    // clang-format on
    virtual bool solve(int N, const vector<int>& A) = 0;

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
        int         T = 0, N = 0;
        vector<int> A;
        // Step 1: Read number of test cases from file/console
        cin >> T;
        for (int test_no = 1; test_no <= T; ++test_no) {
            // Step 2.1: Read input for the test case
            cin >> N;
            A.clear();
            A.resize(N);
            for (int idx = 0; idx < N; ++idx) {
                cin >> A[idx];
            }
            // Step 2.2: Solve for the given problem
            auto answer = solve(N, A);
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
 *  - Submission link: https://www.codechef.com/viewsolution/73065241
 *  - Status: Correct Answer
 *  - Runtime: 0.004477 sec
 *  - Memory usage: 8.1 M
 * Algorithm metadata:
 *  - Time complexity: O(T*O(N)) ~ O(T*N), where T is the number of test cases and N is size of A
 *  - Space complexity: O(N), where N is size of A
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
     * Time complexity: O(N), where N is the size of A
     * Space complexity: O(N), where N is the size of A
     * Additional notes
     *  -
     */
    // clang-format on
    bool solve(int N, const vector<int>& A) override {
        unordered_map<int, int> A_map;
        for (int A_i : A) {
            if (A_map.find(A_i) == end(A_map)) {
                A_map.emplace(A_i, 0);
            }
            A_map[A_i] += 1;
        }
        int numUnique = static_cast<int>(A_map.size()), numNonSingle = 0;
        for (const auto& [key, freq] : A_map) {
            numNonSingle += static_cast<int>(freq > 1);
        }
        if (numUnique <= 2) {
            return true;
        } else {
            if (numUnique & 1) {
                return numNonSingle >= 1;
            }
        }
        return true;
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
