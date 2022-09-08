---
Contest Name: START55D - Starters 55 Division 4 (Rated)
Problem Code: PERMCLEAR
Problem Title: Permutation Clear
Problem Difficulty: 
Problem Url: https://www.codechef.com/START55D/problems/PERMCLEAR
Problem Tags: ; 
Editorial Url: 
Video Editorial Url: 
Discussion Url: https://discuss.codechef.com/search?q=PERMCLEAR
IsTemplate: No
---


# Problem Statement

Alice has an array $A$ of length $N$ which is initially a *permutation*. She 
dislikes $K$ numbers which are $B\_1, B\_2, \ldots, B\_K$ all of which are 
**distinct**. Therefore, she removes all the occurrences of these numbers from 
$A$. The order of the remaining elements of the $A$ does **not** change. 

Can you find out the resulting array $A$?

Note: A *permutation* of length $N$ is an array where every integer from $1$ to 
$N$ occurs exactly once.

# Constraints

- $1 \leq T \leq 1000$
- $1 \leq K \lt N \leq 10^5$
- $1 \le A_i, B_i \le N$
- $A$ is initially a *permutation*.
- $B_i \ne B_j$ when $(i \ne j)$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

# Format

## Input

- The first line contains a single integer $T$ — the number of test cases. 
  Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ integers $A_1, A_2, \ldots, 
  A_N$ denoting the array $A$.
- The third line of each test case contains an integer $K$ — the size of the 
  array $B$.
- The fourth line of each test case contains $K$ integers $B_1, B_2, \ldots, 
  B_K$ denoting the numbers which Alice dislikes.


## Output

For each test case, output the resulting array $A$ after the removal of all 
occurrences of $B_1, B_2, \ldots B_K$.

It is guaranteed that there will be at least one element in the resulting array.

# Sample Testcases

## Sample Test 1

**Input:**
3
4
4 1 3 2
2
3 1
9
5 2 9 1 8 6 4 3 7
3
5 8 9
5
3 4 5 1 2
2
2 3


**Output:**
4 2
2 1 6 4 3 7
4 5 1


**Explanation:**
**Test Case 1:** Here $A = [4, 1, 3, 2]$ and $B = [3, 1]$. The resulting array 
$A$ after removing all the numbers which Alice dislikes is $[4, 2]$.

Note that here $[2, 4]$ is an incorrect answer since the order of elements 
should be the same as in the original array.

**Test Case 2:** Here $A = [5, 2, 9, 1, 8, 6, 4, 3, 7]$ and $B = [5, 8, 9]$. 
The resulting array $A$ after removing all the numbers which Alice dislikes is 
$[2, 1, 6, 4, 3, 7]$.

**Test Case 3:** Here $A = [3, 4, 5, 1, 2]$ and $B = [2, 3]$. The resulting 
array $A$ after removing all the numbers which Alice dislikes is $[4, 5, 1]$.

# Useful References/Discussions
