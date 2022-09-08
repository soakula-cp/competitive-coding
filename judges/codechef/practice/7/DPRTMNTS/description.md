---
Problem Code: DPRTMNTS
Problem Title: Departments (Hard Version)
Problem Difficulty: 7*
Problem Url: https://www.codechef.com/problems/DPRTMNTS
Problem Tags: Graphs; Data Structures
Editorial Url: https://discuss.codechef.com/problems/DPRTMNTS
Video Editorial Url: 
Discussion Url: https://discuss.codechef.com/search?q=DPRTMNTS
IsTemplate: No
---

# Problem Statement

\*\*This is the hard version of the problem. The only difference between the easy and hard versions is that in the hard one, there are no constraints on the number of employees in every department.\*\*

ChefCorp has $N$ employees. Each employee belongs to \*\*exactly one\*\* of the $M$ departments. Each department is headed by \*\*exactly one\*\* of the employees belonging to that department.

The management structure of ChefCorp is as follows:
- Each employee of a department (including its head) is \*in contact\* with every other employee of that department.
- The head of each department is \*in contact\* with the heads of all the other departments.

For example, let $N = 7$, $M = 3$ and employees $1, \textbf{2}, 3$ belong to the first department, employees $\textbf{4}, 5$ belong to the second department and employees $\textbf{6}, 7$ belong to the third department (employees in bold represent the heads of the departments). The following pairs of employees are in contact with each other: $(1, 2), (1, 3), (2, 3), (4, 5), (6, 7), (2, 4), (4, 6), (2, 6)$.

However, due to some inexplicable reasons, ChefCorp loses all its data on the departments. Given the total number of employees $N$ and \*\*every pair\*\* of employees who are \*in contact\* with each other, can you help recover the number of departments and the employees belonging to each of the departments?

# Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 1000$
- $1 \leq K \leq \frac{N\cdot(N-1)}{2}$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq K$.
- The sum of $N$ over all test cases does not exceed $3000$.

# Format

## Input

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ — the total number of employees in ChefCorp.
- The second line of each test case contains a single integer $K$ — the number of pairs of employees *in contact* with each other.
- $K$ lines follow. The $i^{th}$ of these $K$ lines contain two space-separated integers $u_i$ and $v_i$, denoting that employee $u_i$ is *in contact* with $v_i$.

## Output

- For each test case, output the following:
    - In the first line output $M$ — the number of departments.
    - In the second line, output $N$ space-separated integers $D_1, D_2, \ldots, D_N$ $(1 \leq D_i \leq M)$ — denoting that the $i^{th}$ employee belongs to the $D_i^{th}$ department.
    - In the third line, output $M$ space-separated integers $H_1, H_2, \ldots, H_M$ $(1 \leq H_i \leq N, H_i \neq H_j$ when $i \neq j)$ — denoting that the $H_i^{th}$ employee is the head of the $i^{th}$ department.

If there are multiple answers, **output any**. It is guaranteed that at least one solution always exists.


# Subtasks



# Sample Testcases

## Sample Test 1

**Input:**
4
7
8
1 2
1 3
2 3
4 5
6 7
2 4
4 6
2 6
2
1
1 2
3
2
3 2
3 1
6
8
6 2
5 4
3 1
5 2
3 6
2 1
6 1
2 3


**Output:**
3
1 1 1 2 2 3 3
2 4 6
2
1 2
1 2
2
1 2 1
3 2
2
1 1 1 2 2 1
2 5


**Explanation:**
**Test case 1:** Explained in the problem statement.


# Useful References/Discussions


