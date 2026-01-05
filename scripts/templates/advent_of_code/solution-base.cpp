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
    static void print_answer(int answer) { cout << answer << "\n"; }

 protected:
    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Function in which solution for the part one of question is calculated
     *
     * Parameters:
     *  - N: int -
     *
     * Returns:
     *  - int -
     */
    // clang-format on
    // TODO(TEMPLATE__AUTHOR_ALIAS) :: Update function signature
    virtual int solve_part_one(int N) = 0;

    // clang-format off
    /**
     * FUNCTION DESCRIPTION
     *
     * Function in which solution for the part two of question is calculated
     *
     * Parameters:
     *  - N: int -
     *
     * Returns:
     *  - int -
     */
    // clang-format on
    // TODO(TEMPLATE__AUTHOR_ALIAS) :: Update function signature
    virtual int solve_part_two(int N) = 0;

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
    void run(int part_no) {
        int N = 0;
        read_input();
        int answer = 0;
        switch (part_no) {
            case 2:
                answer = solve_part_two(N);
                break;
            case 1:
            default:
                answer = solve_part_one(N);
                break;
        }
        print_answer(answer);
    }
};
