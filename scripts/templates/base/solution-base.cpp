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
    // TODO(TEMPLATE__AUTHOR_ALIAS) :: Update based on problem requirements
    static void print_answer(bool answer) {
#ifdef PRINT_DEBUG
        cout << answer << std::endl;
#else
        cout << answer << "\n";
#endif
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
     *
     * Returns:
     *  - bool - 
     */
    // clang-format on
    // TODO(TEMPLATE__AUTHOR_ALIAS) :: Update function signature
    virtual bool solve(int N) = 0;

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
        int T = 0, N = 0;
        // Step 1: Read number of test cases from file/console
        cin >> T;
        for (int test_no = 1; test_no <= T; ++test_no) {
            // TODO(TEMPLATE__AUTHOR_ALIAS) :: Step 2.1: Read input for the test
            // case
            cin >> N;
            // TODO(TEMPLATE__AUTHOR_ALIAS) :: Step 2.2: Solve for the given
            // problem
            auto answer = solve(N);
            // TODO(TEMPLATE__AUTHOR_ALIAS) :: Step 2.3: Print solution in
            // expected format
            print_answer(answer);
        }
    }
};
