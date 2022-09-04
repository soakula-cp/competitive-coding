---
Contest Name: START54D - Starters 54 Division 4 (Rated)
Problem Code: EQDIS
Problem Title: Equal Distinct
Problem Difficulty: 
Problem Url: https://www.codechef.com/START54D/problems/EQDIS
Problem Tags: Data Structures, Simple Algos; Algorithms
Editorial Url: https://discuss.codechef.com/problems/EQDIS
Video Editorial Url: https://video.gumlet.io/62c2db7b1a5e497c7a49783d/630f24be5047db4af4ef0af6/main.mpd
Discussion Url: https://discuss.codechef.com/search?q=EQDIS
IsTemplate: No
---


# Problem Statement

Let $F(S)$ denote the number of \*\*distinct\*\* elements in the array $S$. 
For example, $F([1, 2, 3, 2]) = 3, F([1, 2]) = 2.$

You are given an array $A$ containing $N$ integers. Find if it is possible to 
divide the elements of the array $A$ into two arrays $B$ and $C$ such that :
- Every element of the array $A$ belongs either to array $B$ or to array $C$.
- $F(B) = F(C)$.

# Constraints

- $1 \leq T \leq 10^4$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq N$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

# Format

## Input

- The first line of input will contain a single integer $T$, denoting the 
  number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the length of 
      the array $A$.
    - The next line contains $N$ space-separated integer $A_1, A_2, \dots, A_N$, 
      denoting the elements of the array $A$.

## Output

For each test case, print `YES` if it is possible to divide the elements of the 
array $A$ into two arrays $B, C$ satisfying all the conditions and `NO` otherwise.

You may print each character of the string in either uppercase or lowercase 
(for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as 
identical).

# Sample Testcases

## Sample Test 1

**Input:**
3
2
1 2
3
1 2 3
4
3 1 1 2

**Output:**
YES
NO
YES

**Explanation:**
**Test case $1$:** One possible division is $B = [1], C = [2]$. Here 
$F(B) = F(C) = 1.$

**Test case $2$:** There is no way to distribute the elements of the array 
$A = [1, 2, 3]$ satisfying all the conditions.

**Test case $3$:** One possible division is $B = [3, 1], C = [1, 2]$. 
Here $F(B) = F(C) = 2.$

# Useful References/Discussions
