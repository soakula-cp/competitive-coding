---
Contest Name: LP2TO301 - Basic programming concepts
Problem Code: INDIPERM
Problem Title: Indivisible Permutation
Problem Difficulty: 
Problem Url: https://www.codechef.com/LP2TO301/problems/INDIPERM
Problem Tags: ; 
Editorial Url: 
Video Editorial Url: https://video.gumlet.io/62c2db7b1a5e497c7a49783d/62d4f9ef6717eda2b0eeadc7/main.mpd
Discussion Url: https://discuss.codechef.com/search?q=INDIPERM
IsTemplate: No
---


# Problem Statement

You are given an integer $N$. Construct an array $P$ of size $N$ such that:

- $P$ is a permutation of the first $N$ natural numbers, i.e, each integer 
  $1, 2, 3, \ldots N$ occurs exactly once in $P$. For example, $[1, 3, 2]$ is a 
  permutation of size $3$, but $[1, 3, 4]$ and $[2, 1, 2]$ are not.
- $P$ is **indivisible**. $P$ is said to be **indivisible** if $i$ does 
  not divide $P\_i$ for every index $2 \leq i \leq N$.

It can be proven that under the given constraints, there always exists an 
**indivisible** permutation. If there are multiple, you may print any of them.

# Constraints

- $1 \leq T \leq 600$
- $2 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

# Format

## Input

- The first line of input contains a single integer $T$, denoting the number of 
  test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$, 
  denoting the size of the indivisible permutation you must construct.


## Output

- For every test case, print a single line containing $N$ space-separated 
  integers. These integers must form an **indivisible**  permutation.

# Sample Testcases

## Sample Test 1

**Input:**
4
2
3
4
5

**Output:**
2 1 
1 3 2 
1 3 4 2 
4 5 2 3 1 

**Explanation:**
- For the last test case:
    - $P_2 = 5$ is not divisible by $2$
    - $P_3 = 2$ is not divisible by $3$
    - $P_4 = 3$ is not divisible by $4$
    - $P_5 = 1$ is not divisible by $5$
- Since $i$ does not divide $P_i$ for every index $2\leq i\leq N$, the 
  permutation is **indivisible**.

# Useful References/Discussions
